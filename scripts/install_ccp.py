import os
import sys
import shutil
import subprocess

def install(target_dir):
    # Absolute paths
    source_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_root = os.path.abspath(target_dir)

    if not os.path.isdir(target_root):
        print(f"❌ Target directory does not exist: {target_root}")
        sys.exit(1)

    print(f"🌍 Installing CCP from {source_root} to {target_root}...")

    # 1. Copy SYSTEM_PROMPT.md
    print("📜 Installing SYSTEM_PROMPT.md...")
    shutil.copy(os.path.join(source_root, "SYSTEM_PROMPT.md"), target_root)
    
    # 2. Setup Scripts
    print("🛠️  Installing scripts...")
    target_scripts = os.path.join(target_root, "scripts")
    os.makedirs(target_scripts, exist_ok=True)
    shutil.copy(os.path.join(source_root, "scripts", "update_maps.py"), target_scripts)

    # 3. Setup World Map
    target_map = os.path.join(target_root, "WORLD_MAP.md")
    if not os.path.exists(target_map):
        print("🗺️  Creating WORLD_MAP.md...")
        shutil.copy(os.path.join(source_root, "templates", "WORLD_MAP.template.md"), target_map)
    else:
        print("⏭️  WORLD_MAP.md already exists, skipping.")

    # 4. Bootstrap Legends
    print("📍 Bootstrapping Legends in all folders...")
    legend_template_path = os.path.join(source_root, "templates", "LEGEND.template.md")
    with open(legend_template_path, "r", encoding="utf-8") as f:
        legend_content = f.read()
    
    ignore = {".git", "node_modules", "dist", "build", ".next", "coverage", "__pycache__", "venv", ".venv"}
    
    created_count = 0
    for root, dirs, files in os.walk(target_root):
        dirs[:] = [d for d in dirs if d not in ignore]
        
        legend_path = os.path.join(root, "LEGEND.md")
        if not os.path.exists(legend_path):
            folder_name = os.path.basename(root) if root != target_root else "Root"
            # Simple template filling
            content = legend_content.replace("[Current Folder Name]", folder_name)
            
            with open(legend_path, "w", encoding="utf-8") as f:
                f.write(content)
            created_count += 1
    
    print(f"   - Created {created_count} new LEGEND.md files.")

    # 5. Run update_maps
    print("🤖 Running Auto-Cartographer to index files...")
    update_script = os.path.join(target_scripts, "update_maps.py")
    
    # Run in the target directory so pathing works
    subprocess.run([sys.executable, update_script], cwd=target_root)
    
    print("\n✅ CCP Installation Complete!")
    print("👉 Next Step: Open 'WORLD_MAP.md' in the target repo and fill in your Regions.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python install_ccp.py <target_directory>")
        sys.exit(1)
        
    install(sys.argv[1])
