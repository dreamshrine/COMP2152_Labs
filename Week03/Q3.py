#Question 3: Coordinate System (Tuples - Creation Unpacking
point1 = (3, 5)
point2 = (7, 2)
print(f"Point 1: {point1}\nPoint 2: {point2}\n")

x1, y1 = point1
x2, y2 = point2
print(f"X1: {x1}, Y1: {y1}\nX2: {x2}, Y2: {y2}\n")

distance = ((x2 - x1)**2 + (y2 - y1)**2)** 0.5
print(f"Distance Between Points: {distance}")

python_tuple = tuple(("P", "Y", "T", "H", "O", "N"))
for x in python_tuple:
    print(x)