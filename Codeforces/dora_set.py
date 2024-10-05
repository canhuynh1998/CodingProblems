def main():
    t = int(input())

    for _ in range(t):
        l, r = list(map(int, input().split(" ")))

        print(((r+1)// - (l)//2)//2)