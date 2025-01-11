class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        return self.width * self.height


    def perimeter(self):
        return 2 * (self.width + self.height)


    def draw(self):
        print('*' * self.width)

        for _ in range(self.height - 2):
            print('*' + ' ' * (self.width - 2) + '*')

        if self.height > 1:
            print('*' * self.width)


result = Rectangle(10, 10)
print(result.draw())

