def main():
    read = open("shell.in")
    n = int(read.readline())
    points = 0
    guesses = [0, 0, 0]
    shells = [i for i in range(3)]
    for _ in range(n):
        a, b, g = list(map(int, read.readline().split(" ")))
        shells[a-1], shells[b-1] = shells[b-1], shells[a-1]
        guesses[shells[g-1]] += 1
    points = max(guesses)
    with open("shell.out","w") as f:
        print(points, file=f)


if __name__ == "__main__":
    main()