from string_calculator import StringCalculator
import sys


def main():
    calculator = StringCalculator()

    numbers_str, delimiter = calculator.extract_delimiter(sys.argv[1])

    numbers_list = calculator.parse_input(numbers_str, delimiter)

    result = calculator.add_list(
        calculator.handle_negative_numbers(numbers_list))

    print(result)


if __name__ == '__main__':
    main()
