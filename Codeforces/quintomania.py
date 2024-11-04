def main():
  t = int(input())

  for _ in range(t):
    n = int(input())

    number = list(map(int, input().split(" ")))
    valid = True
    for i in range(1, len(number)):
      prev, current = number[i - 1], number[i]

      if abs(current - prev) != 5 and abs(current - prev) != 7:
        valid = False
        break
    if valid:
      print("YES")
    else:
      print("NO")

if __name__ == "__main__":
  main()