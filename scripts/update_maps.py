import os
import re
import logging
import argparse

# 1. Setup Robust Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger("CCP-Cartographer")

class Cartographer:
    """Handles the maintenance of LEGEND.md files within a CCP-compliant repository."""
    
    START_MARKER = "<!-- CCP_INVENTORY_START -->"
    END_MARKER = "<!-- CCP_INVENTORY_END -->"
    IGNORED_DIRS = {".git", "node_modules", "dist", "build", ".next", "venv", ".venv"}

    def __init__(self, root_dir):
        self.root_dir = root_dir

    def get_inventory(self, directory):
        """Returns a sorted list of files in the directory, excluding the Legend and hidden files."""
        try:
            return sorted([
                f for f in os.listdir(directory)
                if os.path.isfile(os.path.join(directory, f))
                and not f.startswith(".")
                and f != "LEGEND.md"
            ])
        except OSError as e:
            logger.error(f"Could not access directory {directory}: {e}")
            return []

    def parse_existing_legend(self, text, current_files):
        """Extracts existing descriptions from the Legend to prevent overwriting human work."""
        existing_meta = {}
        # Regex to find: | `filename` | Purpose | (supports both 2 and 3 column formats)
        # Try 2-column format first (minimal standard)
        pattern_2col = r"\|\s*`([^`]+)`\s*\|\s*([^|]+)\|"
        rows = re.findall(pattern_2col, text)
        
        for name, purpose in rows:
            clean_name = name.strip()
            if clean_name in current_files:
                existing_meta[clean_name] = purpose.strip()
        return existing_meta

    def update_directory(self, directory):
        """Updates or verifies the LEGEND.md file for a single directory."""
        legend_path = os.path.join(directory, "LEGEND.md")
        
        if not os.path.exists(legend_path):
            return # Protocol: LEGEND creation is a human architectural choice

        files = self.get_inventory(directory)
        
        try:
            with open(legend_path, "r", encoding="utf-8") as f:
                content = f.read()

            if self.START_MARKER not in content or self.END_MARKER not in content:
                logger.warning(f"Skipping {directory}: Markers missing in LEGEND.md")
                return

            before, rest = content.split(self.START_MARKER, 1)
            _, after = rest.split(self.END_MARKER, 1)

            meta = self.parse_existing_legend(content, files)
            
            new_rows = []
            for f in files:
                # Per PROTOCOLS.md: per-file purposes are optional
                purpose = meta.get(f, "Optional")
                # Normalize empty or TODO purposes to "Optional"
                if not purpose or "TODO" in purpose:
                    purpose = "Optional"
                new_rows.append(f"| `{f}` | {purpose} |")

            inventory_table = "\n".join([
                self.START_MARKER,
                "| File | Purpose |",
                "| :--- | :--- |",
                *new_rows,
                self.END_MARKER
            ])

            updated_content = f"{before}{inventory_table}{after}"

            with open(legend_path, "w", encoding="utf-8") as f:
                f.write(updated_content)
            
            logger.info(f"✅ Map Synced: {os.path.relpath(directory, self.root_dir)}")

        except Exception as e:
            logger.error(f"Failed to process {legend_path}: {e}")

    def run(self):
        """Walks the repository and updates all Legends."""
        for dirpath, dirnames, _ in os.walk(self.root_dir):
            dirnames[:] = [d for d in dirnames if d not in self.IGNORED_DIRS]
            self.update_directory(dirpath)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CCP Auto-Cartographer v1.3.3")
    parser.add_argument("path", nargs="?", default=os.getcwd(), help="Path to the repository root")
    args = parser.parse_args()
    
    cartographer = Cartographer(args.path)
    logger.info("🗺️ Starting CCP Map Synchronization...")
    cartographer.run()
    logger.info("✨ Synchronization Complete.")
