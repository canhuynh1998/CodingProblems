def main():
    read = open("lostcow.in")
    x, y = list(map(int, read.readline().split(" ")))
    distance = 0
    jump = 1

    position = x

    while position < y:
        next_pos = x + jump
        distance += abs(next_pos - position)
        position = next_pos
        jump *= -2
    if position > y:
        distance -= (position - y)
    with open("lostcow.out","w") as f:
        print(distance, file=f)

if __name__ == "__main__":
    main()
