#Day021 - How to get the data and break larger data into chunks
"""
Download the zip file data(14Gb):
http://deepyeti.ucsd.edu/jianmo/amazon/categoryFiles/Clothing_Shoes_and_Jewelry.json.gz
"""
import pandas as pd
dir(pd)
help(pd.read_json)

"""
chunking:
    dividing large data into chunks.
    14Gb of large data can't be run in one go with 8Gb RAM device,
    so we can diide it into different parts by chunking.
    E.g.  32292000 (32.2 Million)
    ('filename',chunksize = 1000000)
    total - 32 divisions for 32 Million and last division for 0.2 Million.
    so, total 33 chunks.
"""










