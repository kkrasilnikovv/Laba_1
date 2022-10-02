import json


def deserialize():
    with open("data.json", 'r') as fp:
        data = json.load(fp)
    return data


def serialize(data):
    with open("data.json", "w") as write_file:
        json.dump(data, write_file, indent=4)
    #write_file.close()
