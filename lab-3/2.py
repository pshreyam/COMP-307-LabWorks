"""
Implementation of page replacement algorithms
"""

from prettytable import PrettyTable


def fifo(ref_string, frame_size):
    """
    Implementation of 'First In First Out' page page replacement algorithm
    """
    
    print("\nFIFO\n")
    frame = [None for _ in range(frame_size)]
    page_faults = 0
    table = PrettyTable()

    for page in ref_string:
        if page in frame:
            # Page hit
            table.add_column(f"{page}", ['' for _ in frame])
        else:
            # Page fault
            if None in frame:
                # Free frames
                frame[frame.index(None)] = page
            else:
                # Use page replacement algorithm
                frame = frame[1:] + [page]
            page_faults += 1
            table.add_column(f"{page}", list(map(lambda x: '' if x is None else x, frame)))
    
    print(table)
    print(f"Page faults = {page_faults}")


def optimal(ref_string, frame_size):
    """
    Implementation of 'Optimal' page replacement algorithm
    """
    
    print("\nOptimal\n")
    frame = [None for _ in range(frame_size)]
    page_faults = 0
    table = PrettyTable()

    for i, page in enumerate(ref_string):
        future = ref_string[i+1:]
        
        if page in frame:
            # Page hit
            table.add_column(f"{page}", ['' for _ in frame])
        else:
            # Page Fault
            if None in frame:
                # Free Frames
                frame[frame.index(None)] = page
            else:
                # Use page replacement algorithm
                indices = []
                for x in frame:
                    if x not in future:
                        break
                    else:
                        indices.append(future.index(x))
                if len(indices) == frame_size:
                    victim_index = indices.index(max(indices))
                else:
                    victim_index = frame.index(x)
                frame[victim_index] = page

            page_faults += 1
            table.add_column(f"{page}", list(map(lambda x: '' if x is None else x, frame)))
    
    print(table)
    print(f"Page faults = {page_faults}")


def lru(ref_string, frame_size):
    """
    Implementation of 'Last Recently Used' page replacement algorithm
    """
    
    print("\nLRU\n")
    frame = [None for _ in range(frame_size)]
    page_faults = 0
    table = PrettyTable()

    for page in ref_string:
        if page in frame:
            # Page hit
            frame.remove(page)
            frame.append(page)
            table.add_column(f"{page}", ['' for _ in frame])
        else:
            # Page Fault
            if None in frame:
                # Free Frames
                frame[frame.index(None)] = page
            else:
                # Use page replacement algorithm
                frame.pop(0)
                frame = frame + [page]
            page_faults += 1
            table.add_column(f"{page}", list(map(lambda x: '' if x is None else x, frame)))
    
    print(table)
    print(f"Page faults = {page_faults}")


def second_chance(ref_string, frame_size):
    """
    Implementation of 'Second Chance' page replacement algorithm
    """

    print("\nSecond Chance\n")
    frame = [None for _ in range(frame_size)]
    page_faults = 0
    table = PrettyTable()
    chances = []

    for page in ref_string:
        if page in frame:
            # Page hit
            if page not in chances:
                chances.append(page)
            table.add_column(f"{page}", ['' for _ in frame])
        else:
            # Page fault
            if None in frame:
                # Free frames
                frame[frame.index(None)] = page
            else:
                # Use page replacement algorithm
                i = 0
                victim = frame[i]
                while victim in chances:
                    chances.remove(victim)
                    victim = frame[i+1]
                frame.remove(victim)
                frame = frame + [page]
            page_faults += 1
            table.add_column(f"{page}", list(map(lambda x: '' if x is None else x, frame)))
    
    print(table)
    print(f"Page faults = {page_faults}")


if __name__ == "__main__":
    reference_string = [7, 2, 3, 1, 2, 5, 3, 4, 6, 7, 7, 1, 0, 5, 4, 6, 2, 3, 0, 1]
    frame_size = 3

    fifo(reference_string[:], frame_size)
    lru(reference_string[:], frame_size)
    optimal(reference_string[:], frame_size)
    second_chance(reference_string[:], frame_size)