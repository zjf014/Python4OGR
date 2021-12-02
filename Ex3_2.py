#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from osgeo import ogr

def create_shp_by_layer(shp, layer):
    outputfile = shp
    driver = ogr.GetDriverByName("ESRI Shapefile")
    
    if os.access(outputfile, os.F_OK):
        driver.DeleteDataSource(outputfile)
    
    newds = driver.CreateDataSource ( outputfile )
    pt_layer = newds.CopyLayer ( layer, '')
    newds.Destroy ()

def Ex3_2():
    # select features by location
    shp = './data/counties.shp'
    
    driver = ogr.GetDriverByName("ESRI Shapefile")    
    ds = ogr.Open(shp)
    
    layer = ds.GetLayer(0)
    print("feature count : {}".format(layer.GetFeatureCount()))

    cover_shp = './data/dalian.shp'
    cover_ds = ogr.Open(cover_shp)
    cover_layer = cover_ds.GetLayer(0)
    cover_feats = cover_layer.GetNextFeature()
    poly = cover_feats.GetGeometryRef()
    layer.SetSpatialFilter(poly)
    print("feature count : {}".format(layer.GetFeatureCount()))

    out_shp = './data/dalian_cover.shp'
    create_shp_by_layer(out_shp, layer)

if __name__ == '__main__':
    Ex3_2()
