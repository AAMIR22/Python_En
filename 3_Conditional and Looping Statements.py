# Exercise 1
# Name your file: MonthNames.py
# Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year.
# An example run of the program (numbers in bold are typed in by the user)
# Enter the month: 3
# Month 3 is March
#please refer MonthNames.py file
print(f'Exercise 1')
print(f'Please refer MonthNames.py file')



# Exercise 2
# A certain cinema currently sells tickets for a full price of 6 pounds,
# but always sells tickets for half price to people who are less than 16 years old, and for a third of the price for people who are 60 years old or more.
# An example run of the program (numbers in bold are typed in by the user)
# Enter your age: 63
# Your ticket costs £2.00
print(f'\nExercise 2')
Film={'name':'Interstellar','price':6,'unit':'pounds'}
Category1limit=16
Category2limit=60
Age=int(input('Enter your Age : '))
if Age>Category2limit:
    print(f'Your Ticket Costs £',Film['price']/3)
elif Age<Category1limit:
    print(f'Your Ticket Costs £',Film['price']/2)
else:
    print(f'Your Ticket Costs £',Film['price'])



# Exercise 3
# Name your file: BodyMassIndex.py
# Write a program to calculate your BMI and give weight status. Body Mass Index (BMI) is an internationally used measurement to check if you are a healthy weight for your height.The metric BMI formula accepts weight in kilograms and height in meters:
# BMI= weight(kg)/height2(m2)
# BMI Weight Status Categories table
# BMI range - kg/m2   Category
# Below 18.5                    Underweight
# 18.5 -24.9         Normal
# 25 - 29.9          Overweight
# 30 & Above     Obese
# An example run of the program (numbers in bold are typed in by the user)
# Enter your weight in (kg): 75
# Enter your height in (m): 1.70
# Your BMI is: 25.95
# You are in the “overweight” range.
#please refer BodyMassIndex.py file
print(f'\nExercise 3')
print(f'Please refer BodyMassIndex.py file')



# Exercise 4
# Write a Python program to receive 3 numbers from the user and print the greatest among them.
print(f'\nExercise 4')
Num1=int(input("Enter the 1st number : "))
Num2=int(input("Enter the 2nd number : "))
Num3=int(input("Enter the 3rd number : "))
max_n=max(Num1,Num2,Num3)
print(f'The greatest number is : ',max_n)



# Exercise 5
# Find the factorial of a given number using loops(note the number is received from the user)
print(f'\nExercise 5')
fact=int(input('Enter a number to find factorial : '))
res=1
for i in range(1,fact+1):
    res*=i
print(f'Factorial of {fact} is {res}')



# Exercise 6
# Reverse a number using while loop
print(f'\nExercise 6')
num=int(input("Enter a number to reverse the digits : "))
r_num=0
while num > 0:
    num1=num%10
    r_num=(r_num*10)+num1
    num=num//10
print(r_num)



# Exercise 7
# Finding the multiples of a number using loop
print(f'\nExercise 7')
num=int(input("Enter numbers to find the multiples of each digit : "))
r_num=1
while num > 0:
    num1=num%10
    r_num=r_num*num1
    num=num//10
print(r_num)



# Exercise 8
# Write a program to print the inputted value as it is and break the loop if the value is 'done'.
# Example run of the program
# :hello there
# hello there
# :finished
# finished
# :done
# Done
print(f'\nExercise 8')
while True:
    text = (input("Entering 'Done' will end the programme \nInput the text :"))
    if text.lower()=="done":
        print(f'Done')
        break
    else:
        print(text)



# Exercise 9
# Write a program that prints the numbers from 1 to 10. But for multiples of three print "Fizz" instead of the number and for the multiple of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"
print(f'\nExercise 9')
for i in range(1,11):
    if i % 3 == 0 and i % 5 == 0:
        print(f'FizzBuzz')
    elif i % 3 == 0:
        print(f'Fizz')
    elif i % 5 == 0:
        print(f'Buzz')
    else :
        print(i)



# Exercise 10
# Write a program to print the following pattern:

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
print(f'\nExercise 10')
for i in range(5,0,-1):
    for j in range (i,0,-1):
        print(j,end=" ")
    print()