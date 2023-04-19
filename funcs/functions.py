from functools import reduce


def literal_number(text: str):
    nums: dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    return nums[text] if text in nums else False


def sum_nosum(ls: list):
        return reduce(lambda num1, num2: num1+num2, map(lambda x: x, ls)) if ls != [] else 0


def no_vaules(string: str):
    return string.replace("a", "").replace("o", "").replace("u", "").replace("e", "")


def repetitive_nums(min_value: int, max_value: int):
    return sum(str(num).count(digit) for num in range(min_value, max_value+1) for digit in ('8', '0'))


