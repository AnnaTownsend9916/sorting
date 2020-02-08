from random import shuffle
nums = [n for n in range(10)]
shuffle(nums)





def bubble_sort(lst):
    # N is assigned to the length of the list
    n = len(lst)
    
    # go through each item(traverse)
    for i in range(n):
        #decides on swapping
        # normally false but if swapped
        #it changes to True.
        swapped = False
            
        # for unsorted items
        # the last i items are sorted already
        for j in range(0, n-i-1):
            # If the current item is greater than
            # the item to its right, swap them
            if lst[j] > lst[j+1]:
                # Swapping
                lst[j], lst[j+1] = lst[j+1], lst[j]
                # dang it smells like a swap just occured change ya variable 
                swapped = True
                
        # If there werent any swaps in inner loop
        # the list is sorted, so the loops life span has come to an end and stops
        if not swapped:
            break
            #breakup
    return lst
print(bubble_sort(nums))









