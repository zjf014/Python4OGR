import geopandas
import matplotlib.pyplot as plt
import matplotlib.colors as colors

gdf = geopandas.GeoDataFrame
census = gdf.from_file("./data/road_depth.shp")
# print(census.to_json())

cmap = colors.ListedColormap(['blue', 'yellow', 'red'])
# print(cmap)

census.plot(figsize=(13.79, 8.85),
            column="id",
            cmap=cmap,
            scheme='UserDefined',
            classification_kwds={
                'bins': [9, 199]
            })
plt.axis('off')

# plt.savefig('Figure.png', transparent=True)
plt.show()
