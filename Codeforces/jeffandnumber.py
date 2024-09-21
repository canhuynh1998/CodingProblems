def main():
    n = int(input())
 
    numbers = list(map(int, input().split(" ")))
    
    counters = {5:0, 0:0}
    for num in numbers:
        counters[num] += 1
    print(counters)
    sum_five = 0
    max_five = 0
    for _ in range(counters[5]):
        sum_five += 5
        if sum_five % 9 == 0:
            max_five = max(max_five, sum_five)
    if max_five == 0:
        if counters[0] == 0:
            print(-1)
        else:
            print(0)
    else:
        if counters[0] == 0:
            print(-1)
        else:
            result = ['5'] * (max_five // 5) + ['0'] * counters[0]
            
            print(''.join(result))

if __name__ == "__main__":
    main()