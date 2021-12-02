#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from osgeo import ogr  # import ogr libs

def Ex1_1():
    drv_count = ogr.GetDriverCount()
    print(drv_count)  # support 82 data formats

def Ex1_2():
    # read .shp file
    inshp = './data/roadtrl020.shp'    
    driver = ogr.GetDriverByName('ESRI Shapefile')
    datasource = driver.Open(inshp, update=0)
    if datasource:
        print('done')
    else:
        print('could not open')
    # print(dir(datasource))

    return datasource


def Ex1_2_2():
    # direct open .shp file
    inshp = './data/roadtrl020.shp'    
    ds = ogr.Open(inshp)
    
    driver = ds.GetDriver()
    print(driver.name)
    print(dir(ds))


def Ex1_3():

    datasource = Ex1_2()
  
    layer = datasource.GetLayer(0) # get layers
    # print(dir(layer))
    print("feature count : {0}".format(layer.GetFeatureCount()))
    print("layer extent : {0}".format(layer.GetExtent()))
    print("layer spatial : {0}".format(layer.GetSpatialRef()))
    
    
    layerdef = layer.GetLayerDefn()  # fields
    for i in range(layerdef.GetFieldCount()):
        defn = layerdef.GetFieldDefn(i)
        print(defn.GetName(),defn.GetWidth(),defn.GetType(),defn.GetPrecision())

    layer.ResetReading()  # traverse features
    feature = layer.GetNextFeature()
    while feature:
        feature = layer.GetNextFeature()
    # dir(feature)
    
    # layer.ResetReading()
    feat=layer.GetFeature(0)  # get 1st feature
    
    print("LENGTH : {}".format(feat.GetField('length'))) # get field value
    for i in range(feat.GetFieldCount()):
         print("{} : {}".format(feat.keys()[i],feat.GetField(i)))
         
    geom = feat.GetGeometryRef()  # get geometry
    print("geometry name : {}".format(geom.GetGeometryName()))
    print("point count : {}".format(geom.GetPointCount()))
    # print("spatial reference : {}".format(geom.GetSpatialReference()))
    print("wkt : {}".format(geom.ExportToWkt()))
    print("X : {}".format(geom.GetX(0)))
    print("Y : {}".format(geom.GetY(0)))
    print("Z : {}".format(geom.GetZ(0)))
    
    # arc0 = geom.GetGeometryRef(0)
    # arc0.GetGeometryName()
    # arc0.GetGeometryCount()
    # arc0.GetPointCount()
    # arc0.GetX(0)
    # arc0.GetY(0)
    # arc0.GetZ(0)
    # arc0.ExportToWkt()

    # bl = geom.Intersect(other)  /Overlaps/Contains/Within/Crosses/Disjoint
    # point = geom.Centroid()

    datasource.Destroy()


if __name__ == '__main__':
    #Ex1_1()
    #Ex1_2()
    #Ex1_2_2()
    Ex1_3()
