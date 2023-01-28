def count (lst):
  even = 0
  odd = 0 
  for i in lst:
    if i%2 ==0:
      even += 1
    else:
      odd += 1
  return even, odd
lst = [25, 20, 26, 88, 6, 50, 57, 80]
even, odd = count(lst)
print (f'Even:{even} and Odd:{odd}') 
