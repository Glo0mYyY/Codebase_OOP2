import xml.etree.ElementTree as ET

# XML-Datei öffnen
tree = ET.parse('books.xml')
root = tree.getroot()

# Titel aller Bücher ausgeben
for book in root.iter('book'):
    title = book.find('title').text
    print(title)

# Jahr des ersten Buches ändern
first_book = root.find('book')
year_element = first_book.find('year')
year_element.text = '2022'

# XML-Datei speichern
tree.write('books.xml')
