class Rectangle:
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width

    def __iter__(self):
        return iter([{'length': self.length}, {'width': self.width}])

#Usage
rect = Rectangle(5, 3)
for item in rect:
    print(item)