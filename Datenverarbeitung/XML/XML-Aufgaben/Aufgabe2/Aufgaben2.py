import os
import xml.etree.ElementTree as ET

# Define the path to the XML file
baum = os.path.join(os.path.dirname(__file__), 'students.xml')


# XML-Datei parsen
baum_parsed = ET.parse(baum)
wurzel = baum_parsed.getroot()

# Namen und Noten der Studenten ausgeben
for student in wurzel.findall('student'):
    name = student.find('name').text
    grade = student.find('grade').text
    print(f"Name: {name}, Grade: {grade}")

# Alter des letzten Studenten um eins erhöhen
letzter_student = wurzel.findall('student')[-1]
alter = int(letzter_student.find('age').text)
letzter_student.find('age').text = str(alter + 1)

# Die Änderung zurück in die XML-Datei schreiben
baum_parsed.write(baum)
