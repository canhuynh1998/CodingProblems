"""
One day Vasya painted a Cartesian coordinate system on a piece of paper and marked some set of points (x1, y1), (x2, y2), ..., (xn, yn). Let's define neighbors for some fixed point from the given set (x, y):

point (x', y') is (x, y)'s right neighbor, if x' > x and y' = y
point (x', y') is (x, y)'s left neighbor, if x' < x and y' = y
point (x', y') is (x, y)'s lower neighbor, if x' = x and y' < y
point (x', y') is (x, y)'s upper neighbor, if x' = x and y' > y
We'll consider point (x, y) from the given set supercentral, if it has at least one upper, at least one lower, at least one left and at least one right neighbor among this set's points.

Vasya marked quite many points on the paper. Analyzing the picture manually is rather a challenge, so Vasya asked you to help him. Your task is to find the number of supercentral points in the given set.

Input
The first input line contains the only integer n (1 ≤ n ≤ 200) — the number of points in the given set. Next n lines contain the coordinates of the points written as "x y" (without the quotes) (|x|, |y| ≤ 1000), all coordinates are integers. The numbers in the line are separated by exactly one space. It is guaranteed that all points are different.

Output
Print the only number — the number of supercentral points of the given set.
"""

def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = list(map(int, input().split(" ")))
        points.append((x, y))
    
    counts = 0
    
    for p1 in points:
        left = 0
        right = 0
        up = 0
        down = 0
        for p2 in points:
            if p1 == p2:
                continue
            if (p2[0] < p1[0] and p2[1] == p1[1]):
                left +=1
            if ( p2[0] > p1[0] and p2[1] == p1[1] ):
                right += 1
            if (p2[0] == p1[0] and p2[1] < p1[1]):
                down += 1
            
            if    (p2[0] == p1[0] and p2[1] > p1[1]):
                up += 1
        if left != 0 and right != 0 and up != 0 and down != 0:
            counts += 1
    print(counts)

if __name__ == "__main__":
    main()