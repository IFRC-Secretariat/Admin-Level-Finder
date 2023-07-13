"""
Module to find the admin levels of coordinate points specified by latitude and longitude.
Find admin levels from GADM data.
"""
from shapely.geometry import Point
from admin_levels_finder.gadm_datasets import GADMDatasets


class AdminLevelsFinder:
    """
    Find admin levels of points based on coordinates.
    Currently this can only do one country and CRS at a time.
    """
    def __init__(self, iso3, crs):
        """
        Parameters
        ----------
        iso3 : string (required)
            ISO3 of the country which the point is in.

        crs : string (required)
            The coordinate reference system that the coordinates will be provided in, e.g. the CRS of Google Maps is 'EPSG:4326'.
        """
        # Get the GADM data in the provided CRS
        self.iso3 = iso3
        self.admin_data = GADMDatasets()\
                          .get_admin2_data(iso3=iso3)\
                          .to_crs(crs)


    def find(self, *args, errors='ignore'):
        """
        Parameters
        ----------
        args : sequence or array-like
            The coordinates of the point to find admin levels for.
            The coordinates can either be passed as a single parameter, or as individual float values using multiple parameters:
                - 1 parameter: a sequence or array-like of with 2 or 3 values.
                - 2 or 3 parameters (float): x, y, and possibly z.

        errors : string (default='ignore)
            If the point is not found, raise an error if errors='raise'.
        """
        # Check which polygon the coordinate is in
        point = Point(args)
        for idx, row in self.admin_data.iterrows():
            polygon = row['geometry']
            if polygon.covers(point):
                return row
            
        # Raise an error if required
        if errors=='raise':
            raise ValueError(f'Point {args} not found in GADM admin levels data for {self.iso3}.')