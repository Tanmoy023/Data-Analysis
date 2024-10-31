import pandas as pd
import numpy as np

# pip install xlrd

data = pd.read_excel("data.xlsx")
data = pd.read_excel("data.xlsx", sheet_name="person")
print(data)
