"""
LANGUAGES
en
ja
sv
Krarkl wants to learn the birthdays of all his 
 friends, so he knows whom to congratulate each day. Unfortunately collisions sometimes arise, meaning several friends may have the same birthday. This may confuse Krarkl, so he decided to only remember the birthday of the friend he likes the most in case of a collision. Given a list of birthdays for each of his friends and how much Krarkl likes each friend, print what friends Krarkl will remember the birthday for.

Input
The first line of input contains an integer 
 (
), the number of friends.

Then 
 lines follow, one for each friend. The 
’th of these lines contains a string with the 
’th friend’s first name 
 (
 will be between 
 and 
 letters long), an integer 
 (
) denoting how much Krarkl likes the friend, and their birthday given in the format DD/MM (where DD is a day between 01 and 31, and MM is a month between 01 and 12). A higher value of 
 means that Krarkl likes that friend more.

The birthdays will be real dates during 2020 (a leap year), for example 28/02 for February 28. All names will consist only of small English letters (a-z) with a capital first letter (A-Z). All 
 will be distinct.

Output
On the first line, print an integer 
 – the number of friends whose birthdays Krarkl will remember.

This should be followed by 
 lines containing a single word each, the first names of the chosen friends, in lexicographical order.

Scoring
Your solution will be tested on a number of test case groups. To get the points for a group, you need to pass all test cases in the group.

Group

Points

Constraints






No further constraints

Explanation of samples
In the first sample, Sanna and Simon have the same birthday. Since Krarkl likes Sanna less than Simon (
), Krarkl will only remember Simon’s and Saga’s birthdays.

In the second sample, Krarkl has really bad luck and will miss half of his friends’ birthdays.

Notes: input is string
"""

def main():
    n = int(input())
    friends = {}

    for _ in range(n):
        current_friend = input().split(" ")
        if current_friend[2] not in friends:
            friends[current_friend[2]] = []
        friends[current_friend[2]].append((current_friend[0], int(current_friend[1])))

    result = []

    for  value in friends.values():
        friend_name = max(value, key=lambda x:x[1])[0]
        result.append(friend_name)

    result = sorted(result)
    print(len(result))
    for name in result:
        print(name)


if __name__ == "__main__":
    main()