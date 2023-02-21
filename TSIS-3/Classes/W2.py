class Square():
    def __init__(self, length):
        self.lengths = int(length)

    def area(self):
        return self.lengths * self.lengths

square = Square(input())
print("Area of the square:", square.area())