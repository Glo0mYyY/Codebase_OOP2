import xml.etree.ElementTree as ET

# XML-Datei öffnen
tree = ET.parse('students.xml')
root = tree.getroot()

# Namen und Noten aller Studenten ausgeben
for student in root.iter('student'):
    name = student.find('name').text
    grade = student.find('grade').text
    print(f"Name: {name}, Grade: {grade}")

# Alter des letzten Studenten erhöhen
last_student = root[-1]
age_element = last_student.find('age')
age = int(age_element.text)
age += 1
age_element.text = str(age)

# XML-Datei speichern
tree.write('students.xml')
