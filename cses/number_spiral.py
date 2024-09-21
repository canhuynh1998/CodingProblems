def main():
    n = int(input())

    for _ in range(n):
        y, x = list(map(int, input().split(" ")))
        if y > x:
            inner_square = ( y - 1) * ( y - 1)
            if y % 2 == 0:
                print(inner_square + 2 * y - x)
            else:
                print(inner_square + x)
        else:
            inner_square = (x - 1) * (x-1)
            if x % 2 == 0:
                print(inner_square + y)
                
            else:
                print(inner_square + 2 * x - y)

if __name__ == "__main__":
    main()