def main():
    t = int(input())

    for _ in range(t):
        n, k = list(map(int, input().split(" ")))
        leaves = (k * (2*n - k + 1)) // 2
        if leaves % 2 == 0:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()