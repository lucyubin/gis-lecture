!pip install geokakao

import pandas as pd
import geokakao as gk

data = pd.read_csv('*.csv', encoding='euc-kr')
data = data.head(10)

gk.add_coordinates_to_dataframe(data, '주소')
print(data)

data.to_csv('*.csv', index=False, encoding='euc-kr')
