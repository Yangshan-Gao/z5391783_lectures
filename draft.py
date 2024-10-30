import pandas as pd
import numpy as np


|            | AUD/USD | EUR/AUD |
|------------+---------+---------|
| 2020-09-08 | 0.7280  | 1.6232  |
| 2020-09-09 | 0.7209  | 1.6321  |
| 2020-09-10 | NaN     | 1.6221  |
| 2020-09-11 | 0.7263  | 1.6282  |
| 2020-09-14 | 0.7281  | NaN     |
| 2020-09-15 | 0.7285  | 1.6288  |

<class 'pandas.core.frame.DataFrame'>
Index: 6 entries, 2020-09-08 to 2020-09-15
Data columns (total 2 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   AUD/USD  5 non-null      float64
 1   EUR/AUD  5 non-null      float64
dtypes: float64(2)

df.loc['a':'z']

