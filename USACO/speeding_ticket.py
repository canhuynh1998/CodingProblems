def main():
    read = open("speeding.in")
    n, m = list(map(int, read.readline().split(" ")))
    rs = []

    for _ in range(n):
        r, s = list(map(int, read.readline().split(" ")))
        rs.append((r, s))
    
    bes = []
    for _ in range(m):
        br, bs = list(map(int, read.readline().split(" ")))
        bes.append((br, bs))
    idx1, idx2 = 0, 0
    max_speed = 0

    while idx1 < len(rs) and idx2 < len(bes):
        segment, speed_limit = rs[idx1]
        journey, speed_actual = bes[idx2]
        if speed_actual > speed_limit:

            max_speed = max(max_speed, speed_actual - speed_limit)
        
        if segment > journey:
            idx2 += 1
        elif segment < journey:
            idx1 += 1
        else:
            idx1 += 1
            idx2 += 1


    with open("speeding.out","w+") as f:
        print(max_speed, file=f)    


if __name__ == "__main__":
    main()
