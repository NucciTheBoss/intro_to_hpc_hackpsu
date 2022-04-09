#!/usr/bin/env python3
import datetime
import os
import time

import dask
import dask.dataframe as dd


if not os.path.exists('data'):
    os.mkdir('data')

def name(i):
    """Provide date for filename given index"""
    return str(datetime.date(2000, 1, 1) + i * datetime.timedelta(days=1))

df = dask.datasets.timeseries()
df.to_csv('data/*.csv', name_function=name)

start = time.time()

end = time.time()

print(f"Time to completion: {end - start}")
