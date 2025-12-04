import numpy as np


def rotation(line: str) -> None:
    """
    Processes a rotation command and updates the global currentvalue and code.
    Tracks how many times the value wraps around the 0-99 range.

    Args:
        line (str): The rotation command string (e.g., "R50").
    """
    global currentvalue, code

    direction = line[0]
    val = int(line[1:])
    old = currentvalue

    if direction == "R":
        new = old + val

        # number of times we pass zero
        passes = (old + val) // 100

        code += passes

        # landing exactly on 0 (only if final modulo is 0)
        if new % 100 == 0:
            code += 1

        currentvalue = new % 100

    else:  # L
        new = old - val

        # number of passes going backward
        # absolute value needed for negative new
        passes = abs((old - val) // 100)

        code += passes

        # landing exactly on 0
        if new % 100 == 0:
            code += 1

        currentvalue = new % 100


if __name__ == "__main__":
    numbers = np.linspace(0, 99, 100, dtype=int)
    currentvalue = int(50)
    code = int(0)

    path = "Data/day1_1.txt"
    with open(path, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            oldval = currentvalue
            rotation(line)

            # print(f"{oldval} -> {line.strip()} -> {currentvalue} | Code: {code}")
    print(code)
