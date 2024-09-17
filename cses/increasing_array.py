def main():
    n = int(input())
    numbers = list(map(int, input().split(" ")))

    idx = 1
    moves = 0
    while idx < n:
        prev, current = numbers[idx - 1], numbers[idx]
        if current <= prev:
            moves += prev - current
            numbers[idx] = prev
        idx += 1
    print(moves)

if __name__ == "__main__":
    main()