import os
import xml.etree.ElementTree as ET

baum = os.path.join(os.path.dirname(__file__), 'students.xml')

baum_parsed = ET.parse(baum)
wurzel = baum_parsed.getroot()

for student in wurzel.findall('student'):
    name = student.find('name').text
    grade = student.find('grade').text
    print(f"Name: {name}, Grade: {grade}")

letzter_student = wurzel.findall('student')[-1]
alter = int(letzter_student.find('age').text)
letzter_student.find('age').text = str(alter + 1)

baum_parsed.write(baum)
