# nested lists

students = []
result = []

n = int(input())

for _ in range(n):
  name = input()
  score = float(input())
  students.append([name, score])
  
lowest = min([student[1] for student in students])
second_lowest = min([student[1] for student in students if student[1] != lowest])

for i in range(n):
  if students[i][1] == second_lowest:
    result.append(students[i][0])
result = sorted(result)
for student in result:
  print(student)