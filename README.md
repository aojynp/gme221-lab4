# Laboratory 4
Spatial Statistics: Spatial Autocorrelation and Cluster Detection  
--------------------------------------------------------------------------------
# Overview
The laboratory exercise focuses on computational spatial statistics measuring spatial autocorrelation and detecting clusters within spatial data (parcel). Generally, it flows from geometric reconstruction (spatial weights) to spatial analysis and visualization of spatial values’ trends and/or distribution within the study area. The primary goal is to use Python to identify hotspots and coldspots in parcel valuations by the Global Moran’s I (overall pattern) and Local Moran’s I (local clusters). Spatial features are retrieved directly from a PostGIS database and loaded into Python for high-level processing and cluster detection.

--------------------------------------------------------------------------------
# How to run
(1) Set up data connection to the PostGIS database using sqlalchemy and create_engine to read the data from the restored polygon from the pgAdmin.
(2) Run SQL query to load the assessed_parcels table 
(3) Spatial Weights Configuration by import functions from spatial_weights.py to calculate a spatial weights matrix (w).
(4) Visualized via weights graph of visualize_neighbors to verify the topological network of nodes (centroids) and edges (neighbor connections).
(5) Statistical Computation using Global Moran's I and Local Moran's I to measure overall spatial autocorrelation for attributes like ass_ass_va or ass_market and to compute local statistics for each parcel (p-value threshold: < 0.05), respectively.
(6) Visualization of Cluster Classification through assigning labels to the DataFrame to identify "Hotspots" (High-High), "Coldspots" (Low-Low), or "Not Significant" areas based on the computed local statistics and a p-value threshold.

--------------------------------------------------------------------------------
# Outputs expected
The expected output for this exercise has a concentration on a modularized Python codebase wherein it comprised scripts for spatial weights, Moran’s I computations, and visualization. Consequently, it is also expected to generate critical visual outputs, including spatial connectivity graphs and Local Moran’s I cluster maps that identify statistically significant hotspots and coldspots.

--------------------------------------------------------------------------------
# Milestones and Reflections
