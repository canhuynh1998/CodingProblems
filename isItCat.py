def main():
    length = int(input())
    string = input().lower()
    compressed = []
    for idx in range(1, len(string)):
        prev = string[idx - 1]
        current = string[idx]
        if prev != current:
            compressed.append(prev)
    compressed.append(string[-1])
    joined_string = ''.join(compressed)
    result = "YES" if joined_string == "meow" else "No"

    print(result)

if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        main()