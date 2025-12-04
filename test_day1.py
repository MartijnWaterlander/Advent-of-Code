import day1_2   # import the module, not just the function


def run_rotation(start, cmd):
    """
    Helper to reset day1_2 globals, run rotation(command),
    and return (final_position, code_value).

    Args:
        start (int): Starting value.
        cmd (str): Rotation command.

    Returns:
        tuple: (final_position, code_value)
    """
    day1_2.currentvalue = start
    day1_2.code = 0
    day1_2.rotation(cmd)
    return day1_2.currentvalue, day1_2.code


def test_land_on_zero_forward():
    pos, c = run_rotation(20, "R80")
    assert pos == 0
    assert c == 1


def test_land_on_zero_backward():
    pos, c = run_rotation(5, "L5")
    assert pos == 0
    assert c == 1


def test_cross_zero_forward_once():
    pos, c = run_rotation(95, "R10")
    assert pos == 5
    assert c == 1


def test_cross_zero_backward_once():
    pos, c = run_rotation(3, "L10")
    assert pos == 93
    assert c == 1


def test_multiple_wraps_forward():
    pos, c = run_rotation(50, "R867")
    assert pos == 17
    assert c == 9


def test_multiple_wraps_backward():
    pos, c = run_rotation(30, "L250")
    assert pos == 80
    assert c == 3


def test_large_number_forward():
    pos, c = run_rotation(0, "R12345")
    assert pos == 45
    assert c == 123


def test_large_number_backward():
    pos, c = run_rotation(10, "L10000")
    assert pos == 10
    assert c == 100


def test_no_wrap_forward():
    pos, c = run_rotation(50, "R20")
    assert pos == 70
    assert c == 0


def test_no_wrap_backward():
    pos, c = run_rotation(50, "L20")
    assert pos == 30
    assert c == 0
