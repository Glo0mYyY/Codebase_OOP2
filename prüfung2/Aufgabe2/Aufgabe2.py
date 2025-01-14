import os
import xml.etree.ElementTree as ET

source = os.path.join(os.path.dirname(__file__), 'employees.xml')

XMLcontent = ET.parse(source)
root = XMLcontent.getroot()


def parse_element(element):  # Nested Funktion - Looped für jedes Child
    result = {}
    projects = []
    if element.text and element.text.strip():
        result[element.tag] = element.text.strip()  # Whitespace entfernen
    for child in element:
        # Nested, looped bis keine child-elemente
        result[child.tag] = parse_element(child)
        if child.tag == "project":
            projects.append(child.text)
    if projects.count == 0:
        return "none"
    else: 
        return print(projects)


for employee in root.iter('employee'):
    parse_element(employee)
#data = parse_element(root)