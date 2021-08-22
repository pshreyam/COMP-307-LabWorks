import copy
import pandas as pd
# Function to insert row in the dataframe
def Insert_row(row_number, df, row_value):
    # Starting value of upper half
    start_upper = 0
   
    # End value of upper half
    end_upper = row_number
   
    # Start value of lower half
    start_lower = row_number
   
    # End value of lower half
    end_lower = df.shape[0]
   
    # Create a list of upper_half index
    upper_half = [*range(start_upper, end_upper, 1)]
   
    # Create a list of lower_half index
    lower_half = [*range(start_lower, end_lower, 1)]
   
    # Increment the value of lower half by 1
    lower_half = [x.__add__(1) for x in lower_half]
   
    # Combine the two lists
    index_ = upper_half + lower_half
   
    # Update the index of the dataframe
    df.index = index_
   
    # Insert a row at the end
    df.loc[row_number] = row_value
    
    # Sort the index labels
    df = df.sort_index()
   
    # return the dataframe
    return df


def check_size_invalidity(p_s, df):
    temp = pd.DataFrame({"Partition": [], "Size": []})
    for i, M in df.iterrows():
        if not M["Status"] == 'allocated':
            temp.loc[len(temp)] = [M["Partition"], M["Size"]]
    return p_s > temp["Size"].max()