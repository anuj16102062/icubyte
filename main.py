import re

def add(numbers: str) -> int:
    if not numbers:
        return 0
    delimiter = ",|\n"
    custom_delimiter_match = re.match(r"^//(.+)\n(.*)", numbers)

    if custom_delimiter_match:
        delimiter = re.escape(custom_delimiter_match.group(1))
        numbers = custom_delimiter_match.group(2)

    split_numbers = re.split(delimiter, numbers)
    num_list = [int(num) for num in split_numbers if num]
    negatives = [num for num in num_list if num < 0]

    if negatives:
        negatives_str = ",".join(map(str, negatives))
        raise ValueError(f"negative numbers not allowed {negatives_str}")
    return sum(num_list)