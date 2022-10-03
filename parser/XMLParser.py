import xml.etree.ElementTree as ET
from model.Book import Book


@staticmethod
def XMLserialization(data: dict, path: str):
    root = ET.Element("Books")
    for el in data:
        mId = ET.Element("id-" + str(el["serial_number"]))
        mName = ET.SubElement(mId, "Name")
        mName.text = el["name"]
        mPrice = ET.SubElement(mId, "Price")
        mPrice.text = str(el["price"])
        root.append(mId)

    s = ET.tostring(root, encoding="utf-8", method="xml")
    s = s.decode("UTF-8")
    try:
        with open(path, "w") as wf:
            wf.write(s)
    except FileNotFoundError:
        print("Не найден файл: "+path)


@staticmethod
def XMLdeserialization(path):
    l = []
    tree = ET.parse(path)
    root = tree.getroot()
    for el in root:
        l.append(Book(int(el.tag.split("-")[1]), el[0].text, int(el[1].text)))
    return l
