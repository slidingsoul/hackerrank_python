def print_formatted(number):
  padding = len(f"{number:b}")
  for num in range(1, number + 1):
    number = f"{num}".rjust(padding)
    octal = f"{num:o}".rjust(padding)
    hexa = f"{num:X}".rjust(padding)
    binary = f"{num:b}".rjust(padding)
    print(f"{number} {octal} {hexa} {binary}")

print_formatted(17)