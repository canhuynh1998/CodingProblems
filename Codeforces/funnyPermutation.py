def main():
    tests = int(input())

    for _ in range(tests):
        current = int(input())
        per = []
        if current == 3:
            print(-1)
            continue
            
        for i in range(3, current + 1):
            per.append(str(i))
        per += ["2","1"]
        string = " ".join(per)
        print(string)
    
    
if __name__ == "__main__":
    main()