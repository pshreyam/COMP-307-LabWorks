from prettytable import PrettyTable

def check_reference_avaibility(df, page_reference):
    for i, F in df.iterrows():
        if F["Frame"] == page_reference:
            return F["Status"]
    return None

def free_frame(df):
    for i, F in df.iterrows():
        if F["Status"] == -1:
            return i
    return None

def get_frame_list(df):
    frame = list(df["Frame"])
    for i in range(len(frame)):
        if  frame[i] == None:
            frame[i] = ''   
    return frame