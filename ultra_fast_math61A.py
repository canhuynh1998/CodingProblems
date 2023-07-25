def main():
    num1 = input()
    num2 = input()

    result = []

    for idx, c1 in enumerate(num1):
        c2 = num2[idx]
        if c1 == c2 :
            result.append('0')
        else:
            result.append('1')
    print(''.join(result))
if __name__ == "__main__":
    main()