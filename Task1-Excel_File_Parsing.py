import pandas as pd

workbook = pd.read_excel('C:/Users/Lenovo/Desktop/ani/application/relay_data1.xlsx')
error_occurred = False

for col in workbook.columns[1:]:
    try:
        workbook[col] = pd.to_numeric(workbook[col], errors='raise')
    except ValueError:
        print(f"Error occurred while converting column '{col}' to numeric.")
        error_occurred = True

if not error_occurred:
    print(workbook)