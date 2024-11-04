import heapq
def main():
  t = int(input())

  for _ in range(t):
    n, k = list(map(int, input().split(" ")))
    shelves = {}
    for _ in range(k):
      brand, cost = list(map(int, input().split(" ")))
      if brand not in shelves:
        shelves[brand] = 0
      shelves[brand] += cost
    result = sorted(shelves.values(), reverse=True)[:n]
    print(sum(result))

if __name__ == "__main__":
  main()