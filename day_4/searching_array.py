# #linear search

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i  # Return the index if found
#     return -1  # Return -1 if not found

# my_array = [19, 20, 29, 30, 90, 102,123]
# target = 19
# target2 = 30
# target3 = 123
# index = linear_search(my_array, target)
# if index != -1:
#     print(f"Element {target} found at index {index} time complexity - O(1)-best case")  
# else:
#     print(f"Element {target} not found in the array")

# index2 = linear_search(my_array, target2)
# if index2 != -1:
#     print(f"Element {target2} found at index {index2} time complexity - O(n/2)-average case")
# else:
#     print(f"Element {target2} not found in the array")

# index3 = linear_search(my_array, target3)
# if index3 != -1:
#     print(f"Element {target3} found at index {index3} time complexity - O(n)-worst case")
# else:
#     print(f"Element {target3} not found in the array")

## Binary search
# Example of binary search in Python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2  # Integer division to find the middle index
        if arr[mid] == target:
            return mid  # Return the index if found
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half
    return -1  # Return -1 if not found

my_array = [10, 20, 30, 40, 50, 60, 70, 80]  # Sorted array
target = 40
target2 = 20
target3 = 80
index = binary_search(my_array, target)
if index != -1:
    print(f"Element {target} found at index {index} time complexity - O(log n)-best case")
else:
    print(f"Element {target} not found in the array")
index2 = binary_search(my_array, target2)
if index2 != -1:
    print(f"Element {target2} found at index {index2} time complexity - O(log n)-average case")
else:
    print(f"Element {target2} not found in the array")

index3 = binary_search(my_array, target3)
if index3 != -1:
    print(f"Element {target3} found at index {index3} time complexity - O(log n)-worst case")
else:
    print(f"Element {target3} not found in the array")
