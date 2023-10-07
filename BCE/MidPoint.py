import matplotlib.pyplot as plt

def draw_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy / dx if dx != 0 else None  # Avoid division by zero

    # Determine the octant
    if slope is None or slope > 1:
        steep = True
    else:
        steep = False

    if steep:
        x1, y1 = y1, x1  # Swap x1 and y1
        x2, y2 = y2, x2  # Swap x2 and y2

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    y = y1

    x_coordinates = []
    y_coordinates = []

    for x in range(x1, x2 + 1):
        if steep:
            x_coordinates.append(y)
            y_coordinates.append(x)
        else:
            x_coordinates.append(x)
            y_coordinates.append(y)

        if d > 0:
            y += 1 if y2 > y1 else -1
            d -= 2 * dx

        d += 2 * dy

    return x_coordinates, y_coordinates

# Input coordinates
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# Generate line coordinates
x_coords, y_coords = draw_line(x1, y1, x2, y2)

# Plot the line
plt.plot(x_coords, y_coords, marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.grid(True)
plt.show()
