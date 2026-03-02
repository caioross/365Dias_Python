import csv
import xml.etree.ElementTree as ET

def csv_to_xml(csv_file_path, xml_file_path):
    """
    Convert a CSV file to an XML file.

    Args:
    csv_file_path (str): The path to the CSV file.
    xml_file_path (str): The path to the XML file to be created.
    """
    # Create the root element
    root = ET.Element("Records")

    # Open the CSV file and read data
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # Create a record element for each row
            record = ET.SubElement(root, "Record")
            for key, value in row.items():
                # Create a child element for each column
                child = ET.SubElement(record, key)
                child.text = value

    # Create an ElementTree object and write to an XML file
    tree = ET.ElementTree(root)
    tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

def main():
    """
    Main function to execute the CSV to XML conversion.
    """
    csv_file_path = 'input.csv'
    xml_file_path = 'output.xml'
    csv_to_xml(csv_file_path, xml_file_path)
    print(f"CSV file '{csv_file_path}' has been converted to XML file '{xml_file_path}'.")

if __name__ == '__main__':
    main()