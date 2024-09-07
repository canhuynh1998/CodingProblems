def main():
    cases = int(input())

    for _ in range(cases):
        arrayLength = int(input())
        array = input().split()
        unique = set()

        for i in array:
            unique.add(i)
        if len(unique) == arrayLength:
            print("YES")
        else:
            print("NO")
if __name__ == "__main__":
    main()