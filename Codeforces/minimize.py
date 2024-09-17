def main():
    n = int(input())
    for _ in range(n):
        a, b = list(map(int, input().split(" ")))
        mid = (b - a + 1) // 2
        c = a + mid
        print((c-a) + (b-c))

if __name__ == "__main__":
    main()