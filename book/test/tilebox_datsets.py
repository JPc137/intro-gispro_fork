from tilebox.datasets import Client
from shapely.geometry import box

# Initialize the Tilebox datasets client
client = Client()
sentinel_2 = client.dataset("open_data.copernicus.sentinel2_msi")
sentinel_2a = sentinel_2.collection("S2A_S2MSI2A")

# Define a rectangular area over Ireland
area = box(-10.68234795, 51.36473433, -5.34679566, 55.44704815)

# Query for Sentinel-2 granules within the specified temporal and spatial extent
granules = sentinel_2a.query(
    temporal_extent=("2025-03-01", "2025-06-01"),
    spatial_extent=area
)

print(f"Located {granules.sizes['time']} Sentinel-2 granules.")