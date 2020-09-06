class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self, height, radius):
        return self.pi * radius**2 * height

    def surface_area(self, height, radius):
        return (2 * self.pi * radius * height) + (2 * self.pi * radius ** 2)
