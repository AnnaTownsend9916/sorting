from random import shuffle
nums = [n for n in range(10)]
shuffle(nums)



def insertion_sort(lst):
    # For every item in the list (except the first one).
    for i in range(1, len(lst)):
        # take the first item of unsorted list
        elem_selected = lst[i]
 
        # Check the items in the unsorted portion
        # and move them one index to the right if they
        # are greater than the item selected.
        while i > 0 and elem_selected < lst[i-1]:
            lst[i] = lst[i-1]
            i -= 1
 
        # Insert the item where it belongs.
        lst[i] = elem_selected
    return lst
print(insertion_sort(nums))
