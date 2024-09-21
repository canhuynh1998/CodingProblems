def main():
    number = int(input())
    found = False
    for i in range(1, number + 1):
        is_lucky = True
        current_num = i
        while current_num > 0:
            current_digit =  current_num % 10
            if current_digit != 4 and current_digit != 7:
                is_lucky = False
                break
            current_num //= 10
        
        if is_lucky and number % i == 0:
            found = True
            break
    if found: print("YES")
    else: print("NO")


if __name__ == "__main__":
    main()