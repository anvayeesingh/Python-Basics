import math

def calculate_circumference(radius):
    """
    Calculates the circumference of a circle given its radius.
    """
    return 2 * math.pi * radius

r = float(input("Enter the radius of the circle: "))
circumference = calculate_circumference(r)

print(f"The circumference of the circle is: {circumference:.2f}")
