def main():
    n = int(input())
    percentages = list(map(int, input().split(' ')))
    print((sum(percentages) / n))
if __name__ == "__main__":
    main()
