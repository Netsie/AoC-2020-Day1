# Day1_Puzzle_Input.txt is a text file with the list of numbers provided for the puzzles

# Advent of Code, Day 1, Puzzle 2:

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
    for k in range (j+1, n):
      count = int(out[i]) + int(out[j]) + int(out[k])
      if count == 2020:
        break
    if count == 2020:
      break
  if count == 2020:
      break
      
no1 = int(out[i])
no2 = int(out[j])
no3 = int(out[k])

count = int(out[i]) + int(out[j]) + int(out[k])
print(f'{no1} + {no2} + {no3} = {count}')

product = int(out[i]) * int(out[j]) * int(out[k])
print(f'{no1} * {no2} * {no3}= {product}')
