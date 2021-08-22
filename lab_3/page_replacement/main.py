from fifo import FIFO
from lru import LRU
from optimal import Optimal
from second_chance import SecondChance

if __name__ == "__main__":
    reference = input("Give page reference in order: \t").split()
    _frame = input("Give Memory Partition in order: \t").split()

    frame = [int(_) for _ in _frame]

    flag = input("Want FIFO Algorithm?(Y/n)")
    if flag == '' or flag.capitalize() == "Y":
        for F in frame:
            print(f"~~~~~~~~~~~~~~~{int(F)} frames~~~~~~~~~~~~~~~~\n")
            fifo = FIFO(reference, F)
            fifo.algorithm()
    print('\n')

    flag = input("Want LRU Algorithm?(Y/n)")
    if flag == '' or flag.capitalize() == "Y":
        for F in frame:
            print(f"~~~~~~~~~~~~~~~{int(F)} frames~~~~~~~~~~~~~~~~\n")
            lru = LRU(reference, F)
            lru.algorithm()
    print('\n')

    flag = input("Want Optimal Algorithm?(Y/n)")
    if flag == '' or flag.capitalize() == "Y":
        for F in frame:
            print(f"~~~~~~~~~~~~~~~{int(F)} frames~~~~~~~~~~~~~~~~\n")
            optimal = Optimal(reference, F)
            optimal.algorithm()
    print('\n')

    flag = input("Want Second Chance Algorithm?(Y/n)")
    if flag == '' or flag.capitalize() == "Y":
        for F in frame:
            print(f"~~~~~~~~~~~~~~~{int(F)} frames~~~~~~~~~~~~~~~~\n")
            sc = SecondChance(reference, F)
            sc.algorithm()
    print('\n')