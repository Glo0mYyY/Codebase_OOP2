import json
import os
import xml.etree.ElementTree as ET

def xml_to_json(xml_file, json_file):
    os.chdir(os.path.dirname(os.path.abspath(__file__))) # Script Pfad setzen
    tree = ET.parse(xml_file)
    root = tree.getroot()

    def parse_element(element): # Nested Funktion - Looped für jedes Child
        result = {}
        if element.text and element.text.strip():
            result[element.tag] = element.text.strip() # Whitespace entfernen
        for child in element:
            result[child.tag] = parse_element(child) # Nested, looped bis keine child-elemente
        return result

    data = parse_element(root)

    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

xml_to_json('book.xml', 'book.json')