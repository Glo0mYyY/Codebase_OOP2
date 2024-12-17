import xml.etree.ElementTree as ET

baum = ET.parse('students.xml')
wurzel = baum.getroot()

print("Namen und Noten der Studenten:")
for student in wurzel:
    name = student[0].text
    note = student[2].text
    print(f"Name: {name}, Note: {note}")

letzter_student = wurzel[-1]
alter_element = letzter_student[1]
neues_alter = int(alter_element.text) + 1
alter_element.text = str(neues_alter)
print(f"Das Alter des letzten Studenten wurde auf {neues_alter} erhöht.")

baum.write('students_aktualisiert.xml')
print("Aktualisierte XML wurde als 'students_aktualisiert.xml' gespeichert.")
