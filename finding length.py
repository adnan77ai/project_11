def count(names):
  more = 0
  less = 0
  for i in names:
    if len(i)>5:
      more += 1
    else: 
      less += 1
  return more, less

names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Jasmine"]

more, less = count(names)

print(f'More than Five:{more}\nLess than Five:{less}')


