import json


def deserialize(path):
    try:
        with open(path, 'r') as fp:
            data = json.load(fp)
        return data
    except FileNotFoundError:
        print("Не найден файл: " + path)



def serialize(data, path):
    try:
        with open(path, "w") as write_file:
            json.dump(data, write_file, indent=4)
    except FileNotFoundError:
        print("Не найден файл: " + path)
    # write_file.close()
