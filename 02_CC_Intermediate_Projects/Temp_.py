'''
'# Importing unittest framework
import unittest


# Function that gets tested
def times_ten(number):
    return number * 100

# Test class
class TestTimesTen(unittest.TestCase):
    def test_multiply_ten_by_zero(self):
        self.assertEqual(times_ten(0), 0, 'Expected times_ten(0) to return 0')

    def test_multiply_ten_by_one_million(self):
        self.assertEqual(times_ten(1000000), 10000000, 'Expected times_ten(1000000) to return 10000000')

    def test_multiply_ten_by_negative_number(self):
        self.assertEqual(times_ten(-10), -100, 'Expected add_times_ten(-10) to return -100')

# Run the tests
unittest.main()
'''
'''
# your code below:
import unittest


def get_nearest_exit(row_number):
    if row_number < 15:
        location = 'front'
    elif row_number < 30:
        location = 'middle'
    else:
        location = 'back'
    return location


# Write your code below:
class NearestExitTests(unittest.TestCase):

    def test_row_1(self):
        self.assertEqual(get_nearest_exit(1), 'front', 'The nearest exit to row 1 is in the front!')

    def test_row_20(self):
        self.assertEqual(get_nearest_exit(20), 'middle', 'The nearest exit to row 20 is in the middle!')

    def test_row_40(self):
        self.assertEqual(get_nearest_exit(40), 'back', 'The nearest exit to row 40 is in the back!')


# test_row_1()
# test_row_20()
# test_row_40()

#unittest.main()
'''
'''
import unittest


# The function we want to test
def times_ten(number):
    return number * 100


# Our test class
class TestTimesTen(unittest.TestCase):

    def test_times_ten(self):
        for num in [0, 1000000, -10]:
            with self.subTest(num):
                expected_result = num * 10
                message = "Expected result of times_ten(" + str(num) + ") is :" +str(expected_result)
                self.assertEqual(times_ten(num), expected_result , message)

#unittest.main()
'''
'''
import unittest
def power_cycle_device():
  print('Power cycling bluetooth device...')

class BluetoothDeviceTests(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    power_cycle_device()

  def test_feature_a(self):
    print('Testing Feature A')

  def test_feature_b(self):
    print('Testing Feature B')

  @classmethod
  def tearDownClass(self):
    power_cycle_device()

#unittest.main()
'''
'''
import sys
import unittest


class LinuxTests(unittest.TestCase):

    @unittest.skipUnless(sys.platform.startswith("linux"), "This test only runs on Linux")
    def test_linux_feature(self):
        print("Error, This test should only run on Linux")

    @unittest.skipIf(not sys.platform.startswith("linux"), "This test only runs on Linux")
    def test_other_linux_feature(self):
        print("Error, "
              "This other_test_2 should only run on Linux")

'''
'''

sku_list = [7046538, 8289407, 9056375, 2308597]
sku_iterator = iter(sku_list)
for i in range(5):
  #next_sku = sku_iterator.__next__()
  next_sku = next(sku_iterator)
  print(next_sku)
'''

'''
def prize_generator():
  student_info = {
    "Joan Stark": 355,
    "Billy Mars": 45,
    "Tori Rivers": 18,
    "Kyle Newman": 25
  }

  for student in student_info:
    name = student
    id = student_info[name]
    if id % 3 == 0 and id % 5 == 0:
      yield student + " gets prize C"
    elif id % 3 == 0:
      yield student + " gets prize A"
    elif id % 5 == 0:
      yield student + " gets prize B"

prizes = prize_generator()
print(next(prizes))
print(next(prizes))
print(next(prizes))
print(next(prizes))
print(next(prizes))

'''
'''

def number_generator():
    i = 0
    while True:
        yield i
        i += 1

def even_number_generator(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n


even_numbers = even_number_generator(number_generator())


def summa():
    yield 'Summa Cum Laude'

def magna():
    yield 'Magna Cum Laude'

def cum_laude():
    yield 'Cum Laude'

def honors_generator(gpas):
  for gpa in gpas:
    if gpa > 3.9:
      yield from summa()
    elif gpa > 3.7:
      yield from magna()
    elif gpa > 3.5:
      yield from cum_laude()


def graduation_countdown(days):
  while days >= 0:
    days_left = yield days
    if days_left != None:
      days = days_left
    else:
      days -= 1


days = 25
countdown_generator = (day for day in range(days, -1,-1))
grad_days = graduation_countdown(days)
for day in grad_days:
  if day == 15:
    grad_days.send(10)
  elif day == 3:
    grad_days.close()
  print("Days Left: " + str(day))


days = 25
gpas = [3.2, 4.0, 3.6, 2.9, 3.75]

honors = honors_generator(gpas)
for honor_label in honors:
  print(honor_label)

'''
'''
song_tags = {'country', 'folk', 'acoustic'}

song_tags.add("guitar")
song_tags.add("country2")
print(song_tags)

other_tags =  ['live', 'blues', 'acoustic']
song_tags.update(other_tags)
#song_tags.update(['live', 'blues', 'acoustic'])
print(song_tags)

'''
'''
song_tags = {'guitar', 'acoustic', 'folk', 'country', 'live', 'blues'}

#song_tags.remove("guitar")
#zsong_tags.remove("fiddle")

song_tags.discard("guitar")
song_tags.discard("fiddle")
print(song_tags)
'''
'''
allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie', 'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal', 'jazz', 'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', 'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']

song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb', 'warm', 'due', 'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}

tag_set = set(song_data_users["Retro Words"])


bad_tags = []
for tag in tag_set:
  if tag not in allowed_tags:
    bad_tags.append(tag)

#print(bad_tags)

for tag in bad_tags:
  if tag in tag_set:
    tag_set.remove(tag)

#print(tag_set)

song_data_users["Retro Words"] = tag_set
print(song_data_users)

'''
'''

#   .union()  | merge
prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}

py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})

combined_tags = prepare_to_py.union(py_and_dry)
print(combined_tags)

combined_frozen_tags = py_and_dry | prepare_to_py
print(combined_frozen_tags)

# Write your code below!
new_song_data = {}
for key, value in song_data.items():
    song_tag_set = set(song_data[key])
    user_tag_set = set(user_tag_data[key])
    new_song_data[key] = song_tag_set.union(user_tag_set)

print(new_song_data)

prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}

py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})


frozen_intersection_tags = py_and_dry.intersection(prepare_to_py)
print(frozen_intersection_tags)

intersected_tags = prepare_to_py & py_and_dry
print(frozen_intersection_tags)


song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_recent_songs = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}




tags_int = set(user_recent_songs["Retro Words"]) & set(user_recent_songs["Lowkey Space"])
print(tags_int)

recommended_songs = {}
for key, value in song_data.items():
    for tag in value:
        if tag in tags_int:
            if key not in user_recent_songs:
                recommended_song[key] = value


 print(recommended_songs)

'''
'''
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth']}


tag_diff = set(user_liked_song['Back To Art']).difference(user_disliked_song['Retro Words'])
print(tag_diff)

# Checkpoint 2
recommended_songs = {}
for key, val in song_data.items():
    for tag in val:
        if tag in tag_diff:
            if key not in user_liked_song and key not in user_disliked_song:
                recommended_songs[key] = val

print(recommended_songs)

'''
'''
user_song_history = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Stomping Cue': ['country', 'fiddle', 'party'],
                     'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

friend_song_history = {'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
                     'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
                     'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

# Write your code below!
# Checkpoint 1
user_tags = set()
for key, val in user_song_history.items():
    user_tags.update(set(val))

friend_tags = set()
for key, val in friend_song_history.items():
    friend_tags.update(set(val))

#unique_tags = user_tags.symmetric_difference(friend_tags)

unique_tags = user_tags ^ friend_tags
print(unique_tags)

'''
'''

orders = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99},
          'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99}
         }

order_4829_price = orders['order_4829']['price']
print(order_4829_price)
order_6184_size = orders['order_6184']['size']
print(order_6184_size)
orders['order_4829']['size'] = 'x-large'
print(orders['order_4829']['size'])
num_of_orders = len(orders)
print(len(orders))
print(orders)

'''
'''

# Checkpoint #1
supplies_deque = deque()

# Checkpoint #2
for row in csv_data:
  if row[2] == "important" :
    supplies_deque.appendleft(tuple(row))
  else:
    supplies_deque.append(tuple(row))

#print(supplies_deque)

# Checkpoint #3
ordered_important_supplies = deque()
for i in range(25):
    ordered_important_supplies.append(supplies_deque.popleft())

# Checkpoint #4
ordered_unimportant_supplies = deque()
for i in range(10):
    ordered_unimportant_supplies.append(supplies_deque.pop())

print("25 Ordered IMPORTANT Supplies: " , ordered_important_supplies)
print("10 Ordered UNIMPORTANT Supplies: " , ordered_unimportant_supplies)
'''
'''
clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'white', '12', 24.99),
           ('t-shirt', 'grey', 'small', 8.99)]
from collections import namedtuple

ClothingItem = namedtuple("ClothingItem", ['type', 'color', 'size',  'price'])

new_coat = ClothingItem("coat", "black" , "small", 14.99)

coat_cost = new_coat.price

updated_clothes_data = []

for item in clothes:
  updated_clothes_data.append(ClothingItem(item[0], item[1], item[2], item[3]))

print(updated_clothes_data)
'''
'''
from collections import defaultdict

#prices = {'jeans': 19.99, 'shoes': 24.99, 't-shirt': 9.99, 'blouse': 19.99}

validate_prices = defaultdict(lambda: "no price assigned!")

validate_prices['jeans'] = 19.99
validate_prices['shoes'] = 24.99
validate_prices['t-shirt'] = 9.99
validate_prices['blouse'] = 19.99

print(list(validate_prices))
print(validate_prices['jacket'])



from collections import defaultdict

validated_locations = defaultdict(lambda: "TODO: Add to website")

validated_locations.update(site_locations)
#print(validated_locations)

for item in updated_products:
  site_locations[item] = validated_locations[item]

print(site_locations)
'''
'''

first_order = {'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50}}
second_order = {'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99}}
third_order = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99}}

list_of_dicts = [first_order, second_order, third_order]
print(list_of_dicts)

print(list_of_dicts[1]['order_6184']['price'])

dict_of_dicts = {}
dict_of_dicts.update(first_order)
dict_of_dicts.update(second_order)
dict_of_dicts.update(third_order)
print(dict_of_dicts)
print(dict_of_dicts['order_6184']['price'])

from collections import OrderedDict
orders = OrderedDict()

orders.update({'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50}})
orders.update({'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99}})
orders.update({'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99}})

find_order = orders["order_2905"]
print(find_order)

orders_list = list(orders.items())
print(orders_list)
third_order = orders_list[2]

orders.move_to_end("order_6184")
last_order = orders.popitem()
print(last_order)
'''
'''
from collections import OrderedDict
orders = OrderedDict(order_data)
to_move = []
to_remove= []

#print(orders)

for key, val in orders.items():
  if val == 'returned':
    to_move.append(key)
  elif val == 'canceled':
    to_remove.append(key)

for order_to_be_removed in to_remove:
  orders.pop(order_to_be_removed)

for order_to_be_moved_back in to_move:
  orders.move_to_end(order_to_be_moved_back)

print("Ordered Orders : " , orders)
print("MOVED Orders: ", to_move)
print("REMOVED Orders: " , to_remove)
'''
'''

year_profit_data = [
    {'jan_profit': 15492.30, 'jan_holiday_profit': 2589.12},
    {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88},
    {'mar_profit': 11849.13},
    {'apr_profit': 9870.68},
    {'may_profit': 13662.34},
    {'jun_profit': 12903.54},
    {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21},
    {'aug_profit': 17685.69},
    {'sep_profit': 9815.57},
    {'oct_profit': 10318.28},
    {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55},
    {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79}
]

new_months_data = [
    {'jan_profit': 13977.85, 'jan_holiday_profit': 2176.43},
    {'feb_profit': 16692.15, 'feb_holiday_profit': 3239.74},
    {'mar_profit': 17524.35, 'mar_holiday_profit': 4301.92}
]

from collections import ChainMap

profit_map = ChainMap(*year_profit_data)

# Checkpoint #2
def get_profits(input_map):
    total_standard_profit = 0.0
    total_holiday_profit = 0.0

    for key in input_map.keys():
        if 'holiday' in key:
            total_holiday_profit += input_map[key]
        else:
            total_standard_profit += input_map[key]

    return total_standard_profit, total_holiday_profit

last_year_standard_profit, last_year_holiday_profit = get_profits(profit_map)

# Checkpoint #3
for item in new_months_data:
    profit_map = profit_map.new_child(item)


current_year_standard_profit , current_year_holiday_profit = get_profits(profit_map)

year_diff_standard_profit = current_year_standard_profit - last_year_standard_profit
print(year_diff_standard_profit)

year_diff_holiday_profit = current_year_holiday_profit - last_year_holiday_profit
print(year_diff_holiday_profit)

'''
'''
clothes_list = ['skirt', 'hoodie', 'dress', 'blouse', 'jeans', 'shoes', 'skirt', 'skirt', 'jeans', 'hoodie', 'boots', 'jeans', 'jacket', 't-shirt', 'skirt', 'skirt', 'dress', 'shoes', 'blouse', 'hoodie', 'skirt', 'boots', 'shoes', 'boots', 'jeans', 'hoodie', 'blouse', 'hoodie', 'shoes', 'shoes', 'blouse', 'boots', 'blouse', 'hoodie', 't-shirt', 'jeans', 'dress', 'skirt', 'jacket', 'boots', 'skirt', 'dress', 'jeans', 'jeans', 'jacket', 'jeans', 'shoes', 'dress', 'hoodie', 'blouse']
#counted_items = {}
#for item in clothes_list:
#    if item not in counted_items:
#        counted_items[item] = 1
#    else:
#        counted_items[item] += 1

#print(counted_items)

from collections import Counter
counted_items = Counter(clothes_list)
print(counted_items)




from collections import Counter

def find_amount_sold(opening, closing, item):
  opening_count = Counter(opening)
  closing_count = Counter(closing)
  opening_count.subtract(closing_count)
  return opening_count[item]

tshirts_sold = find_amount_sold(opening_inventory , closing_inventory, "t-shirt")
print(tshirts_sold)

print(Counter(opening_inventory))
print(Counter(closing_inventory))

print(Counter(opening_inventory).subtract(Counter(closing_inventory)))
'''
'''

class Customer:

  def __init__(self, name, age, address, phone_number):
    self.name = name
    self.age = age
    self.address = address
    self.phone_number = phone_number

class CustomerWrap(Customer):

  def __init__(self, name, age, address, phone_number):
    self.customer = Customer(name, age, address, phone_number)

  def display_customer_info(self):
    print('Name: ' + self.customer.name)
    print('Age: ' + str(self.customer.age))
    print('Address: ' + self.customer.address)
    print('Phone Number: ' + self.customer.phone_number)

customer = CustomerWrap('Dmitri Buyer', 38, '123 Python Avenue', '5557098603')
customer.display_customer_info()
'''

'''

from collections import UserDict

# Create a class which inherits from the UserDict class
class DisplayDict(UserDict):
    # A new method to increase the dictionary's functionality
    def display_info(self):
        print("Number of Keys: " + str(len(self.keys())))
        print("Keys: " + str(list(self.keys())))
        print("Number of Values: " + str(len(self.values())))
        print("Values: " + str(list(self.values())))

    # We can also overwrite a method from the dictionary class
    def clear(self):
        print("Deleting all items from the dictionary!")
        super().clear()

disp_dict = DisplayDict({'user': 'Mark', 'device': 'desktop', 'num_visits': 37})

disp_dict.display_info()

disp_dict.clear()
'''
'''
from collections import UserDict


class OrderProcessingDict(UserDict):

  def clean_orders(self):
    to_del = []

    for key, value in self.data.items():
      if value["order_status"] == "complete":
        to_del.append(key)

    for item in to_del:
      del self.data[item]
      print("Deleting Completed Orders...")


# Checkpoint #2
process_dict = OrderProcessingDict(data)
process_dict.clean_orders()
print(process_dict)
'''
'''
from collections import UserList

# Create a class which inherits from the UserList class
class CondenseList(UserList):

    # A new method to remove duplicate items from the list
    def condense(self):
        self.data = list(set(self.data))
        print(self.data)


    # We can also overwrite a method from the list class
    def clear(self):
        print("Deleting all items from the list!")
        super().clear()

condense_list = CondenseList(['t-shirt', 'jeans', 'jeans', 't-shirt', 'shoes'])

condense_list.condense()

condense_list.clear()

print(condense_list)



class ListSorter(UserList):
  def append(self,item):
    self.data.append(item)
    self.data.sort()

sorted_list = ListSorter(data)
sorted_list.append(2)
print(sorted_list)
'''
'''

class SubtractString(UserString):
  def __sub__(self, other):
    if other in self.data:
      self.data = self.data.replace(other, "")

subtract_string  = SubtractString(str_name )
subtract_string - str_word

print(subtract_string)




split_prices = deque()
for item in overstock_items:
    if item[1] > 20.0:
        split_prices.appendleft(item)
    else:
        split_prices.append(item)

print(split_prices)



ClothesBundle = namedtuple('ClothesBundle', ['bundle_items', 'bundle_price'])

bundles = []
while len(split_prices) >= 5:
    bundle_list = [split_prices.pop(), split_prices.pop(), split_prices.pop(), split_prices.popleft(),
                   split_prices.popleft()]
    calc_price = sum(item[1] for item in bundle_list)

    bundles.append(ClothesBundle(bundle_list, calc_price))
print("BUNDLES: ", bundles)

promoted_bundles = []

for bundle in bundles:
    if bundle[1] >= 100:
        promoted_bundles.append(bundle)

print("PROMOTED BUNDLES: ", promoted_bundles)
'''
'''

class PoemFiles:
    def __init__(self, poem_file, mode):
        print("Starting up a poem context manager")
        self.file = poem_file
        self.mode = mode

    def __enter__(self):
        print("Opening poem file")
        self.opened_poem_file = open(self.file, self.mode)
        return self.opened_poem_file

    def __exit__(self, *exc):
        print("Closing poem file")
        self.opened_poem_file.close()


with PoemFiles('poem.txt', 'w') as open_poem_file:
    open_poem_file.write('Hope is the thing with feathers')

'''
'''
class PoemFiles:

  def __init__(self, poem_file, mode):
    print(' \n -- Starting up a poem context manager -- \n ')
    self.file = poem_file
    self.mode = mode

  def __enter__(self):
    print('Opening poem file')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file

  # Create your __exit__ method here:
  def __exit__(self, exc_type, exc_value, traceback):
    print(exc_type)
    print(exc_value)
    print(traceback)
    self.opened_poem_file.close()

# First
'''
'''

with PoemFiles('poem.txt', 'r') as file:
   print("---- Exception data below ----")
   print(file.uppercasewords())

# Second
with PoemFiles('poem.txt', 'r') as file2:
  print(file2.read())
  print("---- Exception data below ----")

'''

from contextlib import contextmanager


@contextmanager
def poem_files(file, mode):
    print('Opening File')
    open_poem_file = open(file, mode)
    try:
        yield open_poem_file
    finally:
        print('Closing File')
        open_poem_file.close()


@contextmanager
def card_files(file, mode):
    print('Opening File')
    open_card_file = open(file, mode)
    try:
        yield open_card_file
    finally:
        print('Closing File')
        open_card_file.close()


# Write your code below:
with poem_files("poem.txt", "r") as poem:
    with card_files("card.txt", "w") as card:
        card.write(poem.read())

print(poem)
print(card)









