def main():
    read = open("pails.in")
    x, y, m = list(map(int, read.readline().split(" ")))
    max_amount = 0

    for i in range(m + 1):
        if x * i > m:
            break
        for j in range(m + 1):
            new_units = x * i + y * j
            if new_units > m:
                break
            max_amount = max(max_amount, new_units)
    
    with open("pails.out","w+") as f:
        print(max_amount, file=f)    


if __name__ == "__main__":
    main()
