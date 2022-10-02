import xml.etree.ElementTree as ET
from model.Book import Book


@staticmethod
def XMLserialization(data):
    root = ET.Element("books")
    bookName = ET.SubElement(root, "id-"+str(data.serial_number))
    bName = ET.SubElement(bookName, "Name")
    bName.text = data.name
    bPrice = ET.SubElement(bookName, "Price")
    bPrice.text = str(data.price)

    s = ET.tostring(root, encoding="utf-8", method="xml")
    s = s.decode("UTF-8")
    with open(f"{data.name}.xml", "w") as wf:
        wf.write(s)


@staticmethod
def XMLdeserialization(path):
    l = []
    tree = ET.parse(path)
    root = tree.getroot()
    for el in root:
        l.append(Book(int(el.tag.split("-")[1]), el[0].text, int(el[1].text)))
    return l
