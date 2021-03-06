#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from osgeo import ogr

def Ex2_2():
    # create point
    print("1. create point ...")
    point = ogr.Geometry(ogr.wkbPoint)
    point.AddPoint(10,20)
    print(point)
    # create line
    print("2. create line ...")
    line = ogr.Geometry(ogr.wkbLineString)
    line.AddPoint(10,10)
    line.AddPoint(20,20)
    print (line)
    # alter line
    print("3. alter line ...")
    line.SetPoint(0,1,2)
    print (line)
    print (line.GetPointCount())
    print (line.GetX(0),line.GetY(0))
    # create circle
    print("4. create circle ...")
    ring = ogr.Geometry(ogr.wkbLinearRing)
    ring.AddPoint(0,0)
    ring.AddPoint(100,0)
    ring.AddPoint(100,100)
    ring.AddPoint(0,100)
    ring.CloseRings()
    print(ring)
    # create ring
    print("5. create ring ...")
    outring = ogr.Geometry(ogr.wkbLinearRing)
    outring.AddPoint(0,0)
    outring.AddPoint(100,0)
    outring.AddPoint(100,100)
    outring.AddPoint(0,100)
    outring.AddPoint(0,0)

    inring = ogr.Geometry(ogr.wkbLinearRing)
    inring.AddPoint(25,25)
    inring.AddPoint(75,25)
    inring.AddPoint(75,75)
    inring.AddPoint(25,75)
    inring.CloseRings()

    polygon = ogr.Geometry(ogr.wkbPolygon)
    polygon.AddGeometry(outring)
    polygon.AddGeometry(inring)
    print(polygon)
    print(polygon.GetGeometryCount())

    outring2 = polygon.GetGeometryRef(0)
    inring2 = polygon.GetGeometryRef(1)
    print(outring2)
    print(inring2)
    # create multi point
    print("6. create multi point ...")
    multipoint = ogr.Geometry(ogr.wkbMultiPoint)
    point = ogr.Geometry(ogr.wkbPoint)
    point.AddPoint(10,10)
    multipoint.AddGeometry(point)
    point.AddPoint(20,20)
    multipoint.AddGeometry(point)
    print(multipoint)

if __name__ == '__main__':
     Ex2_2()
