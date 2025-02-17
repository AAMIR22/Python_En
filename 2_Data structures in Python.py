#Topic :List Exercise
# Q1. Create a list of 5 random numbers and print the list.
print("List\nQ1:")
list1=[2,5,3,7]
print(list1)


# Q2. Insert 3 new values to the list and print the updated list.
print("\nQ2:")
list1[4:4]=[2,3,4]
#or
#list1.extend([2,3,4])
#or
# list1.append(2)
# list1.append(3)
# list1.append(4)
print(list1)

# Q3. Try to use a for loop to print each element in the list.
print("\nQ3:")
for i in list1:
    print(i)


# Topic: Dictionary Exercise
# Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.
print("\nDictionary\nQ1:")
Dict1={'name':'John','Age':25,'Address':'New York'}
print(Dict1)

# Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'.
print("\nQ2:")
Dict1['Phone']=1234567890
print(Dict1)

# Topic: Set Exercise Q1.Create a set with values 1, 2, 3, 4, and 5.
print("\nSet\nQ1:")
Set1={1,2,3,4,5}
print(Set1)

# Q2. Add the value 6 to the set created in Q1.
print("\nQ2:")
Set1.add(6)
print(Set1)

# Q3. Remove the value 3 from the set created in Q1.
print("\nQ3:")
Set1.remove(3)
print(Set1)


# Topic:Tuple Exercise Q1. Create a tuple with values 1, 2, 3, and 4
print("\nTuple\nQ1:")
Tuple1=(1,2,3,4)
print(Tuple1)


#Q2. Print the length of the tuple created in Q1.
print("\nQ2:")
print(len(Tuple1))