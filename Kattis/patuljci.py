def main():
    numbers = []

    for _ in range(9):
        num = int(input())
        numbers.append(num)

    total = sum(numbers)
    target_to_element = total - 100
    seens = {}
    for idx, n in enumerate(numbers):
        potential = target_to_element - n
        if potential in seens:
            numbers[idx] = -numbers[idx]
            numbers[seens[potential]] = -numbers[seens[potential]]
        seens[n] = idx

    for idx in range(len(numbers)):
        if numbers[idx] < 0:
            continue
        print(numbers[idx])

if __name__ == "__main__":
    main()