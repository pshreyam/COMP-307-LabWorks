import pandas as pd
from utils import check_reference_avaibility, free_frame, get_frame_list
from prettytable import PrettyTable

class FIFO():
    def __init__(self, page_reference:list, page_frame_size:int):
        self.page_reference = pd.Series(page_reference)
        self.frame_size = page_frame_size
        S = [None for _ in range(self.frame_size)]
        Status = [-1 for _ in range(self.frame_size)]  
        self.frame = pd.DataFrame({"Frame": S, "Status": Status})
        self.page_fault = 0
        self.table = PrettyTable()
    
    def get_victim(self):
        for i, F in self.frame.iterrows():
            if F["Status"] == self.frame_size - 1:
                return i
    
    def update_status(self):
        for i in range(len(self.frame)):
            status = self.frame.at[i, "Status"]
            if not status == -1:
                self.frame.at[i, "Status"] = (status + 1) % self.frame_size

    def algorithm(self):
        for ref in self.page_reference:
            # Check if reference is already in frame, if yes, skip
            s_ref = check_reference_avaibility(self.frame, ref)
            if not s_ref == None:
                self.table.add_column(ref, ['' for _ in range(self.frame_size)])
                continue

            # check if there are any free frame i.e. frame["Frame"] = None and skip
            i_frame = free_frame(self.frame)
            if not i_frame == None:
                self.update_status()
                self.frame.at[i_frame, "Frame"] = ref
                self.frame.at[i_frame, "Status"] = 0
                self.page_fault += 1
                self.table.add_column(ref, get_frame_list(self.frame))
                continue
            
            # If no free frame, select victim
            i_victim = self.get_victim()
            self.update_status()
            self.frame.at[i_victim, "Frame"] = ref
            self.page_fault += 1
            self.table.add_column(ref, get_frame_list(self.frame))
        print(self.table)
        print(f"Total Page Fault: {self.page_fault}\n")


if __name__ == '__main__':
    pr = ['7', '2', '3', '1', '2', '5', '3', '4', '6', '7', '7', '1', '0', '5', '4', '6', '2', '3', '0', '1']
    pf = 3

    fifo = FIFO(pr, pf)
    fifo.algorithm()