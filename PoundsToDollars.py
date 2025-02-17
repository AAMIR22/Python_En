# Exercise 10
# Name your file: PoundsToDollars.py
# Write a program that asks the user to enter an amount in pounds (£) and the program calculates and converts an amount in dollar ($)
# An example runs of the program:
# Please enter amount in pounds: XXX
# £ XXX are $ XXX


Dollar_Pound_rate=1.26
print("The current exchange rate (as of 18-feb-2025 01:50 am (+4:30 GST)) is 1 British Pounds (GBP) = 1.26 US Dollar (USD) aprox.")
Pounds=int(input('Enter an amount in pounds: '))
Dollar=Dollar_Pound_rate*Pounds
print("US Dollar : ",Dollar)


