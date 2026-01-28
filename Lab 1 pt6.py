#Exercise 6: Unit Conversion
feet = int(input("Enter your height in feet:"))
conv_inch=12
inch = int(input("Enter the inches in your height:"))
conv_meter=39.3701
print( "Your height is: ", round((((feet*conv_inch) + inch) / conv_meter), 2), "in meters.")

