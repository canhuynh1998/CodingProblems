def main():
    t = int(input())
    for _ in range(t):
        _, k = list(map(int, input().split(" ")))
        people = list(map(int, input().split(" ")))
        given = 0
        taken = 0
        for a in people:
            if a == 0 and taken > 0:
                given += 1
                taken -= 1
            elif a >= k:
                taken += a
        print(given)


if __name__ == "__main__":
    main()