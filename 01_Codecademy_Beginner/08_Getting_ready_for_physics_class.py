## GETTING READY FOR PHYSICS CLASS:

# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Write your code below:

def f_to_c(f_temp):
  c_temp = (f_temp - 32 ) * 5 / 9
  return c_temp
f100_in_celsius = f_to_c(100)
print(" 100deg Fahrenheit in Celius: " , f100_in_celsius)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print("Celsius 0 deg in Fahrenheit: " , c0_in_fahrenheit)

# Calculate force using f = m * a
def get_force(mass, acceleration):
  force = mass * acceleration
  return force
train_force = get_force(train_mass, train_acceleration)

print ("The GE train supplies " , train_force , "Newtons of force." )

# Calculate energy using E = mc^2
def get_energy(mass , c = 3*10**8):
  energy = mass * (c**2)
  return energy

bomb_energy = get_energy(bomb_mass)
print ( "A 1kg bomb supplies ", bomb_energy ," Joules." )

# Calculate work using w = f * d  = m * a * d
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  work = force * distance
  return work

train_work= get_work(train_mass, train_acceleration, train_distance)
print ("The GE train does ", train_work , "Joules of work over ", train_distance , "meters.")







