import sys
from _codecs import decode

from string_calculator import StringCalculator


def main():
    if len(sys.argv) == 2:

        calculator = StringCalculator()

        decoded_input = decode(sys.argv[1], 'unicode_escape')
        result = calculator.add(decoded_input)

        print(result)
    else:
        print(
            "Usage: python main.py //[delimiter]\\n[delimiter separated numbers]")
        sys.exit(1)


if __name__ == '__main__':
    main()
