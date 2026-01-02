from enum_direction import Direction

def main():
    current_direction = Direction.UP
    print(f"The current direction is {current_direction}!")

    direction_list = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
    for direction in direction_list:
        print(f"Moving {direction}!")
    
    print("End of program!")

main()