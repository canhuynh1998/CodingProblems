def main():
    n = int(input())
    heights = list(map(int, input().split(' ')))
    max_idx, min_idx = len(heights) - 1, 0 
    max_val, min_val = max(heights), min(heights)
    for idx, h in enumerate(heights):
        if h == max_val:
            max_idx = min(max_idx, idx)
        if h == min_val:
            min_idx = max(min_idx, idx)
    if min_idx < max_idx:
        print(max_idx + (n - 1 - min_idx) - 1)
    else:
        print(max_idx + (n - 1 - min_idx))
if __name__ == "__main__":
    main()
