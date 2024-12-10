def read_input(filename):
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


lines = read_input("../../day4.txt")
width = len(lines[0])-1
height = len(lines)
num_occ = 0
for x in range(1,height-1):
    for y in range(1, width-1):
        if lines[x][y] == 'A':
            top = False
            bottom = False
            if (lines[x-1][y-1] == 'M' and lines[x+1][y+1] == 'S') or \
                (lines[x-1][y-1] == 'S' and lines[x+1][y+1] == 'M'):
                top = True
            if (lines[x+1][y-1] == 'M' and lines[x-1][y+1] == 'S') or \
                (lines[x+1][y-1] == 'S' and lines[x-1][y+1] == 'M'):
                bottom = True
            if top and bottom:
                num_occ += 1

print(num_occ)