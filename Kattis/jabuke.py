def main():
    x1, y1 = list(map(int, input().split(" ")))
    x2, y2 = list(map(int, input().split(" ")))
    x3, y3 = list(map(int, input().split(" ")))
    area = compute_area(x1, y1, x2, y2, x3, y3)
    n = int(input())

    count = 0

    for _ in range(n):
        x, y = list(map(int, input().split(" ")))
        area1 = compute_area(x, y, x2, y2, x3, y3)
        area2 = compute_area(x1, y1, x, y, x3, y3)
        area3 = compute_area(x1, y1, x2, y2, x, y)

        if area1 + area2 + area3 == area:
            count += 1
        
    print(area)
    print(count)

def compute_area(x1, y1, x2, y2, x3, y3):
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2


if __name__ == "__main__":
    main()