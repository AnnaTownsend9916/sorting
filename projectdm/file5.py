from random import shuffle
nums = [n for n in range(10)]
shuffle(nums)



# takes in a tuple or list and an item you want to find
def binary_search(data, item):
 
    # The lower bound is the first index in the list.
    # The upper bound is the last index in the list.
    low = 0
    high = len(data) - 1
 
    # While the interval is true
    while low <= high:
        # Find the item in the middle of the interval
        middle = (low + high)//2
        # If that item is equal to the target item,
        # return the index.
        if data[middle] == item:
            return middle
        # If the item is not equal to the target item,
        # check if it's greater or smaller and reassign
        # the bounds appropriately. 
        elif data[middle] > item:
            high = middle - 1
        else:
            low = middle + 1
 
    # Else, if the item is not found in the list, return -1
    return -1
print(binary_search(nums, 7))