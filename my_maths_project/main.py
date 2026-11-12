from math_tools import square_calculater,cube_calculator

def main():
    print("-----starting main application ------")
    num=5
    square=square_calculater(num)
    cube=cube_calculator(num)

    print(f"the square of {num} is {square}")
    print(f"the cube of {num} is {cube}")
    return main