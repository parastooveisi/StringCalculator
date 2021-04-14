class StringCalculator:

    def add_list(self, input_list):
        result = 0
        for number in input_list:
            result += number
        return result

    def parse_input(self, input_string):
        return [int(n) for n in input_string.split(",") if n]
