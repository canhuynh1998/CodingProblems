def main():
    n = int(input())
    numbers = list(map(int, input().split(" ")))

    total = n * (n + 1) // 2

    print(total - sum(numbers))

if __name__ == "__main__":
    main()