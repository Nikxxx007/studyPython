def print_arr(a):
    for i in a:
        for line in i:
            print("{:^3}".format(line), end = " ")
        print("")


def found(pathArr, finPoint):
    weight = 1
    for i in range(len(pathArr) * len(pathArr[0])):
        weight += 1
        for y in range(len(pathArr)):
            for x in range(len(pathArr[y])):
                if pathArr[y][x] == (weight - 1):
                    if y > 0 and pathArr[y - 1][x] == 0:
                        pathArr[y - 1][x] = weight
                    if y < (len(pathArr) - 1) and pathArr[y + 1][x] == 0:
                        pathArr[y + 1][x] = weight
                    if x > 0 and pathArr[y][x - 1] == 0:
                        pathArr[y][x - 1] = weight
                    if x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == 0:
                        pathArr[y][x + 1] = weight
                    if (abs(y - finPoint[0]) + abs(x - finPoint[1])) == 1:
                        pathArr[finPoint[0]][finPoint[1]] = weight
                        return True
    return False

def print_path(pathArr, finPoint):
    res = []
    y = finPoint[0]
    x = finPoint[1]
    weight = pathArr[y][x]

    while (weight):
        weight -=1
        if y > 0 and pathArr[y - 1][x] == weight:
            res.append(x)
            res.append(y)
            y -= 1
        elif y < (len(pathArr) - 1) and pathArr[y + 1][x] == weight:
            y += 1
            res.append(x)
            res.append(y)
        elif x > 0 and pathArr[y][x - 1] == weight:
            x -= 1
            res.append(x)
            res.append(y)
        elif x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == weight:
            x += 1
            res.append(x)
            res.append(y)
    res = res[::-1]
    return res
            
    
def main():
    a = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    pozIn = (1, 1)
    pozOut = (2, 5)

    print("Maze: ")
    print_arr(a)
    
    # Fill array with -1 and step value
    path = [[x if x == 0 else -1 for x in y] for y in a]
    path[pozIn[0]][pozIn[1]] = 1

    if not found(path, pozOut):
        print("Path was not found!")
        return

    result = print_path(path, pozOut)
    result.insert(0, pozIn[0])
    result.insert(1, pozIn[1])
    result.append(pozOut[0])
    result.append(pozOut[1])
    # Print path
    print("Path: ")
    for i in range(0, len(result) - 1, 2):
        print(f'({result[i]};{result[i + 1]})', end=' ')
    print()


if __name__ == '__main__':
    main()