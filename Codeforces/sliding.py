def main():
  t = int(input())


  for _ in range(t):
    n, m, r, c = list(map(int, input().split(" ")))
    move_up = n - r
    move_up_distance = m
    affected_people = (n - r) * m  + (m - c)
    print(affected_people - move_up + move_up * move_up_distance)

if __name__ =="__main__":
  main()