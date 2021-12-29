import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        co = file.readline()
        d = float(file.readline())
    co = list(map(float, co.split()))
    t = []
    with open(sys.argv[2]) as file:
        for line in file:
            t.append(list(map(float, line.split())))

    for i in range(len(t)):
        g = ((t[i][0] - co[0])**2 + (t[i][1] - co[1])**2)**(1/2)
        if g == d:
            print("{} - точка лежит на окружности".format(i))
        else:
            if g > d:
                print("{} - точка снаружи".format(i))
            else:
                print("{} - точка внутри".format(i))
