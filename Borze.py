"""
Ternary numeric notation is quite popular in Berland. To telegraph the ternary number the Borze alphabet is used. Digit 0 is transmitted as «.», 1 as «-.» and 2 as «--». You are to decode the Borze code, i.e. to find out the ternary number given its representation in Borze alphabet.

Input
The first line contains a number in Borze code. The length of the string is between 1 and 200 characters. It's guaranteed that the given string is a valid Borze code of some ternary number (this number can have leading zeroes).

Output
Output the decoded ternary number. It can have leading zeroes.
"""
def main():
    string = input()
    if len(string) == 1:
        print("0")
        return
    idx = 0
    result = []

    while idx < len(string):
        current_char = string[idx]
        if current_char == ".":
            result.append("0")
            idx += 1
        elif current_char == "-":
            next_char = string[idx+1]
            if next_char == "-":
                result.append("2")
            else:
                result.append("1")
            idx += 2
    print("".join(result))
    return


if __name__ == "__main__":
    main()