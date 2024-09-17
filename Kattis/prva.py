# def main():
r, c = list(map(int, input().split(" ")))
strings = []
board = []
for _ in range(r):
    line = input()
    board.append(line)
    start = 0
    idx = 0
    blocked = 0
    while idx < len(line):
        if line[idx] == "#":
            if len(line[start:idx]) >= 2:
                strings.append(line[start:idx])
            start = idx + 1
            blocked += 1
        idx += 1
    if blocked == 0:
        strings.append(line)
    elif len(line[start:]) >= 2:
        strings.append(line[start:])

for col in range(c):
    current_string = board[0][col] if board[0][col] != "#" else ""
    idx = 1
    start = 0
    blocked = 0
    while idx < r:
        if board[idx][col] == "#":
            if len(current_string) >= 2:
                strings.append(current_string)
            current_string = ""
            start = idx + 1
            blocked += 1
        else:
            current_string += board[idx][col]
        idx += 1
    if blocked == 0:
        strings.append(current_string)
strings.sort()

print(strings[0])

# if __name__ == "__main__":
#     main()