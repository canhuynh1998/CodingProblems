import math
"""
memory limit per test256 megabytes
Freya the Frog is traveling on the 2D coordinate plane. She is currently at point (0,0)
 and wants to go to point (𝑥,𝑦)
. In one move, she chooses an integer 𝑑
 such that 0≤𝑑≤𝑘
 and jumps 𝑑
 spots forward in the direction she is facing.

Initially, she is facing the positive 𝑥
 direction. After every move, she will alternate between facing the positive 𝑥
 direction and the positive 𝑦
 direction (i.e., she will face the positive 𝑦
 direction on her second move, the positive 𝑥
 direction on her third move, and so on).

What is the minimum amount of moves she must perform to land on point (𝑥,𝑦)
?

Input
The first line contains an integer 𝑡
 (1≤𝑡≤104
) — the number of test cases.

Each test case contains three integers 𝑥
, 𝑦
, and 𝑘
 (0≤𝑥,𝑦≤109,1≤𝑘≤109
).

Output
For each test case, output the number of jumps Freya needs to make on a new line.


NOTES: Counting the turning times
"""
def main():
    n = int(input())

    for _ in range(n):
        x, y, k = list(map(int, input().split(" ")))
        a = math.ceil(x / k)
        b = math.ceil(y / k)

        if a <= b:
            print(2 * b)
        else:
            print(2 * a - 1)


if __name__ == "__main__":
    main()