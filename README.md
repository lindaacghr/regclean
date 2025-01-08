# RegClean

RegClean is a Python program designed to perform a deep clean of the Windows registry. It identifies and removes unused and old entries, which can help boost system performance.

## Features

- Scans specified registry paths to find and remove obsolete entries.
- Logs actions and errors to a file (`regclean.log`) for easy review.
- Improves system performance by cleaning up the registry.

## Prerequisites

- Python 3.x
- Windows operating system

## Installation

1. Clone the repository or download the `regclean.py` file.
2. Ensure Python is installed on your system.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing `regclean.py`.
3. Run the script using Python:

   ```bash
   python regclean.py
   ```

## Warnings

- This script modifies the Windows registry. Ensure you have a backup of your registry before running the script.
- Administrator privileges are required to modify the registry. Run the script as an administrator.
- The paths provided in the script are examples. Modify them according to the specific registry entries you wish to clean.

## Logging

All actions and errors are logged to `regclean.log` in the script's directory. Review this file for details on what was cleaned and any issues encountered.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.