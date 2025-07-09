                                                    #   Question 1
                                                    
''' How to convert a Series of data-strings to a timeseries ?  '''


import pandas as pd

date_series = pd.Series(['2025-01-02', '2025-01-06', '2025-01-23'])
time_series = pd.to_datetime(date_series)
print(time_series,"\n")




                                                    #   Question 2
                                                    
''' Create two DataFrames, df1 and df2, with a common column (e.g., 'ID').
 - Perform an inner merge on this common column and display the resulting DataFrame.
 - Perform a left join of df1 and df2 on the 'ID' column. Explain how missing values are handled in the resulting DataFrame. Right Join and Index-Based Join.
 - Perform a right join using pd.merge() on a common column, then perform a join using df.join() based on the index. Compare the results. Merging with Multiple Keys.'''


import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5, 7],
    'Name': ['Jatin', 'Kannu', 'Aayu', 'Deepak', 'Jhanvi', 'Harshit']
})

df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6, 7, 8],
    'Marks': [98, 85, 90, 88, 75, 82]
})

print(df1,"\n")
print(df2,"\n")


# inner merge ( Joins only Matching ID from both Dataframes )

inner_merge = pd.merge(df1, df2, on='ID', how='inner')
print("\nInner Merge:\n", inner_merge)


# Left Join  ( Keeps all data from df1; fills NaN where no match in df2 )

left_join = pd.merge(df1, df2, on='ID', how='left')
print("\nLeft Join:\n", left_join)


# Right Join  ( Keeps all data from df2, fills NaN where no match in df1 )

right_join = pd.merge(df1, df2, on='ID', how='right')
print("\nRight Join:\n", right_join)


# Index-Based Join

df1_index = df1.set_index('ID')
df2_index = df2.set_index('ID')

index_join = df1_index.join(df2_index, how='inner')
print("\nIndex-Based Join:\n", index_join)


# Multiple Key Merge

df1_multi = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5, 7],
    'Section': ['A', 'A', 'B', 'B', 'C', 'D'],
    'Name': ['Jatin', 'Kannu', 'Aayu', 'Deepak', 'Jhanvi', 'Harshit']
})

df2_multi = pd.DataFrame({
    'ID': [3, 4, 3, 5, 7],
    'Section': ['B', 'A', 'C', 'C', 'D'],
    'Marks': [98, 85, 91, 90, 75]
})

multi_merge = pd.merge(df1_multi, df2_multi, on=['ID', 'Section'], how='inner') 
# It compares both ID and Section in each row of both dataframes.If both match exactly, it joins the rows.

print("\nMerge on Multiple Keys:\n", multi_merge)




                                                      #  Question 3


'''Create three DataFrames. Vertically concatenate two of them using pd.concat(), then merge the resulting DataFrame with the third DataFrame on a common key. T Understand join() vs. merge().
Also, Explain the primary differences between df.join() and pd.merge(),'''                                                 


df1 = pd.DataFrame({
    'ID': [1, 2, 5, 6],
    'Name': ['Jatin', 'Viren', 'Kannu', 'Jhanvi']
})

df2 = pd.DataFrame({
    'ID': [3, 4, 7, 8],
    'Name': ['Rihan', 'Aadi', 'Yuvi', 'Kartik']
})

df3 = pd.DataFrame({
    'ID': [2, 3, 4, 6, 7, 9],
    'Marks': [88, 91, 75, 95, 84, 89]
})

df = pd.concat([df1, df2], ignore_index=True)
print("Concatenated df1 and df2:\n", df)

merge = pd.merge(df, df3, on='ID', how='inner')
print("\nMerged DataFrame :\n", merge)

merged = pd.merge(df1, df3, on='ID', how='left')
print("\nMerge on 'ID' with left join:\n", merged)

df1_index = df1.set_index('ID')
df3_index = df3.set_index('ID')

joined = df1_index.join(df3_index, how='left')
print("\nJoin on index:\n", joined)


