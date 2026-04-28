def solve(s):
  s = s.title()
  s = list(s)
  for i in range(len(s) - 1, 0, -1):
    if s[i-1] != " " and s[i].isupper():
      s[i] = s[i].lower()
  return "".join(s)

print(solve("1 w 2 r 3g"))