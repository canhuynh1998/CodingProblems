def main():
    number = int(input())

    five = number // 5
    four = (number - five * 5 ) // 4
    three = (number - five * 5 - four * 4 ) // 3
    two = (number - five * 5 - four * 4 - three * 3) // 2
    one = number - five * 5 - four * 4 - three * 3 - two * 2

    print(five + four + three + two + one)

if __name__ == "__main__":
    main()