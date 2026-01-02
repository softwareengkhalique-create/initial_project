from enum_direction import Direction

def test_direction_up():
    assert Direction.UP == "up", "Up direction not equal"

def test_direction_down():
    assert Direction.DOWN == "down", "Down direction not equal"

def test_direction_left():
    assert Direction.LEFT == "left", "Down direction not equal"