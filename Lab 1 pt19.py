#Exercise 19: Assignment Operators
#The last exercise in this lab!  I admittinly did this one without the compound operators first, but realized
#that is what you were looking for.  As such, I rewrote it using the compound assignment operators.
customer_purchase = 23
coffee_price = 10.00
customer_purchase *= coffee_price
discount = .10 *customer_purchase
print("The Discount amount is :$", format(discount, '.2f'))
customer_purchase -= discount
print("The Total after discount is :$", format(customer_purchase, '.2f'))
