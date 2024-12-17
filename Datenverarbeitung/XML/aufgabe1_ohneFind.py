import xml.etree.ElementTree as ET

baum = ET.parse('books.xml')
wurzel = baum.getroot()

print("Titel aller Bücher:")
for buch in wurzel:
    titel = buch[0].text
    print(f"Titel: {titel}")

erstes_buch = wurzel[0]
jahr_element = erstes_buch[2]
neues_jahr = "2023"
jahr_element.text = neues_jahr
print(f"Das Jahr des ersten Buches wurde auf {neues_jahr} geändert.")

baum.write('books_aktualisiert.xml')
print("Aktualisierte XML wurde als 'books_aktualisiert.xml' gespeichert.")
