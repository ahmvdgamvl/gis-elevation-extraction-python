import geopandas as gpd
import rasterio

# قراءة الملفات 

stations = gpd.read_file('stations.shp')
with rasterio.open('DEM.tif') as src:
    coords =[ [geom.x, geom.y] for geom in stations.geometry] #استخراج 
    stations['elevation'] = [x[0] for x in src.sample(coords)] # الارتفاع 
    
# تصفية الأعمدة

elevations = stations[['name', 'elevation']]

elevations.plot()
# حفظ الجدول في Exel
elevations.to_csv('topographic_elevations.csv', index=False)

# ومرة تاني ك ملف مكاني شيبفايل
stations.to_file('stations_with_elevation.shp', driver='ESRI Shapefile')

