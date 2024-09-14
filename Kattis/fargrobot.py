def main():
    n = int(input())
    command = input()

    result = ""
    idx = 0

    while idx < len(command) and n > 0:
        unique = set()
        
        while idx < len(command) and len(unique) < 3:
            unique.add(command[idx])
            idx += 1
        result += command[idx-1]
        n -= 1
    print(''.join(result))

if __name__ == "__main__":
    main()