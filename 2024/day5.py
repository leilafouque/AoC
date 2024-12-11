
import math

def read_input(filename):
    with open(filename, 'r') as f:
        return [line.rstrip() for line in f]
    

def build_order(puzzle_input):
    ordering = {}
    for order in puzzle_input:
        pages = order.split('|')
        if pages[1] in ordering:
            ordering[pages[1]].append(pages[0])
        else:
            ordering[pages[1]] = [pages[0]]
    return ordering

if __name__ == "__main__":
    puzzle_input_order = read_input("/Users/lfouque/Documents/advent2024/day5_1.txt")
    puzzle_input_updates = read_input("/Users/lfouque/Documents/advent2024/day5_2.txt")

    ordering = build_order(puzzle_input_order)

    result = 0
    to_reorder = []
    for update in puzzle_input_updates:
        pages = update.split(",")
        wrong_order = False
        for x in range(len(pages)):
            for y in range(x+1, len(pages)):
                if pages[x] in ordering and pages[y] in ordering[pages[x]]:
                    wrong_order = True
                    break
        if not wrong_order:
            result += int(pages[math.floor(len(pages) / 2)])
        else:
            to_reorder.append(update)
    print(result)

    result = 0
    re_ordered = []
    for bad in to_reorder:
        pages = bad.split(",")
        for x in range(len(pages)):
            for y in range(x+1, len(pages)):
                if pages[x] in ordering and pages[y] in ordering[pages[x]]:
                    value = pages[y]
                    pages.pop(y)
                    pages.insert(x, value)
        result += int(pages[math.floor(len(pages) / 2)])

    print(result)
    