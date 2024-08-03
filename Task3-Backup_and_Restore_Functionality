# Python-Project3
import pandas as pd
import xml.etree.ElementTree as ET

def read_excel(file_path):
    df = pd.read_excel(file_path)
    return df
    
def update_xml_with_excel_data(xml_file, excel_file, output_xml_file):

    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    df = read_excel(excel_file)
    
    new_root = ET.Element('Root')
    
    for index, row in df.iterrows():
        item = ET.SubElement(new_root, 'Item')
        for col in df.columns:
            child = ET.SubElement(item, col)
            child.text = str(row[col])
    
    new_tree = ET.ElementTree(new_root)
    new_tree.write(output_xml_file, encoding='utf-8', xml_declaration=True)

xml_file = 'C:\\Users\\Lenovo\\Desktop\\settings_files\\projecttask.xml'
excel_file = 'C:\\Users\\Lenovo\\Desktop\\Project\\excel1.xlsx'
output_xml_file = 'new_data.xml'
update_xml_with_excel_data(xml_file, excel_file, output_xml_file)
print("New Data Updated Successfully")
