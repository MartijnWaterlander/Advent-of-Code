import numpy as np


def check(val: int) -> None:
    """
    Adjusts the global currentvalue based on the input value.
    Handles wrapping around 0-99 range.

    Args:
        val (int): The value to check and adjust.
    """
    global currentvalue
    currentvalue = val % 100
    if 0 <= currentvalue < 100:
        return
    elif currentvalue >= 100:
        currentvalue = currentvalue - 100
        return
    elif currentvalue < 0:
        currentvalue = 100 + currentvalue
        return


def rotation(line: str) -> None:
    """
    Updates the current value based on a rotation command.

    Args:
        line (str): The rotation command (e.g., "R10", "L5").
    """
    global currentvalue
    if line[0] == "R":
        currentvalue += int(line[1:])
        check(currentvalue)
    else:
        currentvalue -= int(line[1:])
        check(currentvalue)

    return


numbers = np.linspace(0, 99, 100, dtype=int)
currentvalue = int(50)
code = int(0)

path = "Data/day1_1.txt"
with open(path, "r", encoding="utf-8") as f:
    for lineno, line in enumerate(f, start=1):
        oldval = currentvalue
        rotation(line)

        if currentvalue == 0:
            code += 1
        print(f"{oldval} -> {line.strip()} -> {currentvalue} | Code: {code}")


print(code)
