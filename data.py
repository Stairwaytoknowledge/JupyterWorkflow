import os
import pandas as pd
from urllib.request import urlretrieve

URL = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"

def get_fremont_data(filename = "Fremont.csv", url = URL, force_download = False):
    
    """ Download and cache the fremont data
    
    Parameters
    ----------
    
    csv file Fremont.csv
    url URL
    force download 
    
    Returns
    -------
    data : pandas dataframe
    """
    
    
    if force_download or not os.path.exists(filename):
        urlretrieve(URL, "Fremont.csv")
        
    data = pd.read_csv("Fremont.csv", index_col = "Date", parse_dates = True)
    data.columns = ["Total", "East", "West"]
    return data
