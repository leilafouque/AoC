import re

def read_input(filename):
    with open(filename, 'r') as f:
        return f.read()

def mul(extracts):
    reg_num = re.compile('[0-9]{1,3}')
    result = 0
    for extract in extracts:
        nums = reg_num.findall(extract)
        result += int(nums[0]) * int(nums[1])
    return result

if __name__ == "__main__":
    puzzle_input = read_input("/Users/lfouque/Documents/advent2024/day3.txt")
    extracts = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)', puzzle_input)
    result = mul(extracts)
    print(result)

    result = 0
    dos = re.split('do\(\)', puzzle_input)
    for do in dos:
        dont = re.split("don't\(\)", do)
        do = dont[0]
        extracts = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)', do)
        result += mul(extracts)
    print(result)