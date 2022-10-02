class User:
    def __init__(self, serial_number, name: str, book=[]):
        self.serial_number = serial_number
        self.name = name
        self.book = book
