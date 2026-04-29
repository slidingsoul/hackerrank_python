from collections import Counter

def moneyEarned(shoe_sizes: list[int], purchases: list[(int, int)]):
  sizes_quantities = Counter(shoe_sizes)
  revenue = 0
  for size, price in purchases:
    if size in sizes_quantities:
      revenue += price
      sizes_quantities[size] -= 1
      if sizes_quantities[size] == 0:
        sizes_quantities.pop(size, None)
  return revenue

shoes = int(input())
first_multiple_input = input()
shoe_sizes = list(map(int, first_multiple_input.split()))
customers = int(input())
purchases = []
for i in range(customers):
  second_multiple_input = input()
  purchase = list(map(int, second_multiple_input.split()))
  purchases.append(purchase)
print(moneyEarned(shoe_sizes, purchases))