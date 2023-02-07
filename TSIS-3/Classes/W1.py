class StringOps:
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input("Enter a string: ")

    def printString(self):
        print(self.str.upper())

string_ops = StringOps()
string_ops.getString()
string_ops.printString()