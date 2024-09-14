def main():
    dna = input()

    length = 0

    start = 0

    idx = 0

    while idx < len(dna):
        start_char = dna[start]

        while idx < len(dna) and dna[idx] == start_char:
            idx += 1
        length = max(length, idx - start)
        start = idx
    print(length)
if __name__ == "__main__":
    main()