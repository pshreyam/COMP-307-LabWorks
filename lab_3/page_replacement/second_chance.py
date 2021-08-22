import pandas as pd
from utils import free_frame, get_frame_list
from prettytable import PrettyTable

class SecondChance():
    def __init__(self, page_reference:list, page_frame_size:int):
        self.page_reference = pd.Series(page_reference)
        self.frame_size = page_frame_size
        S = [None for _ in range(self.frame_size)]
        Status = [-1 for _ in range(self.frame_size)]
        Reference = [0 for _ in range(self.frame_size)]
        self.frame = pd.DataFrame({"Frame": S, "Status": Status, "Reference": Reference})
        self.page_fault = 0
        self.table = PrettyTable()
    
    def get_victim(self, ref):
        sc_index = []
        max = self.frame_size - 1
        while(max >= 0):
            for j, V in self.frame.iterrows():
                if V["Status"] == max:
                    if V["Reference"] == 0:
                        self.frame.at[j, "Frame"] = ref
                        self.frame.at[j, "Reference"] = 0
                        self.frame.at[j, "Status"] = 0
                        self.update_status_sc(j, sc_index)
                        self.page_fault += 1
                        return
                    else:
                        self.frame.at[j, "Reference"] = 0
                        sc_index.append(j)
                    continue
            max -= 1
    
    def update_status_sc(self, i_victim, sc_index):
        i_rest = [_ for _ in range(self.frame_size)]
        i_rest.remove(i_victim)
        # print(i_rest)
        if sc_index:
            for sc in sc_index:
                i_rest.remove(sc)
        for i in i_rest:
            self.frame.at[i, "Status"] += 1

    def update_status(self):
        for i in range(len(self.frame)):
            status = self.frame.at[i, "Status"]
            if not status == -1:
                self.frame.at[i, "Status"] = (status + 1) % self.frame_size
    
    def check_reference_avaibility(self, ref):
        for i, F in self.frame.iterrows():
            if F["Frame"] == ref:
                return F["Status"], i
        return -1, -1
    
    def get_frame_list(self):
        frame = list(self.frame["Frame"])
        reference_bit = list(self.frame["Reference"])
        for i in range(len(frame)):
            if  frame[i] == None:
                frame[i] = ''
                reference_bit[i] = ''
        return_f = []
        for i in range(len(frame)):
            if frame[i] != '':
                return_f.append(f"{str(frame[i])} ({str(reference_bit[i])})")
            else:
                return_f.append('')
        return return_f

    def algorithm(self):
        for ref in self.page_reference:
            # Check if reference is already in frame, if yes, mark reference bit of frame to 1 and skip
            s_ref, i_ref = self.check_reference_avaibility(ref)
            if not s_ref == -1:
                self.frame.at[i_ref, "Reference"] = 1
                self.table.add_column(ref, ['' for _ in range(self.frame_size)])
                # print(f"{ref} -> {i_ref}")
                # print(self.frame)
                continue

            # check if there are any free frame i.e. frame["Frame"] = None and skip
            i_frame = free_frame(self.frame)
            if not i_frame == None:
                self.update_status()
                self.frame.at[i_frame, "Frame"] = ref
                self.frame.at[i_frame, "Status"] = 0
                self.frame.at[i_frame, "Reference"] = 0
                self.page_fault += 1
                self.table.add_column(ref, self.get_frame_list())
                # print(ref)
                # print(self.frame)
                continue
            
            # If no free frame, select victim
            self.get_victim(ref)
            self.table.add_column(ref, self.get_frame_list())
            # print(ref)
            # print(self.frame)
        print(self.table)
        print(f"Total Page Fault: {self.page_fault}\n")

            
if __name__ == '__main__':
    # pr = ['7', '2', '3', '1', '2', '5', '3', '4', '6', '7', '7', '1', '0', '5', '4', '6', '2', '3', '0', '1']
    pr = '0 4 1 4 2 4 3 4 2 4 0 4 1 4 2 4 3 4'.split()
    pf = 3

    sc = SecondChance(pr, pf)
    sc.algorithm()