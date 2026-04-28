import math

def print_rangoli(size: int):
  characters = [chr(x) for x in range(97, 97 + size)]
  longest_width = 3 * (size - 1) + size
  for i in range(1, size + 1):
    current = size
    end = (2 * i) - 1
    mid = math.ceil(end // 2) - 1
    letters = []
    for j in range(end):
      letters.append(str(characters[current - 1]))
      if j <= mid:
        current -= 1
      elif j > mid:
        current += 1
    print("-".join(letters).center(longest_width, "-"))
  for i in range(size - 1, 0, -1):
    current = size
    end = (2 * i) - 1
    mid = math.ceil(end // 2) - 1
    letters = []
    for j in range(end):
      letters.append(str(characters[current - 1]))
      if j <= mid:
        current -= 1
      elif j > mid:
        current += 1
    print("-".join(letters).center(longest_width, "-"))