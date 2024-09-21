import math
def main():
    n = int(input())
    pages = list(map(int, input().split(" ")))

    page_per_week = sum(pages)
    week_to_finish = math.ceil(n / page_per_week)
    remaining = n - page_per_week * week_to_finish
    read = 0
    finished = False
    for _ in range(week_to_finish):
        if finished:
            break
        for idx, page in enumerate(pages):
            read += page
            if read >= n:
                print(idx + 1)
                finished = True
                break
if __name__ == "__main__":
    main()