
def main():
    length = int(input())
    strings = input().split(" ")
    for i in range(len(strings)):
        for j in range(len(strings)):
            if i == j:
                continue
            current = strings[i] + strings[j]
            if len(current) != length:
                continue
            if is_palidrome(current):
                print("YES")
                return
                
    print("NO")
def is_palidrome(string):
    front, back = 0, len(string) - 1

    while front < back:
        if string[front] != string[back]:
            return False
        front += 1
        back -= 1
    return True
if __name__ == "__main__":
    tests = int(input())
    for _ in range(tests):
        main()