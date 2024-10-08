def main():
    n = int(input())

    x = list(map(int, input().split(" ")))
    y = list(map(int, input().split(" ")))

    max_distance = 0
    for i in range(n):
        for j in range(i+1, n):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            square = dx * dx + dy * dy
            max_distance = max(max_distance, square)
    print(max_distance)

if __name__ == "__main__":
    main()