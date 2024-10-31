import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "name": ["Tanmoy", "Subhajit", "Milan", "Tanmoy"],
        "passion": ["B.Tech", np.nan, "Architech", "CSE"],
        "like": ["job", pd.NaT, pd.NaT, "job"],
        "earning": [np.nan, pd.NaT, np.nan, pd.NaT],
    }
)
# in pandas pd.NaT and in numpy np.nan both return value similar to None
print(df)

df = df.dropna(how="all", axis=1)  # delete this column which all value is None
# print(df)

# df = df.drop_duplicates(subset=["name"])
# delete this row which have duplicate value in "name" column

df = df.drop_duplicates(subset=["name"], keep="last")
# keep = "first"(by default) / "last" / False(if duplicate is found it drop all for those rows)
print(df)

# print(df.dropna())  # it return this row which all values are not None

print("\n\n>>>\n")
# print(df.shape)  # it return (number of row, number of column)
# print(df.info())

print(df["passion"].value_counts(dropna=False))
# in "passion" column it count how much number of values is present and dropna=False is help to count None value as well

print(df.isnull())  # for None value it show true other wise show False
print(df.notnull())  # for None value it show Fase other wise show True
