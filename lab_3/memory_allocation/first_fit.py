import pandas as pd
from utils import Insert_row, check_size_invalidity
from prettytable import PrettyTable

class FirstFit():
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
                x.add_row(list(self.allocation["Size"]))
                print(x)
                continue
            
            # For every memories, choose which can be allocated in order
            for i in range(len(self.allocation)):
                # if memory space already allocated, skip
                if self.allocation.at[i, 'Status'] == 'allocated':
                    continue
                
                # Get memory size 
                m = self.allocation.at[i, "Partition"]
                m_s = self.allocation.at[i, 'Size']

                # if process size greater than memory size, skip
                if p_s > m_s:
                    continue
                
                # Allocate the process to memory
                self.allocation.at[i, 'Partition'] = p
                self.allocation.at[i, 'Status'] = 'allocated'
                self.allocation.at[i, 'Size'] = p_s
                
                # if p_s less than m_s, create hole after the allocation and break the loop 
                if p_s < m_s:
                    hole_size = m_s - p_s
                    hole = [f"h{p[-1]}", hole_size, 'hole']
                    self.allocation = Insert_row(i+1, self.allocation, hole)
                print(f"Process {p}(size {p_s}) is allocated in memory {m}(size {m_s}).")
                x = PrettyTable()
                x.field_names = list(self.allocation["Partition"])
                x.add_row(list(self.allocation["Size"]))
                print(x)
                break

if __name__ == "__main__":
    partition = [300, 600, 350, 200, 750, 125]

    processes = [115, 500, 358, 500, 400]

    ff = FirstFit(partition, processes)
    ff.algorithm()