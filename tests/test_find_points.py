import unittest
import admin_levels_finder


class TestFindPoints(unittest.TestCase):
    """
    Test finding some points and checking that the correct admin1 and admin2 names are returned.
    """
    def test_point_1(self):
        """
        Test finding the results for a point in the UK.
        """
        uk_finder = admin_levels_finder.AdminLevelsFinder(iso3='GBR', crs='EPSG:4326')
        results = uk_finder.find(-3.272104, 51.083221)
        self.assertEqual(results["NAME_1"], "England")
        self.assertEqual(results["NAME_2"], "Somerset")