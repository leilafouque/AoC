def read_input(filename):
    list1 = []
    list2 = []
    with open(filename, 'r') as f:
        for line in f:
            ab = line.split()
            a = ab[0]
            b = ab[1]
            list1.append(int(a))
            list2.append(int(b))
    return list1, list2

if __name__ == "__main__":
    list1, list2 = read_input("/Users/lfouque/Documents/advent2024/day1_1.txt")
    list1.sort()
    list2.sort()
    diff = 0
    for a, b in zip(list1, list2):
        diff += abs(a - b)

    print(diff)

    similarity = 0
    for a in list1:
        num_occ = 0
        for b in list2:
            if b > a:
                break
            if b == a:
                num_occ += 1
        similarity += a * num_occ

    print(similarity)