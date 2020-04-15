import math

def diamond(n):
  if n % 2 == 0 or n < 0:
    return None
  diamond = ''
  middleNum = math.floor(n/2)
  count = 0
  stars = 1
  spaces = middleNum
  while count < n:
    while count < middleNum:
      diamond += spaces*' ' + stars*'*'+'\n'
      stars += 2
      spaces -= 1
      count += 1
    diamond += spaces*' ' + stars*'*'+'\n'
    spaces += 1
    stars -=2
    count += 1
  return diamond
