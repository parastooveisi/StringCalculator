import re


class StringCalculator:

    def add_list(self, input_list):
        """(list) -> int
            Return the sum of numbers in the given list
            >>> String_Calculator = StringCalculator()
            >>> String_Calculator.add_list([1,2,3])
            6
        """

        result = 0
        for number in input_list:
            if number < 1000:
                # for bonus one
                result += number
        return result

    def parse_input(self, input_string, delimiter=','):
        """(string, string) -> list
            Return the list of numbers in the given string
            >>> String_Calculator = StringCalculator()
            >>> String_Calculator.parse_input("1@2$3*", "@,$,*")
            [1, 2, 3]
        """

        if delimiter == len(delimiter) * delimiter[0]:
            # only one kind of char in delimiter ---> ("$$$")
            return [int(n) for n in input_string.split(delimiter) if n]
        else:
            # for bonus three and four. Different characters in delimiter ---> ("$$@@")
            delimiter_string = ""
            for char in delimiter:
                if char == ",":
                    delimiter_string += "|"
                    continue
                delimiter_string += "\\" + char
            return [int(n) for n in re.split(delimiter_string, input_string) if n]

    def extract_delimiter(self, input_string):
        """(string) -> tuple(string, string)
            Return the delimiter separated numbers and delimiter
            >>> String_Calculator = StringCalculator()
            >>> String_Calculator.extract_delimiter('//$,@\n1$2@3')
            ("1$2@3", "$,@")
        """

        # extract_delimiter covers bonus two
        delimiter_index = input_string.find("//")

        if delimiter_index == -1:
            # if there is no custom delimiter
            return input_string, ","

        new_line_index = input_string.find("\n")
        numbers_str = input_string[new_line_index + 1:]
        delimiter = input_string[input_string.find("//") + 2: new_line_index]
        return numbers_str, delimiter

    def handle_negative_numbers(self, input_list):
        """(list) -> list
            Return list of negative numbers in the list
            >>> String_Calculator = StringCalculator()
            >>> String_Calculator.handle_negative_numbers([1, -4, 3, -5])
            [-4, -5]
         """
        negatives_list = [n for n in input_list if n < 0]

        if negatives_list:
            raise Exception(
                "Negatives not allowed: {list}".format(list=negatives_list))

        return input_list
