"""
Implementation of first-fit, best-fit and worst-fit allocation algorithms
"""

MAX_GAP = 9999999999


def first_fit(processes, holes, unit):
    """
    Allocate holes to processes using the first-fit allocation algorithm
    """

    print("First-Fit:\n")
    print(f"Holes: {holes}\n")

    for j, process in enumerate(processes):
        print(f"For P{j} ({process} {unit}):")
        for i, hole in enumerate(holes):
            if process > hole:
                if i == len(holes) - 1:
                    print(f"P{j} does not fit in any hole.\n")
            else:
                gap = hole - process
                holes[holes.index(hole)] = gap
                break
        print(f"P{j} fits in hole with size {hole} {unit} with {gap} {unit} size remaining.")
        print(f"Remaining holes: {holes}\n")


def best_fit(processes, holes, unit):
    """
    Allocate holes to processes using the best-fit allocation algorithm
    """

    print("Best-Fit:\n")
    print(f"Holes: {holes}\n")

    for j, process in enumerate(processes):
        gaps = [MAX_GAP for _ in holes]
        print(f"For P{j} ({process} {unit}):")
        for i, hole in enumerate(holes):
            if process > hole:
                pass
            else:
                gap = hole - process
                gaps[i] = gap
        
        min_gap = min(gaps)

        if min_gap == MAX_GAP:
            print(f"P{j} does not fit in any hole. It has to wait.\n")
        else:
            hole = holes[gaps.index(min_gap)]
            holes[gaps.index(min_gap)] = min_gap

            print(f"P{j} fits in hole with size {hole} {unit} with {min_gap} {unit} size remaining.")
            print(f"Remaining holes: {holes}\n")


def worst_fit(processes, holes, unit):
    """
    Allocate holes to processes using the worst-fit allocation algorithm
    """

    print("Worst-Fit:\n")
    print(f"Holes: {holes}\n")

    for j, process in enumerate(processes):
        gaps = [-MAX_GAP for _ in holes]
        print(f"For P{j} ({process} {unit}):")
        for i, hole in enumerate(holes):
            if process > hole:
                pass
            else:
                gap = hole - process
                gaps[i] = gap
        
        max_gap = max(gaps)

        if max_gap == -MAX_GAP:
            print(f"P{j} does not fit in any hole. It has to wait.\n")
        else:
            hole = holes[gaps.index(max_gap)]
            holes[gaps.index(max_gap)] = max_gap

            print(f"P{j} fits in hole with size {hole} {unit} with {max_gap} {unit} size remaining.")
            print(f"Remaining holes: {holes}\n")


if __name__ == "__main__":
    holes = [300, 600, 350, 200, 750, 125]
    processes = [115, 500, 358, 200, 375]
    unit = "KB"

    print(f"Processes: {processes}")
    print(f"Holes: {holes}")

    print("#" * 50, end="\n\n")

    first_fit(processes[:], holes[:], unit)
    best_fit(processes[:], holes[:], unit)
    worst_fit(processes[:], holes[:], unit)