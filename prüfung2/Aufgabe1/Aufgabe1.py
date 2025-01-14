import os
import xml.etree.ElementTree as ET

source = os.path.join(os.path.dirname(__file__), 'book.xml')

XMLcontent = ET.parse(source)
root = XMLcontent.getroot()

ageLimit = 80

for i, book in enumerate(root.findall('book')):
    title = book.find('title').text
    author = book.find('author').text
    age = book.find('age').text
    ageInt = int(age)

    if ageInt >= ageLimit:
        print(f"Book", title, "'s author is older than ", ageLimit, " years")

XMLcontent.write(source)
