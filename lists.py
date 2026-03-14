N = int(input())
arr = []

for _ in range(N):
  command = input().split()
  match command[0]:
    case "insert":
      index = int(command[1])
      value = int(command[2])
      arr.insert(index, value)
    case "print":
      print(arr)
    case "remove":
      index = arr.index(int(command[1]))
      arr.pop(index)
    case "append":
      arr.append(int(command[1]))
    case "sort":
      arr.sort()
    case "pop":
      arr.pop()
    case "reverse":
      arr.reverse()