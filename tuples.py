if __name__ == "__main__":
  n = input()
  arr = map(int, input().split())
  tupl = tuple(arr)
  print(hash(tupl))