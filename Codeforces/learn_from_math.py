def main():
    number = int(input())

    is_prime = [True for _ in range(number + 1)]
    is_prime[0] = is_prime[1] = False

    for i in range(2, len(is_prime)):
        if is_prime[i] and i*i <= number:
            for j in range(i*i, number + 1):
                is_prime[j] = False
    print(is_prime)


if __name__ == "__main__":
    main()