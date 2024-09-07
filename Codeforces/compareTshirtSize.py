
def main():
    lines = int(input())
    for _ in range(lines):
        string = input().split(" ")
        if string[0][-1] == "S":
            if string[1][-1] != "S":
                print("<")
            else:
                if len(string[0][:-1]) > len(string[1][:-1]):
                    print("<")
                elif len(string[0][:-1]) < len(string[1][:-1]):
                    print(">")
                else:
                    print("=")
        elif string[0][-1] == "M":
            if string[1][-1] == "S":
                print(">")
            elif string[1][-1] == "L":
                print("<")
            else:
                print("=")
        else:
            if string[1][-1] == "S" or string[1][-1] == "M":
                print(">")
            else:
                if len(string[0][:-1]) > len(string[1][:-1]):
                    print(">")
                elif len(string[0][:-1]) < len(string[1][:-1]):
                    print("<")
                else:
                    print("=")
    
    
if __name__ == "__main__":
    main()