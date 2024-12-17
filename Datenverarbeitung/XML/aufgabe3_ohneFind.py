import xml.etree.ElementTree as ET

wurzel = ET.Element("fruits")

apfel = ET.Element("fruit")
apfel.attrib["name"] = "Apple"
apfel.attrib["color"] = "red"
apfel.attrib["price"] = "1.5"
wurzel.append(apfel)

banane = ET.Element("fruit")
banane.attrib["name"] = "Banana"
banane.attrib["color"] = "yellow"
banane.attrib["price"] = "0.5"
wurzel.append(banane)

orange = ET.Element("fruit")
orange.attrib["name"] = "Orange"
orange.attrib["color"] = "orange"
orange.attrib["price"] = "0.8"
wurzel.append(orange)

baum = ET.ElementTree(wurzel)
baum.write("fruits.xml")
print("Die XML-Datei 'fruits.xml' wurde erfolgreich erstellt.")
