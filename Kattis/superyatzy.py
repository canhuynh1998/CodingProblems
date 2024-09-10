def main():
    n, m = list(map(int, input().split(" ")))
    if m == 0:
        print('Nej')
    else:
        counts = {}
        max_count = 0
        for _ in range(n):
            current_dice = int(input())
            if current_dice not in counts:
                counts[current_dice] = 0
            counts[current_dice] += 1
            max_count = max(counts[current_dice], max_count)
        result = "Ja" if n - max_count <= m else "Nej"
        print(result)

if __name__ == "__main__":
    main()