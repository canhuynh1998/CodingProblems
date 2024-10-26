def main():
  t = int(input())

  for _ in range(t):
    n = int(input())
    if n % 2 == 0:
      print("Sakurako")
    else:
      print("Kosuke")
  
if __name__ == "__main__":
  main()