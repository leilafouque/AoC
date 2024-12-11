with open("/Users/lfouque/Documents/advent2024/day9.txt", 'r') as f:
    data = f.read()
    data.rstrip("\n")
    puzzle_input = list(data)
    print (data)

result = 0
input_index = 0
disk_index = 0
in_file = True
while input_index < len(puzzle_input):
    # print(input_index, in_file, puzzle_input)
    if (in_file):
        file_index = int(input_index / 2)
        file_len = int(puzzle_input[input_index])
        for _ in range(file_len):
            result += disk_index * file_index
            # print(disk_index, file_index)
            disk_index += 1
        in_file = False
        input_index +=1
    else:
        free_space = int(puzzle_input[input_index])
        file_len = int(puzzle_input[-1])
        file_index = int(len(puzzle_input) / 2)
        # print(free_space, file_len, file_index)
        if file_len <= free_space:
            for _ in range(file_len):
                result += disk_index * file_index
                # print(disk_index, file_index)
                disk_index += 1
            free_space -= file_len
            puzzle_input = puzzle_input[:-2]
        else:
            for _ in range(free_space):
                result += disk_index * file_index
                # print(disk_index, file_index)
                disk_index += 1
            puzzle_input[-1] = str(file_len - free_space)
            free_space = 0
        if free_space > 0:
            puzzle_input[input_index] = str(free_space)
        else:
            in_file = True
            input_index +=1
            
print(result)