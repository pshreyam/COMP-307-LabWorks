from first_fit import FirstFit
from best_fit import BestFit
from worst_fit import WorstFit
from prettytable import PrettyTable

if __name__ == "__main__":
    _partition = input("Give Memory Partition in order: \t").split()
    _processes = input("Give processes in order: \t").split()

    partition = [int(_) for _ in _partition]
    processes = [int(_) for _ in _processes]

    print("\nMemory Partitions")
    x = PrettyTable()
    x.field_names = [f"m{i+1}" for i in range(len(partition))]
    x.add_row(partition)
    print(x, '\n')

    print("Given Processes")
    x = PrettyTable()
    x.field_names = [f"p{i+1}" for i in range(len(processes))]
    x.add_row(processes)
    print(x, '\n')

    flag = input("Want First Fit Algorithm?(Y/n)")
    if flag == '' or flag.capitalize() == "Y":
        print ("~~~~~~~~~~~~~~~~~~~~~~~~First Fit Algorithm~~~~~~~~~~~~~~~~~~~~~")
        ff = FirstFit(partition, processes)
        ff.algorithm()
    print('\n')

    flag = input("Want Best Fit Algorithm?(Y/n)")
    if flag == '' or flag.capitalize() == "Y":
        print ("~~~~~~~~~~~~~~~~~~~~~~~~Best Fit Algorithm~~~~~~~~~~~~~~~~~~~~~")
        bf = BestFit(partition, processes)
        bf.algorithm()
    print('\n')
    
    flag = input("Want Worst Fit Algorithm?(Y/n)")
    if flag == '' or flag.capitalize() == "Y":
        print ("~~~~~~~~~~~~~~~~~~~~~~~~Worst Fit Algorithm~~~~~~~~~~~~~~~~~~~~~")
        wf = WorstFit(partition, processes)
        wf.algorithm()
    print('\n')