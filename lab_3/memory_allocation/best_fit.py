import pandas as pd
from utils import Insert_row, check_size_invalidity
from prettytable import PrettyTable

class BestFit():
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
            
            # Find best fit memory for allocating
            # First, create a best_fit dataframe and populate with all memories that can be allocated
            best_fit = pd.DataFrame({"Partition": [], "Hole": []})
            for i, M in self.allocation.iterrows():
                if (not M["Status"] == 'allocated') and (not p_s > M["Size"]):
                    best_fit.loc[len(best_fit)] = [M["Partition"], M["Size"] - p_s]
            
            # Now, choose best fit memory from df which is minimum hole size
            best_fit_partition = best_fit.at[best_fit["Hole"].idxmin(),"Partition"]
            best_fit_hole = best_fit.at[best_fit["Hole"].idxmin(),"Hole"]
            best_fit_index = 0
            for i in range(len(self.allocation)):
                if self.allocation.at[i, "Partition"] == best_fit_partition:
                    best_fit_index = i
            
            # At best_fit_index, allocate the process
            m = self.allocation.at[best_fit_index, "Partition"]
            m_s = self.allocation.at[best_fit_index, 'Size']
            self.allocation.at[best_fit_index, 'Partition'] = p
            self.allocation.at[best_fit_index, 'Status'] = 'allocated'
            self.allocation.at[best_fit_index, 'Size'] = p_s
            
            #  If p_s less than m_s, create hole after the allocation
            if p_s < m_s:
                hole = [f"h{p[-1]}", best_fit_hole, 'hole']
                self.allocation = Insert_row(best_fit_index+1, self.allocation, hole)
            print(f"Process {p}(size {p_s}) is allocated in memory {m}(size {int(m_s)}).")
            x = PrettyTable()
            x.field_names = list(self.allocation["Partition"])
            x.add_row([int(_) for _ in list(self.allocation["Size"])])
            print(x)

if __name__ == "__main__":
    partition = [300, 600, 350, 200, 750, 125]

    processes = [115, 500, 358, 200, 375]

    ff = BestFit(partition, processes)
    ff.algorithm()