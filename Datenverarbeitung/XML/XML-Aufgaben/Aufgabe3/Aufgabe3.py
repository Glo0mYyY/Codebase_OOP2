import xml.etree.ElementTree as ET
import os

def create_fruits_xml():
    fruits = ET.Element("fruits")

    apple = ET.SubElement(fruits, "fruit", name="Apple",color="red", price="1.5")
    banana = ET.SubElement(fruits, "fruit", name="Banana",color="yellow", price="0.5")
    orange = ET.SubElement(fruits, "fruit", name="Orange",color="orange", price="0.8")

    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "fruits.xml")

    tree = ET.ElementTree(fruits)
    with open(file_path, "wb") as xml_file:
        tree.write(xml_file, encoding="utf-8", xml_declaration=True)

create_fruits_xml()