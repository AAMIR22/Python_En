#5_File and Exception Handling

#Exercise 1: Write a Python program to read a file and display its contents
print('Exercise 1')
print("creating a file sample.txt in the same folder...")
file1=open("Sample.txt","w+")
file1.write('Hello, Welcome!')
file1.close()

print("reading sample.txt...")
r_file1=open("Sample.txt","r")
print(r_file1.read())
r_file1.close()




# Exercise 2: Write a Python program to copy the contents of one file to another file
print('\nExercise 2')
print("creating and copying file content from sample.txt to file sample_copy.txt in the same folder...")
file1=open("Sample.txt","r")
read_file1=file1.read()
file1_copy=open("Sample_copy.txt","w+")
file1_copy.write(read_file1)
file1_copy.close()

print('\nreading sample_copy.txt...')
file1_copy=open("sample_copy.txt","r")
print(file1_copy.read())




# Exercise 3: Write a Python program to read the content of a file and count the total number of words in that file.
print('\nExercise 3')
with open("Sample.txt","r") as sample:
    content=sample.read()
    len_sample=len(content)
    print(f"Length of file 'sample.txt' is : ",len_sample)




# Exercise 4: Write a Python program that prompts the user to input a string and converts it to an integer.
# Use try-except blocks to handle any exceptions that might occur
print('\nExercise 4')

try:
    a=input("Enter a string to convert to integer:")
    number=int(a)
    print(number)
except ValueError:
    print("Please enter number")






# Exercise 5: Write a Python program that prompts the user to input a list of integers and
# raises an exception if any of the integers in the list are negative.
print('\nExercise 5')
try:
    integers=input("Enter a list of integers to check for Negative Integers(use spaces to seperate each integers):")
    integer_list=[int(numbers) for numbers in integers.split()]
    for i in integer_list:
        if i < 0:
            raise ValueError ("Negative integer in list:",i)
    print("All are positive integers")
except ValueError as err:
    print(f'{err}')




# Exercise 6: Write a Python program that prompts the user to input a list of integers and
# computes the average of those integers.
# Use try-except blocks to handle any exceptions that might occur.
# use the finally clause to print a message indicating that the program has finished running.
print('\nExercise 6')
integers=input("Enter a list of integers to find average (use space to seperate): ")
try:
    list=[int(x) for x in integers.split()]
    l=len(list)
    sum=0
    for i in list:
        if i < 0:
            raise ValueError ("Negative integer in list:",i)
        sum+=i
    avg=sum/l
    print(f'Number of integers entered: ',l)
    print(f'Average of integers: ',avg)
except ValueError:
        print("Enter only integers")
finally:
    print("Program has finished running")


# Exercise 7 : Write a Python program that prompts the user to input a filename and writes a string to that file.
# Use try-except blocks to handle any exceptions that might occur and print a welcome message if there is no exception occurred.

print('\nExercise 7')
file_name=input('Enter a file name:')
string=input("Enter string to enter on file:")
try:
    with open(file_name,'w') as fi:
        fi.write(string)
    print('Content written successfully')
except:
    print(f'Error while opening the file')
else:
    print("Welcome!The file has been written without any issues.")
