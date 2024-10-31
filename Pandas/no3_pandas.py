import pandas as pd
import numpy as np

# ser = pd.Series(np.random.rand(30))
# print(type(ser))
# print(ser)

newDF = pd.DataFrame(np.random.rand(250, 5), index=np.arange(250))
print(type(newDF))
# print(newDF)

# print(newDF.index)
# print(newDF.columns)
# print(newDF.T)

# print(newDF.head()) # print first 5 row's of this dataframe
# print(newDF.describe())
# print(newDF.dtypes)  # print datatype of each column
# print(newDF[0])  # print newDF 0'th column
# print(type(newDF[0]))  # it's a series

newDF[0][0] = "Tanmoy"
# after changing a value of into different datatype-value, this column type become 'object
# print(newDF.head())
# print(newDF.dtypes)

# npDF = newDF.to_numpy()
# print(npDF)

order = newDF.sort_index(axis=0, ascending=False)
# axis=0 is for columns and axis=1 is for rows
print(order.head())

newDF_view = newDF  # newDF_view is a view of newDF. If i change any element of newDF_view it also reflect in newDF
newDF_view[0][0] = 1.010101
print(newDF.head())

newDF_copy = (
    newDF.copy()
)  # now newDF_copy is a seperate copy of newDF. means any changes dose't reflect in newDf
# newDF_copy[0][0] = 100.111000
# print(newDF_copy)

# print(newDF)
newDF.loc[2, 0] = (
    11.001100  # it is the right way to change the value in DataFrame. [2,0] means in 2'nd row and 0'th column
)
# print(newDF.head())

newDF.columns = list("ABCDE")
# print(newDF.head())

# newDF[1][0] # it show's some error, because new[1][0] is become newDF["B"][0]
# print(newDF["B"][0])

newDF.loc[0, 1] = 150
# just for in newDF no more column is left named '1', it crate a new column named '1' and insted of newDF[0][1] all other valuse is put NaN
# print(newDF.head())

newDF = newDF.drop(1, axis=1)
print(newDF.head())

newDF.loc[0, "B"] = 150
print(newDF.head())

print(newDF.loc[[0, 1, 2], ["A", "B", "C"]])
print(newDF.loc[[0, 1, 2], :])
# df.loc[[rows],[columns]].    it show given rows and column from a dataframe.     it return a new DF from given DF but not change existing DF.

# print(newDF.loc[(newDF["A"] > 0.5)])
print(newDF.loc[(newDF["A"] > 0.5) & (newDF["C"] < 0.5)])

print(newDF.iloc[0, 4])
# it return 0'th row and 4'th column value. by default iloc count index from 0
print(newDF.iloc[[1, 5], [3, 4]])
# it return 1'th and 5'th row then 3'rd and 4'th column value.

# newDF.drop(["D", "E"], axis=1, inplace=True)  # it inplace=True is change actual DF
print(newDF)

newDF.drop([1, 3, 5, 7, 9], axis=0, inplace=True)
# newDF = newDF.reset_index()
# DF.reset_index() is add a new index column from 0 to n-1 but not change the original DF
newDF = newDF.reset_index(drop=True)
# DF.reset_index(drop=True) is reset the index from 0 to n-1
print(newDF)

print("\n\n>>\n")
# newDF["B"] = None # it work but not the right way to do that
newDF.loc[:, ["B"]] = None  # here is the right way
print(newDF)
print(newDF["B"].isnull())
