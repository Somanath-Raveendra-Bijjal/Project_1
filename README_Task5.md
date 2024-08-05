# Backup and Restore Functionality

This repository contains Python scripts for backing up and restoring directories, including test cases to ensure functionality.

## Script Overview

### Backup and Restore Script

The script performs the following tasks:
1. **Creates a Backup:** Copies specified directories to a backup location with a timestamped folder.
2. **Restores from Backup:** Restores specified directories from a backup folder.

### Testing Script

The testing script includes unit tests for the `create_backup` function to verify:
1. **Successful Backup Creation:** Ensures that the backup directory and files are created correctly.
2. **Handling Non-Existent Directories:** Checks that the function raises an error when attempting to back up a non-existent directory.

## How to Run the Python Scripts

1. **Save** the scripts as `Backup_and_Restore.py` and `test_backup_and_restore.py`.

2. **Ensure** that you have Python installed on your system.

3. **Install** the required libraries if you haven't already. Open your terminal or command prompt and run:
