import sys

def count(arr, to):
    w = 0
    for k in arr:
        w += abs(k - to)
    return w

if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        a = []
        for line in file:
            a.append(int(line.rstrip()))

    res = []
    for i in range(min(a), max(a)):
        res.append(count(a, i))

    print(min(res))
