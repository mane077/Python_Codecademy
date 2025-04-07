guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  while True:
    line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    n = yield name

guest_list = read_guestlist('guest_list.txt')

for i in range(1,11):
  print( i , ":" , next(guest_list))

#guest_list.send('Jane,35')
#print(next(guest_list))

guest_list.send('Jane,35')
guests["Jane"] = 35

for guest in guest_list:
  print(guest)

over_21 = (guest for guest in guests if guests[guest] > 21)
print(list(over_21), '\n')


# create 3 tables with 5 seats at each
def first_table():
  for i in range(1, 6):
    yield ("Chicken", "Table 1", "Seat {}".format(i))


def second_table():
  for i in range(1, 6):
    yield ("Beef", "Table 2", "Seat {}".format(i))


def third_table():
  for i in range(1, 6):
    yield ("Fish", "Table 3", "Seat {}".format(i))


# combine the list of tables
def tables():
  yield from first_table()
  yield from second_table()
  yield from third_table()

# create a function which yields a table
def assign_table(t):
  for table in t:
    yield table


# connected generator which assigns a table from each fn()
guest_table = assign_table(tables())


# yield the name along with a table for each guest
def assign_guest(guests, guest_table):
  i=0
  for guest in guests:
    yield i+1 , guest, next(guest_table)
    i+=1


# print the final results
for a in assign_guest(guests, guest_table):
  print(a)







