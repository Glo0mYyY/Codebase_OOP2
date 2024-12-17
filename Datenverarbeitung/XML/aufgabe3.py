import xml.etree.ElementTree as ET

# Neues Element erstellen
fruits = ET.Element('fruits')

# Fruit-Elemente hinzufügen
apple = ET.SubElement(fruits, 'fruit')
apple.set('name', 'Apple')
apple.set('color', 'red')
apple.set('price', '1.5')

banana = ET.SubElement(fruits, 'fruit')
banana.set('name', 'Banana')
banana.set('color', 'yellow')
banana.set('price', '0.5')

orange = ET.SubElement(fruits, 'fruit')
orange.set('name', 'Orange')
orange.set('color', 'orange')
orange.set('price', '0.8')

# ElementTree erstellen und in Datei speichern
tree = ET.ElementTree(fruits)
tree.write('fruits.xml')
