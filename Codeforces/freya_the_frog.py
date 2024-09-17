import math
def main():
    n = int(input())

    for _ in range(n):
        x, y, k = list(map(int, input().split(" ")))
        a = math.ceil(x / k)
        b = math.ceil(y / k)

        if a <= b:
            print(2 * b)
        else:
            print(2 * a - 1)


if __name__ == "__main__":
    main()