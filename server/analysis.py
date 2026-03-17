import geopandas as gpd 
from sqlalchemy import create_engine 

host = "localhost" 
port = "5433" 
dbname = "gme221_lab4" 
user = "postgres" 
password = "sangyan" 

conn_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}" 

engine = create_engine(conn_str) 

sql_query = """ 
SELECT gid, ass_ass_va, ass_market, geom 
FROM public.assessed_parcels; 
""" 

gdf = gpd.read_postgis(sql_query, engine, geom_col="geom") 

#print(gdf.head()) 
#print("CRS:", gdf.crs) 

## SPATIAL WEIGHTS
from spatial_weights import contiguity_weights, knn_weights, distance_weights 
#Place this import at the top of your file with the other imports 

w = distance_weights(gdf) 

print("Neighbors:", w.neighbors) 

from spatial_weights import contiguity_weights, knn_weights, distance_weights 
#Place this import at the top of your file with the other imports 

w = knn_weights(gdf) 

print("Neighbors:", w.neighbors) 

from spatial_weights import contiguity_weights, knn_weights, distance_weights 
#Place this import at the top of your file with the other imports 

w = contiguity_weights(gdf) 

print("Neighbors:", w.neighbors)