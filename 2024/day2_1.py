def read_input(filename):
    reports = []
    with open(filename, 'r') as f:
        for line in f:
            levels = line.split()
            reports.append(levels)
    return reports

if __name__ == "__main__":
    reports = read_input("/Users/lfouque/Documents/advent2024/day2_1.txt")
    safe_reports = 0
    for levels in reports:
        order = 0
        safe = True
        for x in range(len(levels)-1):
            diff = int(levels[x]) - int(levels[x+1])
            if diff == 0 or abs(diff) > 3:
                safe = False
                break
            if order == 0:
                if diff > 0:
                  order = 1
                else:
                  order = -1
            else:
                if order == 1 and diff < 0:
                    safe = False
                    break
                elif order == -1 and diff > 0:
                    safe = False
                    break
        if safe:
            safe_reports += 1

    print(safe_reports)