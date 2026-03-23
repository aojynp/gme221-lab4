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

1. # Interpreting the Neighborhood Structure

The Nodes (red dots) represents an individual entity or the parcels and its location. The centroids serve as coordinates hence these illustrate the location by calculating the parcel’s center. On the other hand, the greens lines represent a relationship between two nodes or centroids, nearest neighbors. These is computed by determining 4 points (parcels) within a 20-unit distance radius (threshold).
Understanding this conditions on the spatial weights for the neighborhood, I made several modifications. Contiguity-Based Weights relies on the shared boundaries of polygons rather than the distance between them hence, only features that share an edge (a boundary line) become neighbors. On the other hand, the K-Nearest Neighbor (knn)It identifies a fixed number k of neighbors for every single feature, regardless of how far apart they are. I compared the graphs where knn value has the modification. K=10 is more saturated had when k is 4, therefore the higher the knn, the densier the graph due to the connected neighbors. And for distance-based method, every parcel within a specific distance d of the target is considered a neighbor. I modified the threshold from 20 to 100resulting to a dense mesh due to lines reaching the 100-distance neighbors as much as possible.

The Effect of Increasing k on Network Density, the number of "edges" or connections in the graph grows. Changing the density of the network changed the strength and significance of the spatial autocorrelation.
Increasing both and the distance threshold directly impacts the statistical strength of spatial autocorrelation, primarily through a process of spatial smoothing. When the parameters expand, it results to computation of the relationship between a target point and a much larger set of neighbors. In a sparse network with low or a small distance, where a single cluster of similar values produces a high value. However, as the network becomes denser, it incorporates distant data points that are geographically further away and, according to the First Law of Geography, less likely to be related. 

When considering the spatial relationships inherent in a parcel dataset, I believe contiguity weights provide the most reliable source in representing actual neighbor of each parcel. The polygons have fundamentally discrete administrative units that tile a continuous surface hence their primary mode of interaction is through shared or with similar boundaries. In a cadastre, the "neighborhood" is defined by physical and legal measured boundaries (metes and bounds). A change in a parcel extent or value on one lot typically affects the immediate neighboring lots who share a line or a corner point. Contiguity weights naturally respect these irregular geometries without forcing an arbitrary distance decay that might not apply to legal or social boundaries.

In contrast, while K-nearest neighbors (KNN) and distance-based weights have advantages in other spatial contexts, they depend on the scales and set number of neighbors or limited distance for identifying neighbors. KNN forces a uniform number of neighbors for every unit, which is statistically convenient but it might ignore a touching neighbor in a dense urban block while reaching across several kilometers to find a "neighbor" for a large rural tract. Similarly, a fixed distance band creates a "one-size-fits-all" radius that may capture dozens of neighbors in a subdivision but leave a large forest parcel isolated. Therefore, contiguity ensures the model reflects the actual topological connectivity of the of the parcels and also the landscape, where the most intense spatial autocorrelation occurs between those who are literally side-by-side.

Visualizing spatial weights before computing into Moran’s I is essential because Moran’s I is entirely dependent on how we define "neighborhood," so if the weights matrix doesn't accurately reflect the real-world connectivity of the parcel features, the resulting statistic becomes mathematical vision rather than a geographical insight. When the algorithm runs, isolated units are often dropped or treated as having no spatial relationship, which can lead to a significant underestimation of the actual clustering happening on the ground. By mapping the weights, these can ensure that every unit is properly integrated into the network.

If the neighborhood structure is incorrect, it defines too many neighbors like when KNN is too high. There is an error when I input k as 20. This washes out local spatial patterns and can force a result of global spatial randomness even when localized hotspots exist. Conversely, an overly restrictive neighborhood might fail to capture the scale of the spatial process, leading us to miss a significant trend entirely. While doing this part several times, visualizing the polygon first enable to choose the spatial weight method in order to reduce or prevent conceptual misalignments before they propagate through our Moran’s I calculation.


