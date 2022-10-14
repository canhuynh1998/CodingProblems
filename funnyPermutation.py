def main():
    tests = int(input())

    for _ in range(tests):
        current = int(input())
        per = []
        if current == 3:
            print("-1")
            continue
        for i in reversed(range(1, current + 1)):
            if i % 2 == 0:
                per.append(str(i-1))
            else:
                per.append(str(i))

        string = " ".join(per)
        print(string)
    
    
if __name__ == "__main__":
    main()