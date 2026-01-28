#Exercise 7: Cloud Storage Cost using Variables and Operators
#Personally, I would be using some if/else statements to make sure the user doesn't enter less than 750 GB,
#but since we haven't covered that yet, I'll just assume the user follows directions.
data = int(input("Enter the amount of data to be stored (in GB): "))
extra_data = data -750
print("The monthly cost for storing", data, "GB is: $", round((100 + (5 * extra_data)), 2))
