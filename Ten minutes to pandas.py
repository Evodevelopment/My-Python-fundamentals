import numpy as np

import pandas as pd

#Creating a Series by passing a list of values, letting pandas create a default integer index:
s = pd.Series([1, 3, 5, np.nan, 6, 8])

#Creating a DataFrame by passing a NumPy array, with a datetime index using date_range() and labeled columns:
dates = pd.date_range("20130101", periods=6)


