#4-Python Function
#Exercise 1:
# Create a function that takes in three arguments, two of which are optional.
# The first argument should be a required positional argument,
# the second argument should be a keyword argument with a default value of 10,
# and the third argument should be a keyword argument with a default value of None.
# The function should print the sum of the first two arguments if the third argument is None,
# and print the product of all three arguments if the third argument is not None.

print("Exercise 1:")

def fun_sum_integers(num1,num2=10,num3=None):
    if num3 is None:
        sum=num1+num2
    else:
        sum=num1+num2+num3
    return sum

result=fun_sum_integers(1)
print(f'Result :',result)


# Exercise 2: Write a function that takes in a list of strings and returns a new list with only the strings that have a length greater than or equal to 5.

print("\nExercise 2:")

def fun_str_greater_len5(*str):
    list=[]
    for i in str:
        if len(i) >= 5:
            list.append(i)
    return list

result = fun_str_greater_len5("Apple","Kiwi","Jackfruit")
print(result)


# Exercise 3: Write a Python program to evaluate a given mathematical expression using the eval() function.
# expression = "3 * 5 + 2"

print("\nExercise 3:")

expression = "3 * 5 + 2"
result=eval(expression)
print(result)


# Exercise 4: (score : 2) Write a Python program to filter out the prime numbers from a given list of integers using the filter() function.

print("\nExercise 4:")

def filter(*args):
    list=[]
    for i in args:
        if i<2:
            continue
        elif i==2:
            list.append(i)
        else:
            is_prime = True
            for j in range(2,int(i**0.5)+1):
                if i % j == 0:
                    is_prime=False
                    break
            if is_prime:
                list.append(i)
    return list

res4=filter(-3,3,4,5,6,7,9,11,13,15,14,17)
print(res4)


# Exercise 5: (score : 2) Write a Python program to convert a list of strings to uppercase using the map() function.

print("\nExercise 4:")

list1 = ["Apple","Kiwi","Jackfruit"]
upper_list=list(map(str.upper,list1))
print(upper_list)