import re

# with open('test.txt') as f:
with open('passports.txt') as f:
  content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

def partOne():
  itemPerLine = []
  passports = []
  countOfValidPassports = 0

  for line in content:
    if line == '':
      itemPerLine.append(line)
    else:
      itemsInLine = line.split()
      for j in itemsInLine:
        j = j[:3]
        itemPerLine.append(j)

  tempHolder = []
  for item in itemPerLine:
    if item == '':
      passports.append(tempHolder)
      tempHolder = []
    else:
      tempHolder.append(item)

  passports.append(tempHolder)

  requiredFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

  for passport in passports:
    valid = True
    for field in requiredFields:
      if field not in passport:
        valid = False
    
    if valid == True:
      countOfValidPassports += 1

  print(countOfValidPassports)


def partTwo():

  itemPerLine = []
  passports = []
  countOfValidPassports = 0

  for line in content:
    if line == '':
      itemPerLine.append(line)
    else:
      itemsInLine = line.split()
      for j in itemsInLine:
        dataItem = []
        dataItem.append(j[:3])
        dataItem.append(j[4:])
        itemPerLine.append(dataItem)

  tempHolder = []
  for item in itemPerLine:
    if item == '':
      passports.append(tempHolder)
      tempHolder = []
    else:
      tempHolder.append(item)

  passports.append(tempHolder)

  for p in passports:
    state = validatePassport(p)
    if state == True:
      countOfValidPassports += 1

  print(countOfValidPassports)


def validatePassport(passport):

  requiredFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
  passportFields = []

  for item in passport:
    passportFields.append(item[0])

  fieldsValid = True

  for field in requiredFields:
    if field not in passportFields:
      fieldsValid = False
  
  if fieldsValid == False:
    return False
  else:
    valid = True
    for item in passport:

      if item[0] == 'byr':
        if len(item[1]) != 4 or int(item[1]) > 2002 or int(item[1]) < 1920:
          valid = False 

      if item[0] == 'iyr':
        if len(item[1]) != 4 or int(item[1]) > 2020 or int(item[1]) < 2010:
          valid = False 

      if item[0] == 'eyr':
        if len(item[1]) != 4 or int(item[1]) > 2030 or int(item[1]) < 2020:
          valid = False 

      if item[0] == 'hgt':
        hFormat = item[1][-2:]
        if hFormat != 'cm' and hFormat != 'in':
          valid = False
        else:
          hValue = int(item[1][:-2])
          if hFormat == 'cm':
            if hValue < 150 or hValue > 193:
              valid = False
          if hFormat == 'in':
            if hValue < 59 or hValue > 76:
              valid = False

      if item[0] == 'hcl':
        match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', item[1])
        if not match:
          valid = False
      
      if item[0] == 'ecl':
        colors = ['amb','blu','brn','gry','grn','hzl','oth']
        if item[1] not in colors:
          valid = False
      
      if item[0] == 'pid':
        if len(item[1]) != 9:
          valid = False

    if valid == True:
      return True
    else:
      return False