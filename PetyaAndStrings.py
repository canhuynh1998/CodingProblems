"""
Little Petya loves presents. His mum bought him two strings of the same size for his birthday. The strings consist of uppercase and lowercase Latin letters. Now Petya wants to compare those two strings lexicographically. The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter. Help Petya perform the comparison.

Input
Each of the first two lines contains a bought string. The strings' lengths range from 1 to 100 inclusive. It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.

Output
If the first string is less than the second one, print "-1". If the second string is less than the first one, print "1". If the strings are equal, print "0". Note that the letters' case is not taken into consideration when the strings are compared.

"""

def main():
    str1 = input().lower()
    count1 = 0
    str2 = input().lower()
    count2 = 0
    for idx, c1 in enumerate(str1):
        c2 = str2[idx]
        if c1 == c2:
            continue
        elif ord(c1) > ord(c2):
            print("1")
            return
        else:
            print("-1")
            return
    print("0")

if __name__ == "__main__":
    main()