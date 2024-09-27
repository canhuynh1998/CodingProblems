def main():
    numbers = int(input())
    
    hundreds = numbers // 100
    twenties = (numbers - hundreds * 100) // 20
    tens = (numbers - hundreds * 100 - twenties * 20) // 10
    fives = (numbers - hundreds * 100 - twenties * 20 - tens * 10) // 5
    ones = numbers - hundreds * 100 - twenties * 20 - tens * 10 - fives * 5
    
    print(hundreds + twenties + tens + fives + ones)

if __name__ == "__main__":
    main()