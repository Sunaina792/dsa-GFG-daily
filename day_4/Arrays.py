# arrays

##================================
## Insertion    
##================================

# Insertion at the End
my_array = [10,45,67,3,87]
my_array.append(64)  
print(my_array) 

# Example of inserting at the beginning of a Python list
my_array = [55,78,99,23,14]
my_array.insert(0, 0)  # Inserts 0 at the beginning (index 0)
print(my_array)  

# Example of inserting at the middle of a Python list
my_array = [78,56,89,12,34]
my_array.insert(3, 10)  # Inserts 10 at index 3
print(my_array)

##================================
## Deletion 
##================================


# Example of deleting from the end 
my_array = [10, 20, 30, 40, 50]
my_array.pop()  # Removes the last element
print(my_array)  

# Example of deleting from the beginning 
my_array = [100, 200, 300, 400, 500]
del my_array[0]  # Deletes the element at index 0
print(my_array) 

# Example of deleting from the middle 
my_array = [11, 22, 33, 44, 55]
del my_array[2]  # Deletes the element at index 2
print(my_array)  

#Another way to delete from the middle 
my_array = [1, 2, 3, 4, 5]
my_array.pop(2) # Removes the element at index 2
print(my_array)  