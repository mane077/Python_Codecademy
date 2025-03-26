## SAL"S SHIPPING

weight = 41.5
print("Package Weight is: " + str(weight))
print("\nShipping Options and costs are: ")
# Ground Shipping ->
if weight <= 2:
    cost_ground_shipping = weight * 1.5 + 20
    print("Ground Shipping cost:      " + str(cost_ground_shipping) + " $")
elif weight > 2 and weight <= 6:
    cost_ground_shipping = weight * 3 + 20
    print("Ground Shipping cost:      " + str(cost_ground_shipping) + " $")
elif weight > 6 and weight <= 10:
    cost_ground_shipping = weight * 4 + 20
    print("Ground Shipping cost:        " + str(cost_ground_shipping) + " $")
else:
    cost_ground_shipping = weight * 4.75 + 20
    print("Ground Shipping cost:      " + str(cost_ground_shipping) + " $")

# Premium Ground Shipping ->
cost_ground_premium_shipping = 125
print("Premium Ground Shipping cost: " + str(cost_ground_premium_shipping) + " $")

# Drone Shipping ->
if weight <= 2:
    cost_drone_shipping = weight * 4.5
    print("Drone Shipping cost:        " + str(cost_drone_shipping) + " $")
elif weight > 2 and weight <= 6:
    cost_drone_shipping = weight * 9
    print("Drone Shipping cost:        " + str(cost_drone_shipping) + " $")
elif weight > 6 and weight <= 10:
    cost_drone_shipping = weight * 12
    print("Drone Shipping cost:        " + str(cost_drone_shipping) + " $")
else:
    cost_drone_shipping = weight * 14.25
    print("Drone Shipping cost:         " + str(cost_drone_shipping) + " $")

if cost_ground_shipping <= cost_ground_premium_shipping and cost_ground_shipping <= cost_drone_shipping:
    print("\nRecommended Shipping - Ground Shipping: " + str(cost_ground_shipping) + " $")
elif cost_ground_premium_shipping <= cost_ground_shipping and cost_ground_premium_shipping <= cost_drone_shipping:
    print("\nRecommended Shipping - Premium Shipping: " + str(cost_ground_premium_shipping) + " $")
else:
    print("\nRecommended Shipping - Drone Shipping: " + str(cost_drone_shipping) + " $")





