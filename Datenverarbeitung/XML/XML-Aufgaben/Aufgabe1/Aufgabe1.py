import os
import xml.etree.ElementTree as ET

source = os.path.join(os.path.dirname(__file__), 'books.xml')

XMLcontent = ET.parse(source)
root = XMLcontent.getroot()

for i, book in enumerate(root.findall('book')):
    title = book.find('title').text
    print("Title:", title)

    if i == 0:
        year = book.find('year')
        year.text = "2022"
        print("Year of the first book changed to:", year.text)

XMLcontent.write(source)