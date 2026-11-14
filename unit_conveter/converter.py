from collections.abc import ValuesView
from config import KM_TO_MILES, SUPPORTED_CONVERSIONS, C_TO_F_MULTIPLIER


class UnitConverter:
    def __init__(self, kilometer):

        self.kilometer = kilometer

    def convert_distance(
        self,
    ):
        if not isinstance(self.kilometer, (int, float)):
            raise ValueError("Input must be a number")
        else:
            return self.kilometer * KM_TO_MILES

    def convert_temperature(self, celsius):
        return celsius * C_TO_F_MULTIPLIER + 32


if __name__ == "__main__":
    print("testing the app")
    test = UnitConverter(10)
    print(test.convert_distance())
    print(test.convert_temperature(100))
