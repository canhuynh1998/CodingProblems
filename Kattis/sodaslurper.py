def main():
    e, f, c = list(map(int, input().split(" ")))
    total = e + f

    bought = 0
    while total >= c:
       temp = total
       total //= c
       bought += total

       total += (temp % c)

    print(bought)


if __name__ == "__main__":
    main()