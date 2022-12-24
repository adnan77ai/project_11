import random
def num():
  number = random.randint(1,90)
  return number

digit = []
for i in range(8):
 digit.append(num())
 digit.sort()

bingo = [[digit[1], digit[5], digit[3]],
         [digit[7], 'BINGO', digit[2]],
         [digit[0], digit[4], digit[6]]]

def prettyprint():
  for row in bingo:
     print(row)
prettyprint()


  