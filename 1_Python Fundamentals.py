# Python Fundamentals
#Exercise 1
# Write Python code that prints your name, student number and email address.
# An example runs of the program:
# Bob
# ST1001
# bob@gmail.com
print('Exercise 1')
Name="Aamir"
No=2
Email='aamirsalmancareers@gmail.com'
print('Name : ',Name)
print('No:',No)
print('Email:',Email)




#Exercise 2
# Write Python code that prints your name, student number and email address using escape sequences.
# An example runs of the program:
# Bob
# ST1001
# bob@gmail.com
print('\nExercise 2')
Name="Aamir"
No=2
Email='aamirsalmancareers@gmail.com'
print('Name:\t',Name,'\nNo.:\t',No,'\nEmail:\t',Email)



#Exercise 3
# Write Python code that add, subtract, multiply and divide the two numbers. You can use the two numbers 14 and 7.  An example run of the program:
# 14 + 7 = 21
# 14 * 7 = 98
# 14 – 7 = 7
# 14 / 7 = 2

print('\nExercise 3')
x=14
y=7
print(x,' + ',y, '=' ,x+y)
print(x,' * ',y, '=' ,x*y)
print(x,' - ',y, '=' ,x-y)
print(x,' / ',y, '=' ,x/y)


#Exercise 4'
# Write Python code that displays the numbers from 1 to 5 as steps.
# An example runs of the program:
# 1
# 2
# 3
# 4
# 5
print('\nExercise 4')
x=[1,2,3,4,5]
for i in x:
    print(i)


#Exercise 5
# Write Python code that outputs the following sentence (including the quotation marks and line break) to the screen:
# An example runs of the program:
# "SDK" stands for "Software Development Kit", whereas
# "IDE" stands for "Integrated Development Environment".
print('\nExercise 5')
print('"SDK" stands for "Software Development Kit", whereas \n"IDE" stands for "Integrated Development Environment".')



# Exercise 6
# Practice and check the output
# print("python is an \"awesome\" language.")
# print("python\n\t2023")
# print('I\'m from Entri.\b')
# print("\65")
# print("\x65")
# print("Entri", "2023", sep="\n")
# print("Entri", "2023", sep="\b")
# print("Entri", "2023", sep="*", end="\b\b\b\b")

print('\nExercise 6')
print("python is an \"awesome\" language.")
#output:
#pyhon ia an "awesome" language.
print("python\n\t2023")
#output:
#python
#	2023
print('I\'m from Entri.\b')
#output:
#I'm from Entri
print("\65")
#output:
#5
print("\x65")
#output:
#e
print("Entri", "2023", sep="\n")
#output:
#Entri
#2023
print("Entri", "2023", sep="\b")
#output:
#Entr2023
print("Entri", "2023", sep="*", end="\b\b\b\b")
#output:
#Entri*



#Exercise 7
# Define the variables below.
# Print the types of each variable.
# What is the sum of your variables? (Hint: use a type conversion function.) What datatype is the sum?
# num=23
# textnum="57"
# decimal=98.3

print('\n\nExercise 7')
num=23
textnum="57"
decimal=98.3
print(type(num))
print(type(textnum))
print(type(decimal))
sum=(num+int(textnum)+decimal)
print(sum)
#output:178.3
print(type(sum))
#output:<class 'float'>




# Exercise 8
# calculate the number of minutes in a year using variables for each unit of time.
# print a statement that describes what your code does also.
# Create three variables to store no of days in a year, minute in a hour, hours in a day, then calculate the total minutes in a year and print the values
# (hint) total number of minutes in a year =No.of days in an year * Hours in a day * Minutes in an hour

print('\nExercise 8')
# Number of days in a year
Days_in_year=365.25
# Number of hours in a day
Hours_in_day=24
# Number of minutes in a hour
Min_in_hour=60

# Total no of minutes in a year is:
no_of_min_a_year=Days_in_year*Hours_in_day*Min_in_hour

#Printing the final value (Total minutes in a year)
print('Total no. of minutes in a year =',no_of_min_a_year,'minutes')
#output:525960.0

# Exercise 9
# Write Python code that asks the user to enter his/her name and then output/prints his/her name with a greeting.
# An example runs of the program:
# Please enter you name: Tony
# Hi Tony, welcome to Python programming :)
print("\nExercise 9")
Name=input("Enter your Name: ")
print('Hi ',Name,', Welcome to python programming :')


#
# Exercise 10
# Name your file: PoundsToDollars.py
# Write a program that asks the user to enter an amount in pounds (£) and the program calculates and converts an amount in dollar ($)
# An example runs of the program:
# Please enter amount in pounds: XXX
# £ XXX are $ XXX
print("\nExercise 10\nRefer PoundsToDollars.py file")
