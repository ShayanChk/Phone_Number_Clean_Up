#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

# Load the CSV data into a DataFrame
df = pd.read_csv("Phone_Numbers.csv")

# creating a column called 'Number of Digits' in the csv file (Phone_Numbers)
df['Number Of Digits'] = 0

# There are three columns containing phone number (Phone (1), Phone (2), Phone (3)). I am creating a loop to check each cell
# of each column to ignore the empty cells and flag the cells that contain less or more than 10 digits in them
for i in range(1, 4):
    column_name = f'Phone ({i}) (Cleaned)'
    if column_name in df.columns:
        # Count digits and update 'Number Of Digits' if the count is not 10
        df.loc[df[column_name].astype(str).str.count(r'\d') != 10, 'Number Of Digits'] = 1

# Save the modified DataFrame to a new CSV file
df.to_csv("Checked_Phone_Numbers.csv", index=False)

