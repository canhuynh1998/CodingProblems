def main():
    n = int(input())
    number = []

    for i in range(n):
        number.append(input())

    for i in reversed(range(len(number))):
        print(number[i])

if __name__ == "__main__":
    main()