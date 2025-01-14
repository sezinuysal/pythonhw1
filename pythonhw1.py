import math

points = []

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


distances = []
if len(points) > 1:
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclideanDistance(points[i], points[j])
            distances.append(distance)


if distances:
    min_distance = min(distances)
    print("Minimum Euclidean distance:", min_distance)
else:
    print("The list of points is empty or contains fewer than two points.")
