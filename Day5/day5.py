

def decriptBordingPass(data):
  columnData = list(data[:6])
  rowData = list(data[7:])

  maxCol = 128
  maxRow = 8

  col = -1
  row = -1

  minRowPos = 1
  maxRowPos = maxRow

  for item in rowData:
    if item == 'R':
      maxRowPos = (maxRowPos - minRowPos) / 2
      print('Max')
      print(maxRowPos)
    if item == 'L':
      minRowPos = minRowPos + ((maxRowPos - minRowPos) / 2)
      print('Min')
      print(minRowPos)

  print(minRowPos)
  print(maxRowPos)