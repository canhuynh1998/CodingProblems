def main():
  t = int(input())
  for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    max_score = 0
    for _ in range(n-1):
      max_score += max(a) - min(a)
    print(max_score)

if __name__ == "__main__":
  main()