# Create a polygon buffer with shapely

from shapely import wkt, geometry
import matplotlib.pyplot as plt
import pprint

wktPoly = "POLYGON((0 0, 4 0, 4 4, 0 4, 0 0))"
poly = wkt.loads(wktPoly)
pprint.pprint(poly.wkt)
print(poly.area)
#x1,y1=zip(*poly.boundary.coords[:])
x1,y1=poly.boundary.xy
plt.plot(x1,y1)

buf = poly.buffer(5.0)
pprint.pprint(buf.wkt)
print(buf.area)
x2,y2=zip(*buf.boundary.coords[:])

plt.plot(x2,y2)
plt.show()

