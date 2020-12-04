with open('input.txt') as f:
  content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

targetSum = 2020
numbersPart1 = [0, 0]
numbersPart2 = [0, 0, 0]

# Part 1
for p1Item1 in content:
  for p1Item2 in content:
    if int(p1Item1) + int(p1Item2) == targetSum:
      numbersPart1[0] = p1Item1
      numbersPart1[1] = p1Item2

# Part 2
for p2Item1 in content:
  for p2Item2 in content:
    for p2Item3 in content:
      if int(p2Item1) + int(p2Item2) + int(p2Item3) == targetSum:
        numbersPart2[0] = p2Item1
        numbersPart2[1] = p2Item2
        numbersPart2[2] = p2Item3

# Print results
print('Part 1 => ', int(numbersPart1[0]) * int(numbersPart1[1]))
print('Part 2 => ', int(numbersPart2[0]) * int(numbersPart2[1]) * int(numbersPart2[2]))