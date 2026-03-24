# Accept the radius of a circle and display its area and circumference. 

radius = float(input("Enter the radius of the circle: "))
pi= 3.14
area = pi * radius ** 2
circumference = 2 * pi * radius
print(f"Area of the circle: {area}")
print(f"Circumference of the circle: {circumference}")