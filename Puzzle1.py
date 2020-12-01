# Day1_Puzzle_Input.txt is a text file with the list of numbers provided for the puzzles

# Advent of Code, Day 1, Puzzle 1: 

f = open("Day1_Puzzle_Input.txt", "r")
out = []
n = 0

while True:
  line = f.readline()
  n = n + 1
  if not line:
    n = n - 1
    break;
  out.append(line.strip())
  
f.close()

for i in range(0, n):
  for j in range(i+1, n):
    count = int(out[i]) + int(out[j])
    if count == 2020:
      break
  if count == 2020:
    break
      
no1 = int(out[i])
no2 = int(out[j])

count = int(out[i]) + int(out[j])
print(f'{no1} + {no2} = {count}')

product = int(out[i]) * int(out[j])
print(f'{no1} * {no2} = {product}')
