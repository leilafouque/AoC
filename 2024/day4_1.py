def read_input(filename):
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


lines = read_input("../../day4.txt")
width = len(lines[0])-1
height = len(lines)
print(width, height)
num_occ = 0
for line in lines:
    num_occ += line.count("XMAS")
    num_occ += line.count("SAMX")

columns = []
for x in range(width):
    column = ''
    for y in range(len(lines)-1,-1,-1):
        column += lines[y][x]
    columns.append(column)

for column in columns:
    num_occ += column.count("XMAS")
    num_occ += column.count("SAMX")

diagonals = []
for x in range(width):
    diag1 = ''
    diag2 = ''
    for y in range(height - x):
        diag1 += lines[y][x+y]
        diag2 += columns[y][x+y]
    diagonals.append(diag1)
    diagonals.append(diag2)

for x in range(1, height):
    diag1 = ''
    diag2 = ''
    for y in range(width - x):
        diag1 += lines[x+y][y]
        diag2 += columns[x+y][y]
    diagonals.append(diag1)
    diagonals.append(diag2)

for diag in diagonals:
    num_occ += diag.count("XMAS")
    num_occ += diag.count("SAMX")

print(num_occ)
