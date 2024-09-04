import re


class StringCalculator:
    @staticmethod
    def add(numbers: str) -> int:
        if not numbers:
            return 0

        # Handling custom delimiter
        delimiter = ',|\n'  # Default delimiter is comma or newline
        if numbers.startswith('//'):
            delimiter_match = re.match(r"//(.+)\n(.*)", numbers)
            if delimiter_match:
                delimiter = re.escape(delimiter_match.group(1))  # Escape delimiter for regex
                numbers = delimiter_match.group(2)  # Actual numbers part

        # Split the string using the defined delimiters
        num_list = re.split(delimiter, numbers)

        # Convert strings to integers and handle negative numbers
        negatives = []
        result = 0
        for num in num_list:
            if num:
                n = int(num)
                if n < 0:
                    negatives.append(n)
                result += n

        if negatives:
            raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")

        return result
