def main():
    numbers = input().split("+")
    
    ptr1, ptr2, ptr3 = 0, 0, len(numbers) - 1
    
    while ptr2 <= ptr3:
        if numbers[ptr2] == "1":
            numbers[ptr2], numbers[ptr1] =  numbers[ptr1], numbers[ptr2]
            ptr1 += 1
            ptr2 += 1
        elif numbers[ptr2] == "3":
            numbers[ptr2], numbers[ptr3] = numbers[ptr3], numbers[ptr2]
            ptr3 -= 1
        else:
            ptr2 += 1
    print('+'.join(numbers))

if __name__ == "__main__":
    main()