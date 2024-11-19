#Grösstenteils mit ChatGPT gelöst

import os
import xml.etree.ElementTree as ET

# Define the path to the XML file
source = os.path.join(os.path.dirname(__file__), 'books.xml')

# Parse the XML content
XMLcontent = ET.parse(source)
root = XMLcontent.getroot()

# Print the titles of all books and change the year of the first book
for i, book in enumerate(root.findall('book')):
    # Find the title element within each book and print its text
    title = book.find('title').text
    print("Title:", title)

    # If it's the first book, change its year
    if i == 0:
        year = book.find('year')
        year.text = "2022"  # Set the new year value
        print("Year of the first book changed to:", year.text)

# Save the changes back to the XML file
XMLcontent.write(source)
