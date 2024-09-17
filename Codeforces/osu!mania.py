def main():
    n = int(input())

    for _ in range(n):
        row = int(input())
        result = []
        for _ in range(row):
            line = input()
            for idx, c in enumerate(line):
                if c == "#":
                    result.append(idx+1)
        while result:
            print(result.pop(), end=" ")
if __name__ == "__main__":
    main()
