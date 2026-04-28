def doormat(n, m):
  HYPHEN = "-"
  TRIANGLE = ".|."
  WELCOME = "WELCOME"
  for i in range(1, n // 2 + 1):
    triangle_length = (2 * i - 1)
    hyphens_length = (m - (3 * triangle_length)) // 2
    hyphens = HYPHEN * hyphens_length
    triangles = TRIANGLE * triangle_length
    print(f"{hyphens}{triangles}{hyphens}")
  print(WELCOME.center(m, "-"))
  for i in range(n // 2, 0, -1):
    triangle_length = (2 * i - 1)
    hyphens_length = (m - (3 * triangle_length)) // 2
    hyphens = HYPHEN * hyphens_length
    triangles = TRIANGLE * triangle_length
    print(f"{hyphens}{triangles}{hyphens}")

if __name__ == "__main__":
  first_multiple = input()
  n, m = tuple(map(int, first_multiple.split()))
  doormat(n, m)