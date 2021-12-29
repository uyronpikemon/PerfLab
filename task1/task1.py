import sys

def _roll(_array, _m):
    for k in range(_m - 1):
        temp = _array[0]
        for j in range(len(_array) - 1):
            _array[j] = _array[j + 1]
        _array[len(_array) - 1] = temp
    
    return _array

if __name__ == '__main__':
    n = int(sys.argv[1])
    m = int(sys.argv[2])

    a = []
    for i in range(n):
        a.append(i + 1)

    s = str(a[0])
    b = _roll(a, m)

    while b[0] != 1:
        s += str(b[0])
        b = _roll(b, m)

    print(s)
