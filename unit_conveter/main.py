from os import name
from time import process_time_ns
from converter import UnitConverter


def main():
    print("THE MAIN APP")
    b1 = UnitConverter(10)
    print(b1)
    print(b1.convert_temperature(100))
    print(b1)
    print("______________________________________")
    print(b1.convert_distance())


if __name__ == "__main__":
    main()
