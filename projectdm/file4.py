from random import shuffle
nums = [n for n in range(10)]
shuffle(nums)


def linear_search(main_list, item):
    # Check every item in the list
    for i in range(len(main_list)):
        # If the item is the one you are looking for
        if main_list[i] == item:
            # Return the index where the item is located
            return i
    # If the item is not found, return -1
    return -1
print(linear_search(nums, 7))