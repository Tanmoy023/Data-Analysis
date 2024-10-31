# pip install --upgrade pandas
# pip install jupyter
# jupyter notebook
import pandas as pd
import numpy as np

dict1 = {
    "Name": ["Tanmoy", "Sunhajit", "Sankha", "kanaiDa"],
    "Roll": [53, 54, 80, 50],
    "Address": ["Nabin MaheshPur", "TrilochanPur", "Nandigram", "Trilochanpur"],
}

df = pd.DataFrame(dict1)
print(df)

df.to_csv("Friends.csv")
# df.to_csv("Friends_FalseIndex.csv", index=False)

# print(df.head(2))
# print(df.tail(2))
# print(df.describe())
