import geopy
import geopy.distance
import math


# Haversine formula
def get_rectangle_bounds(coordinates):
    start = geopy.Point(coordinates)
    hypotenuse = math.hypot(width / 1000, length / 1000)

    # Convert radians to degrees, use math builtin function
    northeast_angle = 0 - math.degrees(math.atan(width / length))
    southwest_angle = 180 - math.degrees(math.atan(width / length))

    d = geopy.distance.distance(kilometers=hypotenuse / 2)
    northeast = d.destination(point=start, bearing=northeast_angle)
    southwest = d.destination(point=start, bearing=southwest_angle)
    bounds = []
    for point in [northeast, southwest]:
        coords = (point.longitude, point.latitude)
        bounds.append(coords)

    return bounds


length = 1400  # in meters
width = 1400
bearing = 90

if __name__ == '__main__':
    print(get_rectangle_bounds([55.704251748170435, 37.567998629456895]))