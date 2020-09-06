class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self, height, radius):
        self.height = height
        self.radius = radius
        return self.pi * radius**2 * height
