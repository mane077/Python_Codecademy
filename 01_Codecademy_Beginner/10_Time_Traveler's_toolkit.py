### TIME TRAVELER"S TOOLKIT

import datetime as dt
from decimal import Decimal
from random import randint, choice
from custom_module import generate_time_travel_message


current_date = dt.date.today()
current_time = dt.datetime.now().time()

print(current_date)
print(current_time)

base_cost = Decimal("10.00")
print(base_cost)

current_year = dt.datetime.now().year
print(current_year)

target_year = randint(1, 2025)
print(target_year)

cost_multiplier = abs ( current_year - target_year)
print(cost_multiplier)

total_cost = base_cost * cost_multiplier
print(total_cost)

destinations = ["NYC", "LA", "California", "Chicago","Seattle"]

destination = choice(destinations)
print(destination)

generate_time_travel_message (randint(1,2026),choice(destinations), total_cost)

#generate_time_travel_message(target_year,destination, total_cost)
