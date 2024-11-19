import xml.etree.ElementTree as ET
import os


def create_fruits_xml():
    # Wurzelelement erstellen
    fruits = ET.Element("fruits")

    # Fruchtelemente erstellen
    apple = ET.SubElement(fruits, "fruit", name="Apple",
                          color="red", price="1.5")
    banana = ET.SubElement(fruits, "fruit", name="Banana",
                           color="yellow", price="0.5")
    orange = ET.SubElement(fruits, "fruit", name="Orange",
                           color="orange", price="0.8")

    # Pfad zum Verzeichnis des aktuell laufenden Skripts bekommen und Datei speichern
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "fruits.xml")

    # Baum erstellen und in Datei speichern
    tree = ET.ElementTree(fruits)
    with open(file_path, "wb") as xml_file:
        tree.write(xml_file, encoding="utf-8", xml_declaration=True)


# Funktion aufrufen, um die fruits.xml Datei zu erstellen
create_fruits_xml()
