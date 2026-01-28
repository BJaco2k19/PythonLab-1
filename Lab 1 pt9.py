#Exercise 9: Using Strings format, Variables to Determine Shipping
tablet_weight = 1
laptop_weight = 7
TV_weight = 37
ship_rate = 2.66
tablet_cost= tablet_weight * ship_rate
laptop_cost= laptop_weight * ship_rate
TV_cost= TV_weight * ship_rate
print("The total shipping cost for all items is ${:.2f}".format(tablet_cost + laptop_cost + TV_cost))
