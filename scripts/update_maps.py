import os
import re

IGNORED_DIRS = {
    ".git", "node_modules", "dist", "build", ".next",
    "coverage", "__pycache__", "venv", ".venv"
}

START = "<!-- CCP_INVENTORY_START -->"
END = "<!-- CCP_INVENTORY_END -->"

def list_files(directory):
    return sorted([
        f for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
        and not f.startswith(".")
        and f != "LEGEND.md"
    ])

def update_legend(directory):
    legend_path = os.path.join(directory, "LEGEND.md")
    files = list_files(directory)

    if not os.path.exists(legend_path):
        return  # LEGEND creation is a human decision

    with open(legend_path, "r") as f:
        text = f.read()

    if START not in text or END not in text:
        print(f"⚠️  Skipping {directory}: missing inventory markers")
        return

    before, rest = text.split(START, 1)
    _, after = rest.split(END, 1)

    existing = {}
    rows = re.findall(r"\|\s*`([^`]+)`\s*\|\s*([^|]+)\|\s*([^|]+)\|", text)
    for name, purpose, deps in rows:
        existing[name] = (purpose.strip(), deps.strip())

    new_rows = []
    for f in files:
        if f in existing:
            purpose, deps = existing[f]
        else:
            purpose, deps = "📝 TODO: Describe responsibility", "*Auto-detected*"
        new_rows.append(f"| `{f}` | {purpose} | {deps} |")

    inventory = "\n".join([
        START,
        "| File | Purpose | Dependencies |",
        "| :--- | :--- | :--- |",
        *new_rows,
        END
    ])

    updated = before + inventory + after

    with open(legend_path, "w") as f:
        f.write(updated)

    print(f"✅ Updated inventory: {directory}")

def walk_repo(root):
    for dirpath, dirnames, _ in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]
        update_legend(dirpath)

if __name__ == "__main__":
    walk_repo(os.getcwd())
