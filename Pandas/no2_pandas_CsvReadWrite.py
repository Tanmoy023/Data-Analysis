import pandas as pd
import numpy as np

my_csv = pd.read_csv("my_csv.csv")
# print(my_csv)
# print(my_csv["Speed"])
# print(my_csv["Speed"][0])

# my_csv["Speed"][0] = 55  # temporaty change to value
# print(my_csv)
# my_csv.to_csv("my_csv.csv")  # save all changes in 'my_csv.csv'

my_csv.index = ["First", "Second", "Third", "Fourth"]
print(my_csv)
