'''Exercise 1
----------------
Given dataframe 1 and 2, produce dataframe 3.
'''

from numpy.core.numeric import NaN
import pandas as pd

df1 = pd.DataFrame({
    'Date': ['01/01/2021', '02/01/2021', '03/01/2021'],
    'A': [1, 4, 7], 
    'B': [2, 5, 8],
    'C': [3, 6, 9]
    })

df2 = pd.DataFrame({
    'Date': ['03/01/2021', '04/01/2021', '05/01/2021'],
    'C': [4, 6, 8], 
    'D': [5, 7, 9]
    })

df3 = pd.DataFrame({
    'Date': ['01/01/2021', '02/01/2021', '03/01/2021', '04/01/2021', ''],
    'A': [1, 4, 7, NaN, NaN],
    'B': [2, 5, 8, NaN, NaN],
    'C': [3, 6, 4, 6, 8],
    'D': [NaN, NaN, 5, 7, 9]
    })

actual = pd.concat([df1, df2])
expected = df3
print(f"actual = {actual}")




