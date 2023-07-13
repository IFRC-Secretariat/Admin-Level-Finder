import pyproj
from shapely.geometry import Point
from shapely.ops import transform
import unittest
import admin_levels_finder


class TestFindPoint(unittest.TestCase):
    """
    Test finding some points and checking that the correct admin1 and admin2 names are returned.
    """
    def setUp(self):
        self.points = [
            {
                "iso3": "GBR",
                "crs": 'EPSG:4326',
                "coords": (-3.272104, 51.083221),
                "transform_crs": 'EPSG:32642',
                "admin1": "England",
                "admin2": "Somerset"
            },
        ]


    def test_find_point(self):
        """
        Test finding the results for a point in the UK.
        """
        for point in self.points:
            finder = admin_levels_finder.AdminLevelsFinder(iso3=point['iso3'], crs=point['crs'])
            results = finder.find(point['coords'], errors='raise')
            self.assertEqual(results["NAME_1"], point['admin1'])
            self.assertEqual(results["NAME_2"], point['admin2'])


    def test_convert_crs_point(self):
        """
        Test finding a point in a different CRS.
        """
        for point in self.points:
            # Convert the point to a different CRS
            transformer = pyproj.Transformer.from_crs(pyproj.CRS(point['crs']), 
                                                      pyproj.CRS(point['transform_crs']), 
                                                      always_xy=True).transform
            point_transformed = transform(transformer, Point(point['coords']))
            finder = admin_levels_finder.AdminLevelsFinder(iso3=point['iso3'], crs=point['transform_crs'])
            results = finder.find(list(point_transformed.coords), errors='raise')

            # Check the results
            self.assertEqual(results["NAME_1"], point['admin1'])
            self.assertEqual(results["NAME_2"], point['admin2'])