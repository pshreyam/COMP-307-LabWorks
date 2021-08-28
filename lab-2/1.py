"""
Implementation of Peterson's Solution for dealing with race condition
"""

buffer = []

i, j = 0, 1 # 0 for P0 and 1 for P1

turn = i # either 0 or 1 (ie. P0 or P1)
flag = [False, False] # Flags for process P0 and P1


def critical_section_for_p0(item):
    flag[0] = True
    turn = 1
    
    while (flag[1] and turn == 1):
        pass

    # critical section
    buffer.append(item)
    
    flag[0] = False


def critical_section_for_p1():
    flag[1] = True
    turn = 0
    
    while (flag[0] and turn == 0):
        pass
    
    # critical section
    x = buffer.pop()
    print(x)
    
    flag[1] = False
    
    # remainder section
    print(buffer)


while True:
    # Only P0 can enter
    critical_section_for_p0('a')
    # Only P1 can enter
    critical_section_for_p1()
    # Only P0 can enter
    critical_section_for_p0('b')
    # Only P1 can enter
    critical_section_for_p1()