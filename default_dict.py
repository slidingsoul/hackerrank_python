from collections import defaultdict

size_group_a, size_group_b = map(int, input().split())
group_a = []
group_b = []
for a in range(size_group_a):
  current_a = input()
  group_a.append(current_a)
for b in range(size_group_b):
  current_b = input()
  group_b.append(current_b)

for index_b, value_b in enumerate(group_b):
  found = False
  for index_a, value_a in enumerate(group_a):
    if value_b == value_a:
      found = True
      print(index_a + 1, end=" ")
  if not found:
    print("-1", end="")
  if index_b < len(group_b) - 1:
    print()