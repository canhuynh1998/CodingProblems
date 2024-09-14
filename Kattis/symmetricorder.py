def main():
    set_numbers = 1

    while True:
        length = int(input())

        if length == 0:
            break
        print(f'SET {set_numbers}')

        strings = [""] * length

        idx = 0
        front, back = 0, length - 1

        while idx < length:
            current = input()
            if idx % 2 == 0:
                strings[front] = current
                front += 1
            else:
                strings[back] = current
                back -= 1
            idx += 1
        set_numbers += 1
        for s in strings:
            print(s)


if __name__ == "__main__":
    main()