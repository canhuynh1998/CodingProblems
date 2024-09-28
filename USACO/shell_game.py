def main():
    read = open("shell.in")
    n = int(read.readline())
    points = 0
    for _ in range(n):
        a, b, g = list(map(int, read.readline().split(" ")))
        if g == a or g == b:
            points += 1
    print(points, file=open("shell.out","w"))


if __name__ == "__main__":
    main()