#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from osgeo import ogr
import os

def Ex3_1():
    # select features by attribute
    shpfile = './data/counties.shp'
    ds = ogr.Open(shpfile)

    layer = ds.GetLayer(0)
    print("feature count : {}".format(layer.GetFeatureCount()))

    layer.SetAttributeFilter("AREA > 10000")
    print("selected count : {}".format(layer.GetFeatureCount()))

    driver = ogr.GetDriverByName("ESRI Shapefile")
    extfile = './data/counties_filter_attr.shp'

    if os.access(extfile, os.F_OK):
        driver.DeleteDataSource(extfile)

    newds = driver.CreateDataSource(extfile)
    lyrn = newds.CreateLayer('counties_filter_attr', None, ogr.wkbPolygon)
    
    feat = layer.GetNextFeature()
    while feat is not None:
        lyrn.CreateFeature(feat)
        feat = layer.GetNextFeature()
    newds.Destroy()


if __name__ == '__main__':
     Ex3_1()
