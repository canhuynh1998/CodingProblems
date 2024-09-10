def main():
    n = int(input())
    for _ in range(n):
        sentence = []
        line = input()
        for idx in range(len(line)):
            if idx == 0:
                sentence.append(line[0].upper())
            elif line[idx] == " ":
                sentence.append(line[idx])
            else:
                sentence.append(line[idx].lower())
        print(''.join(sentence))

if __name__ == "__main__":
    main()