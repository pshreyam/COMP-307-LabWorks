import pandas as pd
from utils import Insert_row, check_size_invalidity
from prettytable import PrettyTable

class WorstFit():
    def __init__(self, partitions:list, processes:list):
        process = {
            "Processes": [f"p{i+1}" for i in range(len(processes))], 
            "Size": processes,
            }
        
        partition = {
            "Partition": [f"m{i+1}" for i in range(len(partitions))],
            "Size": partitions,
        } 
        
        self.processes = pd.DataFrame(process)
        self.partitions = pd.DataFrame(partition)
        import copy
        self.allocation = copy.deepcopy(self.partitions) 
        self.allocation.insert(2, "Status", "not_allocated")

    def algorithm(self):
        for j in range(len(self.processes)):
            p = self.processes.at[j,"Processes"]
            p_s = self.processes.at[j,"Size"]
            
            # check if size of process exceeds max memory size, if yes, process cannot be allocated
            if check_size_invalidity(p_s, self.allocation):
                print(f"Process {p}(size {p_s}) cannot be allocated.")
                x = PrettyTable()
                x.field_names = list(self.allocation["Partition"])
                x.add_row([int(_) for _ in list(self.allocation["Size"])])
                print(x)
                continue

            # Find worst fit memory for allocating
            # First, create a worst_fit dataframe and populate with all memories that can be allocated
            worst_fit = pd.DataFrame({"Partition": [], "Hole": []})
            for i, M in self.allocation.iterrows():
                if (not M["Status"] == 'allocated') and (not p_s > M["Size"]):
                    worst_fit.loc[len(worst_fit)] = [M["Partition"], M["Size"] - p_s]
            
            # Now, choose worst fit memory from df which is maximum hole size
            worst_fit_partition = worst_fit.at[worst_fit["Hole"].idxmax(),"Partition"]
            worst_fit_hole = worst_fit.at[worst_fit["Hole"].idxmax(),"Hole"]
            worst_fit_index = 0
            for i in range(len(self.allocation)):
                if self.allocation.at[i, "Partition"] == worst_fit_partition:
                    worst_fit_index = i
            
            # At worst_fit_index, allocate the process
            m = self.allocation.at[worst_fit_index, "Partition"]
            m_s = self.allocation.at[worst_fit_index, 'Size']
            self.allocation.at[worst_fit_index, 'Partition'] = p
            self.allocation.at[worst_fit_index, 'Status'] = 'allocated'
            self.allocation.at[worst_fit_index, 'Size'] = p_s
            
            #  If p_s less than m_s, create hole after the allocation
            if p_s < m_s:
                hole = [f"h{p[-1]}", worst_fit_hole, 'hole']
                self.allocation = Insert_row(worst_fit_index+1, self.allocation, hole)
            print(f"Process {p}(size {p_s}) is allocated in memory {m}(size {int(m_s)}).")
            x = PrettyTable()
            x.field_names = list(self.allocation["Partition"])
            x.add_row([int(_) for _ in list(self.allocation["Size"])])
            print(x)

if __name__ == "__main__":
    partition = [300, 600, 350, 200, 750, 125]

    processes = [115, 500, 358, 200, 375]

    ff = WorstFit(partition, processes)
    ff.algorithm()