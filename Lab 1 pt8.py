#Exercise 8: Square-footage, Variables and Operators
#I have been using round() to limit decimal places in my outputs for currency and measurements.
#I also included a print of the total area, just for my own rhythm
living_length = int(input("Enter the length of the living room in feet: "))
living_width = int(input("Enter the width of the living room in feet: ")) 
living_total = living_width * living_length
kitchen_length = int(input("Enter the length of the kitchen in feet: "))
kitchen_width = int(input("Enter the width of the kitchen in feet: "))
kitchen_total = kitchen_length * kitchen_width
bedroom_length = int(input("Enter the length of the bedroom in feet: "))
bedroom_width = int(input("Enter the width of the bedroom in feet: "))
bedroom_total = bedroom_length * bedroom_width
total_area = living_total + kitchen_total + bedroom_total
print("The total square footage of the house is:", total_area, "square feet.")
print("The total cost for flooring at $4.57 per square foot is: $", round((total_area * 4.57), 2))
