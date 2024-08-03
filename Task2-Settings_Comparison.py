
import pandas as pd
import xml.etree.ElementTree as ET

# Read Excel file
excel_file = 'C:/Users/Lenovo/Desktop/settings_files/task2OUTPUT.xlsx'
df_excel = pd.read_excel(excel_file, index_col='relayed_id')  # Assuming 'relayed_id' is the index column

# Parse XML file
xml_file = 'C:/Users/Lenovo/Desktop/settings_files/projecttask.xml'
tree = ET.parse(xml_file)
root = tree.getroot()

# Extract relay data from XML
relay_data_xml = {}
for relay in root.findall('./settings/relay'):
    relay_id = relay.get('id')
    parameters = {}
    for param in relay.findall('parameter'):
        parameters[param.get('name')] = param.get('value')
    relay_data_xml[relay_id] = parameters

# Compare data
for relay_id, parameters_excel in df_excel.iterrows():
    if relay_id in relay_data_xml:
        parameters_xml = relay_data_xml[relay_id]
        for param_name, param_value_excel in parameters_excel.items():
            if param_name in parameters_xml:
                param_value_xml = parameters_xml[param_name]
                # Compare param_value_excel with param_value_xml as needed
                # Example: print comparison results
                print(f"Relay {relay_id}, Parameter {param_name}: Excel={param_value_excel}, XML={param_value_xml}")
            else:
                print(f"Parameter {param_name} not found for Relay {relay_id} in XML data")
    else:
        print(f"Relay {relay_id} not found in XML data")
