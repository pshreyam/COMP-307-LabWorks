""" Implementation of Resource Request Algorithm """

import sys

from safety_algorithm import safe_sequence 


def greater_than(first_list, second_list):
    for i in range(len(first_list)):
        if first_list[i] > second_list[i]:
            return True
    return False

# Number of resources
m = 4

# Number of processes
n = 5

resource_request = [0, 4, 2, 0]
request_for_process = 1

available = [1, 5, 2, 0]
allocation = [
    [0, 0, 1, 2],
    [1, 0, 0, 0],
    [1, 3, 5, 4],
    [0, 6, 3, 2],
    [0, 0, 1, 4],
]
maximum_resources = [
    [0, 0, 1, 2],
    [1, 7, 5, 0],
    [2, 3, 5, 6],
    [0, 6, 5, 2],
    [0, 6, 5, 6],
]

need = [[0 for _ in range(m)] for _ in range(n)] 

for i in range(n):
    for j in range(m):
        need[i][j] = maximum_resources[i][j] - allocation[i][j]

if greater_than(resource_request, need[request_for_process]):
    print(f"1) Request[{i}] > Need[{i}]")
    print("The process has exceeded its maximum claim.")
    sys.exit(0)
else:
    print(f"1) Request[{i}] <= Need[{i}]")

if greater_than(resource_request, available):
    print(f"2) Request[{i}] > Available")
    print(f"P_{request_for_process} must wait resources are not available.")
    sys.exit(0)
else:
    print(f"2) Request[{i}] <= Available")

print(f"3) Available = Available - Request[{i}]")
print(f"             = {available} - {resource_request}")
available = [x - y for x, y in zip(available, resource_request)]
print(f"             = {available}\n")

print(f"   Allocation[{i}] = Allocation[{i}] + Request[{i}]")
print(f"                   = {allocation[i]} + {resource_request}")
allocation[request_for_process] = [x + y for x, y in zip(allocation[request_for_process], resource_request)]
print(f"                 = {allocation[request_for_process]}\n")

print(f"   Need[{i}] = Need[{i}] - Request[{i}]")
print(f"           = {need[i]} - {resource_request}")
need[request_for_process] = [x - y for x, y in zip(need[request_for_process], resource_request)]
print(f"           = {need[request_for_process]}\n")

print("So, ")
print(f"Allocation = {allocation}")
print(f"Need = {need}")
print(f"Work = Available = {available}")

# check for safe sequence
print("\nNow, checking for safe state,")
safe_sequence(m, n, available, allocation, maximum_resources, need)
