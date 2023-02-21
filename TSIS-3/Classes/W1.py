class StringOps:
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input( "Enter a string: " )

    def printString(self):
        print(self.str.upper())

strings = StringOps()
strings.getString()
strings.printString()