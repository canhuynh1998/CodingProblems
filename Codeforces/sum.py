def main():
    cases = int(input())

    for _ in range(cases):
        case = input().split()
        a, b, c = int(case[0]), int(case[1]), int(case[2])
        if a+b == c or b+a == c or a+c == b or c+a == b or b+c == a or c+a==b:
            print("YES")
        else:
            print("NO")
if __name__ == "__main__":
    main()