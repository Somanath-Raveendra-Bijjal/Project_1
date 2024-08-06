# Task1 : Excel File Parsing

This repository contains a Python script to parse AWS parameters from an Excel file and extract relevant data.

## How to Run the Python Script

Save the script as Task1-Excel_File_Parsing.py, Open your terminal or command prompt.

Run the script with the command.

python Task1-Excel_File_Parsing.py


----------------------------------------------------------------------------------------------------------------------------

# Task :2 Settings Comparison

This repository contains a Python script to compare settings from an Excel file with settings in an XML file and highlight discrepancies.

## Script Overview

The script performs the following tasks:
1. **Reads** settings data from an Excel file.
2. **Parses** relay settings from an XML file.
3. **Compares** the settings from both files.
4. **Prints** out discrepancies and missing parameters.

### How to Run the Python Script

1. **Save** the script as `Settings_Comparison.py`.

2. **Ensure** that you have Python installed on your system.

3. **Install** the required libraries if you haven't already. Open your terminal or command prompt and run:


----------------------------------------------------------------------------------------------------------------------------

# Task : 3 Backup_and_Restore_Functionality

This repository contains a Python script to update an XML file with data from an Excel file.

## Script Overview

The script performs the following tasks:
1. **Reads** data from an Excel file.
2. **Parses** an existing XML file.
3. **Updates** the XML file by adding new data from the Excel file.
4. **Saves** the updated XML to a new file.

### How to Run the Python Script

1. **Save** the script as `Update_XML_With_Excel.py`.

2. **Ensure** that you have Python installed on your system.

3. **Install** the required libraries if you haven't already. Open your terminal or command prompt and run:


----------------------------------------------------------------------------------------------------------------------------

# Task : 4 Logging and Error Handling

This repository contains a Python script that enhances backup and restore functionality with robust logging and error handling mechanisms.

## Script Overview

The script performs the following tasks:
1. **Creates** backups of specified directories.
2. **Restores** directories from a backup.
3. **Logs** the entire process, including directory creation, backup, restoration, and error handling.

### How to Run the Python Script

1. **Save** the script as `backup_restore_with_logging.py`.

2. **Ensure** that you have Python installed on your system.

3. **Install** the required libraries if you haven’t already. For this script, you only need the standard library, which is included with Python.

4. **Update** the script with appropriate directory paths:
   - **`source_dirs`**: List of directories you want to back up.
   - **`backup_location`**: Directory where backups will be stored.
   - **`restore_dirs`**: List of directories where backups will be restored.

5. **Open Terminal or Command Prompt:**
   - **Windows:** Search for "Command Prompt" or "PowerShell" and open it.
   - **Mac/Linux:** Open the Terminal application.

6. **Navigate** to the directory where you saved the script. Use the `cd` command to change to the directory.


----------------------------------------------------------------------------------------------------------------------------

# Task : 5 Unit Testing and Test Automation

This repository contains a Python script for backing up and restoring directories, enhanced with logging and error handling. 
This section describes how to test the functionality of the script using the `unittest` framework.

## Testing Framework

For testing the script, we use Python's built-in `unittest` framework. This allows us to write and run test cases to ensure that the script functions as expected.

### How to Run the Tests

1. **Save** the test script as `test_bulk_pst.py`.

2. **Ensure** that you have Python installed on your system.

3. **Prepare the Test Environment:**
   - The test script creates temporary directories and files for testing purposes. Ensure that you have appropriate permissions to create and delete directories in the location where you run the tests.

4. **Open Terminal or Command Prompt:**
   - **Windows:** Search for "Command Prompt" or "PowerShell" and open it.
   - **Mac/Linux:** Open the Terminal application.

5. **Navigate** to the directory where you saved the test script. Use the `cd` command to change to the directory.
