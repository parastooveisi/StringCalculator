class StringCalculator:

    def add_list(self, input_list):
        result = 0
        for number in input_list:
            result += number
        return result

    def parse_input(self, input_string, delimiter=','):
        return [int(n) for n in input_string.split(delimiter) if n]

    def extract_delimiter(self, input_string):
        delimiter_index = input_string.find("//")

        if delimiter_index == -1:
            # if there is no custom delimiter
            return input_string, ""

        new_line_index = input_string.find("\n")
        numbers_str = input_string[new_line_index + 1:]
        delimiter = input_string[input_string.find("//") + 2: new_line_index]
        return numbers_str, delimiter

    def handle_negative_numbers(self, input_list):

        negatives_list = [n for n in input_list if n < 0]

        if negatives_list:
            raise Exception(
                "Negatives not allowed: {list}".format(list=negatives_list))

        return input_list
