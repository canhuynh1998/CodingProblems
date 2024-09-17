def main():
    n = int(input())
    if n == 2 or n == 3:
        print('NO SOLUTION')
    else:
        result = [0] * n
        idx = 0
        value = 2
        while value <= n and idx < n:
            result[idx] = value
            value += 2
            idx += 1
    
        value = 1
        while value <= n and idx < n:
            result[idx] = value
            value += 2
            idx += 1
        

        print(" ".join(map(str, result)))
if __name__ == "__main__":
    main()
