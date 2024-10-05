def main():
    read = open("cowsignal.in")

    m, n, k = list(map(int, read.readline().split(" ")))
    result = []
    for _ in range(m):
        current_string = list(read.readline())
        current_line = []

        for c in current_string:
            if c == "\n":
                continue
            current_line.append(c * k )
        
        line = ''.join(current_line)
        result+=[line]*k
    with open("cowsignal.out","w+") as f:
        for l in result:
            print(l, file=f)


if __name__ == "__main__":
    main()
