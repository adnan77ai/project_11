import os, time
todo = []
def add():
  time.sleep(1)
  os.system('clear')
  Name = input ('Name> ')
  Date = input ('Date> ')
  Priority = input ('Priority> ')
  row = [Name, Date, Priority]
  todo.append(row)
  print ('added')
def view():
  time.sleep(1)
  os.system('clear')
  option = input ('1: All\n2: By priority\n')
  if option == '1':
    for row in todo:
      for item in row:
        print (item, end = ' | ')
      print ()
    print()
  else:
    user = input('what priority> ')
    for row in todo:
      if user in row:
        for item in row:
          print (item, end = ' | ') 
        print()
    print()
def edit():
  time.sleep(1)
  os.system('clear')
  find = input('Name of todo to edit\n')
  found = False
  for row in todo:
    if find in row:
      found = True
    if not found:
      print ("Coudn't find that")
      return
  for row in todo:
    if find in row:
      todo.remove(row)
  name = input ('Name> ')
  date = input ('Date> ')
  priority = input ('Priority> ')
  row = [name, date, priority]
  todo.append(row)
  print ('Successfully edited!')
def remove():
  time.sleep(1)
  os.system('clear')
  find = input('Name of todo to remove\n')
  for row in todo:
    if find in row:
      todo.remove(row)
      print('Row removed')

while True:
  user = input ('1:Add\n2:View\n3:Remove\n4:Edit\n')
  if user == '1':
    add()
  if user == '2':
    view()
  if user == '3':
    remove()
  if user == '4':
    edit()
  time.sleep(1)
  os.system('clear')
