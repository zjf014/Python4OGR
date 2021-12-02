# Attribute selection for subset using fiona

import fiona

with fiona.open("./data/MS_UrbanAnC10.shp") as sf:
    filtered = filter(lambda f: f['properties']['POP'] < 5000, sf)
    drv = sf.driver
    crs = sf.crs
    schm = sf.schema
    subset = "./data/MS_Urban_Fiona_Subset.shp"
    with fiona.open(subset, "w",driver=drv,crs=crs,schema=schm) as w:
        for rec in filtered:
            w.write(rec)


