# Version 1.2.2 Changelog

## 🚀 New Features & Improvements

*   **Modular Architecture**: Refactored the script into a `Cartographer` class, making the code more modular, maintainable, and extensible for future features (e.g., Dependency Mapping).
*   **Robust Logging**: Replaced standard `print` statements with Python's built-in `logging` module. This allows for timestamped logs, log levels (INFO, WARNING, ERROR), and easier integration with external logging tools or file redirection.
*   **Enhanced Error Handling**: Implemented comprehensive `try-except` blocks and specific `OSError` handling. The script now gracefully handles inaccessible directories or locked files without crashing the entire process.
*   **Flexible CLI Execution**: Added `argparse` support. You can now execute the script against any target directory by passing the path as an argument (e.g., `python update_maps.py /path/to/repo`). It defaults to the current working directory if no argument is provided.
*   **Improved Output**: Standardized log formatting includes timestamps and clear status indicators (e.g., ✅ Map Synced), providing better visibility into the script's operations.

## 🐛 Bug Fixes

*   Fixed potential crashing issues when encountering file permission errors during directory traversal.

## 🔒 Security & Safety

*   Preserved the logic for `LEGEND.md` updates to ensure existing human-written descriptions and dependencies are **never** overwritten, adhering to the "Human-in-the-Loop" philosophy.
