def main():
  t = int(input())

  for _ in range(t):
    n = int(input())
    prelimeter = 0
    prev_w, prev_h = -1, -1
    for _ in range(n):
      w, h = list(map(int, input().split(" ")))
      prev_h = max(prev_h, h)
      prev_w = max(prev_w, w)
    print(2 * (prev_h + prev_w))
if __name__ == "__main__":
  main()