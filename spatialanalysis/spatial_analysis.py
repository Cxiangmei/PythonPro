#encoding:utf-8

import arcpy

database = ''
if arcpy.Exists(database):
    arcpy.env.workspace = database
    lyrs = arcpy.ListFeatureClasses(feature_type='line')

    for lyr in lyrs:
        cursor = arcpy.da.SearchCursor(lyr,["SHAPE@"])
        if cursor:
            for fea in cursor:
                fea_geo = fea[0]




