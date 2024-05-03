class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'

p1 = Ponto(1,2)
p2 = Ponto(345, 352)
print(p1)
print(p2)

