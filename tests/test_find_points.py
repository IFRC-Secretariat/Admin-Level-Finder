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
        self.iso3 = 'GBR'
        self.crs = 'EPSG:4326'
        self.point_4326 = (-3.272104, 51.083221)
        self.utm_crs = 'EPSG:32642'
        self.admin1 = "England"
        self.admin2 = "Somerset"


    def test_find_point(self):
        """
        Test finding the results for a point in the UK.
        """
        uk_finder = admin_levels_finder.AdminLevelsFinder(iso3=self.iso3, crs=self.crs)
        results = uk_finder.find(self.point_4326, errors='raise')
        self.assertEqual(results["NAME_1"], self.admin1)
        self.assertEqual(results["NAME_2"], self.admin2)


    def test_convert_crs_point(self):
        """
        Test finding a point in a different CRS.
        """
        # Convert the point to the UTM CRS
        transformer = pyproj.Transformer.from_crs(pyproj.CRS(self.crs), 
                                                  pyproj.CRS(self.utm_crs), 
                                                  always_xy=True).transform
        point_utm = transform(transformer, Point(self.point_4326))
        utm_finder = admin_levels_finder.AdminLevelsFinder(iso3=self.iso3, crs=self.utm_crs)
        results = utm_finder.find(list(point_utm.coords), errors='raise')

        # Check the results
        self.assertEqual(results["NAME_1"], self.admin1)
        self.assertEqual(results["NAME_2"], self.admin2)