def main():
    read = open("speeding.in")
    n, m = list(map(int, read.readline().split(" ")))
    rs = []

    for _ in range(n):
        r, s = list(map(int, read.readline().split(" ")))
        rs += [s] * r
    
    bes = []
    for _ in range(m):
        br, bs = list(map(int, read.readline().split(" ")))
        bes += [bs] * br
    max_speed = 0
    for idx, road in enumerate(rs):
        max_speed = max(max_speed, bes[idx] - road)

    with open("speeding.out","w+") as f:
        print(max_speed, file=f)    


if __name__ == "__main__":
    main()
