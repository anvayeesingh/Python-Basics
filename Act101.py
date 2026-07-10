import math

class Circle:
    def __init__(self, radius):
        """Initializes the circle with a given radius."""
        self.radius = radius

    def compute_area(self):
        """Computes and returns the area of the circle (π * r^2)."""
        return math.pi * (self.radius ** 2)

    def compute_perimeter(self):
        """Computes and returns the perimeter/circumference of the circle (2 * π * r)."""
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    my_circle = Circle(5)

    print(f"Radius: {my_circle.radius}")
    print(f"Area: {my_circle.compute_area():.2f}")
    print(f"Perimeter: {my_circle.compute_perimeter():.2f}")
