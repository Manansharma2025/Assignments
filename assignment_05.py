import pandas as pd

#Practise Pandas Series
#       Create a Pandas Series from Dictionary
#       Create a Pandas Series from Lists
#       Access the elements of a Series in Pandas
dict1 = {'a': 10, 'b': 20, 'c': 30}
s1 = pd.Series(dict1)
print("series from dictionary : ")
print(s1)

list1 = [10, 20, 30, 40, 50]
s2 = pd.Series(list1)
print("\nseries from list : ")
print(s2)
###################we can also give index to it###################
index_label = ['a', 'b', 'c', 'd', 'e']
s2.index = index_label
print("\n",s2)

print("first element of s1 series : ", s1.iloc[0])
print("first 3 element of s2 series :\n", s2.iloc[0:3])
print("element of s1 series with index label b : ", s1["b"])
print("any two element of s2 series : \n", s1[["a","c"]])
print("accessing by element values : \n", s2[s2>20])

#DataFrames
#       Make a Pandas DataFrame with a two-dimensional Python list
#       Create DataFrame from Python dict
#       Create Pandas dataframe using list of lists
#       Create a Pandas dataframe using list of tuples
#       Create a Pandas DataFrame from List of Dicts

list2 = [[1,"kanishk",25],[2,"jatin",15],[3,"raju",22]]
df1 = pd.DataFrame(list2, columns=["roll no", "name", "marks"])
print("\nDataFrame fromm a 2d list : ")
print(df1)

dict2 = {'roll no': [1, 2, 3], 'name': ['keshav', 'ashutosh', 'udayan'], 'marks': [25, 30, 35]}
df2 = pd.DataFrame(dict2)
print("\ndataframe from dictionary : ")
print(df2)

print("\n 2D list and list of list are same i think.")
list3 = [[1,"kanishk",25],[2,"jatin",15],[3,"raju",22]]
df3 = pd.DataFrame(list3, columns=["roll no", "name", "marks"])
print("\nDataFrame fromm a list of list : ")
print(df3)

list_o_tupl = [(1,"kanishk",25),(2,"jatin",15),(3,"raju",22)]
df4 = pd.DataFrame(list_o_tupl, columns=["roll no", "name", "marks"])
print("\nDataFrame fromm a list of tupples : ")
print(df4)

list_o_dicts = [{'roll no': 1, 'name': 'kanishk', 'marks': 25},{'roll no': 2, 'name': 'keshav', 'marks': 30},{'roll no': 3, 'name': 'jatin', 'marks': 35}]
df5 = pd.DataFrame(list_o_dicts)
print("\n Dataframe from a list of dictionaries : ")
print(df5)

#Data iteration
#       Different ways to iterate over rows in Pandas Dataframe
#       Selecting rows in pandas DataFrame based on conditions
#       Select any row from a Dataframe using iloc[]
#       Limited rows selection with given column
#       Drop rows from the dataframe based on certain condition applied on a column
#       Insert row at given position in Pandas Dataframe
#       Create a list from rows in Pandas dataframe

result = df1.loc[0]
print("\nrow 1 of dataframe df1 : ")
print(result)

result = df1.loc[[1,2]]
print("\nrow 2 and 3 of dataframe df1 : ")
print(result)

result = df1.iloc[0:2]
print("\nrange of rows of dataframe df1 : ")
print(result)

result = df2[df2["marks"]>25]
print("\nall data from df2 where marks > 25 : ")
print(result)

print("\nFirst row of df3 : ")
print(df3.iloc[0])

print("\nLast two rows of df3 : ")
print(df3.iloc[-2:])

print("\nrows 1 to 2 with column name : ")
print(df4.iloc[0:2]["marks"])

print("\nrows 1 and 2 using column index : ")
print(df4.iloc[0:2,2])

print("\nsame as above using loc : ")
print(df4.loc[0:1,"marks"])

print("\nOriginal DataFrame:")
print(df5)

result = df5[df5['marks'] != 30]
print("\ndataframe after dropping rows where marks=30:")
print(result)
