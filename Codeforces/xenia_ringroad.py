def main():
    n, m = list(map(int, input().split(" ")))
    tasks = list(map(int, input().split(" ")))

    finished = 0
    time = 0
    idx = 0
    current_house = 1
    while finished < m:
        target_house = tasks[idx] 
        time += target_house - current_house if target_house - current_house >= 0 else target_house - current_house + n
        current_house = target_house
        finished += 1
        idx += 1
    print(time)

if __name__ == "__main__":
    main()