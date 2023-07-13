"""
Find the admin details of a point.
"""
import admin_levels_finder

# Specify the point details: the country it's in, the coordinates, and the CRS that the coordinates are in
iso3 = "AFG"
coords = (65.006258, 32.705184)
crs = "EPSG:4326"

# Set up the finder with the given ISO3 and CRS
finder = admin_levels_finder.AdminLevelsFinder(
    iso3=iso3, 
    crs=crs,
)

# Get the details of the point
results = finder.find(
    coords, 
    errors='raise'
)

# Print the country, admin1, and admin2 results
print(f"The point is in country: {results['COUNTRY']}.")
print(f"The point is in admin 1: {results['NAME_1']}.")
print(f"The point is in admin 2: {results['NAME_2']}.")