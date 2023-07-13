"""
Module to get GADM data as Geopandas GeoDataFrames.
"""
import functools
import geopandas as gpd


class GADMDatasets:
    """
    Get GADM admin 0, 1, and 2 datasets as geopandas GeoDataFrames.
    """
    def get_admin1_data(self, iso3):
        """
        Get GADM admin 1 data.

        Parameters
        ----------
        iso3 : string (required)
            The ISO3 of the country to get data for.
        """
        return self.get_gadm_country_data(iso3=iso3, admin_level=1)
    

    def get_admin2_data(self, iso3):
        """
        Get GADM admin 1 data.

        Parameters
        ----------
        iso3 : string (required)
            The ISO3 of the country to get data for.
        """
        return self.get_gadm_country_data(iso3=iso3, admin_level=2)


    def get_gadm_country_data(self, iso3, admin_level):
        """
        Get country data/ admin 1 data/ admin 2 data from GADM and return as a Geopandas GeoDataFrame.
        """
        # Get the download URL
        iso3 = iso3.strip().upper()
        admin_level = str(admin_level).strip()
        url = f'https://geodata.ucdavis.edu/gadm/gadm4.1/json/gadm41_{iso3}_{admin_level}.json.zip'

        # Download the data
        data = gpd.read_file(url)

        return data