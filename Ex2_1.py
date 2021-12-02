#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from osgeo import ogr

def Ex2_1():
     driver=ogr.GetDriverByName('ESRI Shapefile')
     ds =driver.CreateDataSource('./data/xx_test.shp')
     # create point layer
     layer=ds.CreateLayer('test',geom_type=ogr.wkbPoint)

     # add field
     fieldDefn = ogr.FieldDefn('id',ogr.OFTString)
     fieldDefn.SetWidth(4)
     layer.CreateField(fieldDefn)

     # create feature
     featureDefn = layer.GetLayerDefn()
     feature = ogr.Feature(featureDefn)
     # set feature's geometry
     point = ogr.Geometry(ogr.wkbPoint)
     point.SetPoint(0,121.2241,38.9703)
     feature.SetGeometry(point)
     # set feature's field value
     feature.SetField('id', 23)

     # add feature to layer
     layer.CreateFeature(feature)
     
     ds.Destroy()


if __name__ == '__main__':
     Ex2_1()
