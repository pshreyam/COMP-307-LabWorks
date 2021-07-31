""" Implementation of Safety Algorithm """

import sys

def greater_than(first_list, second_list):
    for i in range(len(first_list)):
        if first_list[i] > second_list[i]:
            return True
    return False

# Number of resources
m = 4

# Number of processes
n = 6

available = [3, 1, 2, 1]
allocation = [
    [2, 0, 2, 1],
    [0, 1, 1, 1],
    [4, 1, 0, 2],
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [4, 2, 4, 4]
]
maximum_resources = [
    [9, 5, 5, 5],
    [2, 2, 3, 3],
    [7, 5, 4, 4],
    [3, 3, 3, 2],
    [5, 2, 2, 1],
    [7, 6, 7, 7]
]

need = [[0 for _ in range(m)] for _ in range(n)] 

for i in range(n):
    for j in range(m):
        need[i][j] = maximum_resources[i][j] - allocation[i][j]

safe_sequence = []

finish = [False for _ in range(n)]
finish_preserved = finish[:]
work = available[:]

print(f"\nAvailable = {available}")
print(f"Max = {maximum_resources}")
print(f"Allocation = {allocation}")
print("\nStep 1:\n")
print(f"Need = {need}")
print(f"Finish = {finish}")
print(f"Work = Available = {work}")

print("\nStep 2:\n")
while not all(finish):
    for i in range(n):
        if finish[i]:
            continue
        print(f"For P_{i},\n")
        print(f"(a) Finish[{i}] = {finish[i]}")
        print(f"(b) Need[{i}] is less than equal to Work? : {not greater_than(need[i], work)}\n")
        if not finish[i] and not greater_than(need[i], work): 
            print(f"Work = Work + Allocation[{i}]")
            print(f"     = {work} + {allocation[i]}")
            for j in range(m):
                work[j] = work[j] + allocation[i][j]
            print(f"     = {work}")
            finish[i] = True
            print(f"Finish[{i}] = {finish[i]}")
            safe_sequence.append(i)
            print("\nSafe sequence <", ", ".join([f"P_{i}" for i in safe_sequence]), ">\n")
            print("-"*50, "\n")
        else:
            print(f"Process P_{i} has to wait.\n")
            print("-"*50, "\n")
        
        if i == 5 and finish == finish_preserved:
            print("Safe state cannot be achieved.")
            sys.exit(0)

        finish_preserved = finish[:]
