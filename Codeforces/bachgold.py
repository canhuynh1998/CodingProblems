def main():
    n = int(input())
    k = n // 2
    print(k)
    if n % 2 == 0:
        print(' '.join(map(str,[2] * k)))
    else:
        print(f'{" ".join(map(str, [2] * (k - 1)))} 3')


if __name__ == "__main__":
    main()