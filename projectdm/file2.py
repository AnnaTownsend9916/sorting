from random import shuffle
nums = [n for n in range(10)]
shuffle(nums)


def selection_sort(lst):
    # go through list
    # i= index where unsorted part of list is
    for i in range(len(lst)):
        # The min_index is the
        # smallest item in the unsorted area 
        min_index = i
        # for every item in unsorted
        # check if the item is smaller than the current min
        # and assign that index as the new min_index.
        for curr_index in range(i+1, len(lst)):
            if lst[min_index] > lst[curr_index]:
                min_index = curr_index
        # Swap the min item with the first item of the 
        # unsorted portion of the list.
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst
print(selection_sort(nums))