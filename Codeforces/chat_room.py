def main():

    words = input()
    target = "hello"
    idx = 0
    
    for c in words:
        if idx < len(target) and c == target[idx]:
            idx += 1
    
    if idx == len(target):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()