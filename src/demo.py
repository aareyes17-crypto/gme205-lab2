#from spatial import Point

#p = Point("A", 121.0, 14.6)
#print(p.id, p.lon, p.lat)
#print(p.to_tuple())

#a = Point("B", 122.0, 15.6)
#print(p.distance_to(a))

#q = Point("X", 999, 14)
#print(q.id, q.lon, q.lat)

from spatial import PointSet

def main():
    points = PointSet.from_csv("data/points.csv")

    print("Point count:", points.count())
    print("Bounding box:", points.bbox())

    tagged_points = points.filter_by_tag("poi")
    print("poi points:", tagged_points.count())

if __name__ == "__main__":
    main()
