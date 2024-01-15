from input import data
from time import sleep


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
    step_count = 0
    # current_steps = [key for key in mapping.keys() if key[2] == 'A']
    # while not all(s == 'ZZZ' for s in current_steps):
    #     print(current_steps)
    #     for p in pattern:
    #         current_steps = [mapping[step][int(p)] if step != 'ZZZ' else 'ZZZ' for step in current_steps]
    #         step_count += 1
    #
    # print(step_count)
    # print(current_steps)
    current_step = [key for key in mapping.keys() if key[2] == 'A'][2]

    while current_step != 'ZZZ':
        for p in pattern:
            print(p)
            current_step = mapping[current_step][int(p)]
            print(current_step)
            step_count += 1

    print(step_count)

if __name__ == '__main__':
    # find_step_count(data)
    find_parallel_step_count(data)
