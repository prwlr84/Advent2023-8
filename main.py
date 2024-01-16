from input import data
from math import gcd
from functools import reduce


def remove_bracket(string):
    return ''.join(char for char in string if char.isalnum())


def parse_input(string):
    input_data = [item for item in string.split('\n') if item]
    pattern =['0'if char == 'L' else '1' for char in list(input_data[0])]
    mapping = {}
    for s in input_data[1:]:
        arr = s.split()
        mapping[arr[0]] = [remove_bracket(arr[2]), remove_bracket(arr[3])]

    return [pattern, mapping]


def lcm(numbers):
    def lcm_of_two(a, b):
        return a * b // gcd(a, b)

    return reduce(lcm_of_two, numbers, 1)


def find_step_count(string):
    pattern, mapping = parse_input(string)
    step_count = 0
    current_step = 'AAA'

    while current_step != 'ZZZ':
        for p in pattern:
            current_step = mapping[current_step][int(p)]
            step_count += 1

    print(step_count)


def find_parallel_step_count(string):
    pattern, mapping = parse_input(string)
    step_counts = []
    start_nodes = [key for key in mapping.keys() if key[2] == 'A']

    for n in start_nodes:
        step_count = 0
        current_step = n

        while current_step[2] != 'Z':
            for p in pattern:
                current_step = mapping[current_step][int(p)]
                step_count += 1

        step_counts.append(step_count)

    print(lcm(step_counts))


if __name__ == '__main__':
    find_step_count(data)
    find_parallel_step_count(data)
