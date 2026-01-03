from enum_direction import Direction
import pytest

import sys

def main():
    current_direction = Direction.UP
    print(f"The current direction is {current_direction}!")

    direction_list = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
    for direction in direction_list:
        print(f"Moving {direction}!")
    
    print("End of program!")

import pytest
import sys

if __name__ == "__main__":
    # Run pytest on the current directory
    exit_code = pytest.main(["."])
    
    # If exit_code is 0, it means tests passed
    if exit_code == 0:
        print("✅ Tests passed! Starting program...\n")
        # --- Your actual program logic starts here ---
        main()
        print("Program completed!")
    else:
        print("❌ Tests failed. Program aborted.")
        sys.exit(exit_code)