from spatial import Point

p = Point("A", 121.0, 14.6)
print(p.id, p.lon, p.lat)
print(p.to_tuple())

a = Point("B", 122.0, 15.6)
print(p.distance_to(a))

q = Point("X", 999, 14)
print(q.id, q.lon, q.lat)
