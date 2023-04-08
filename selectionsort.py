"""
Implementation of Selection Sort
Find smallest then swap it with element at position index and increment index.
Increment index => all element on the left of index is sorted

GREEN = min tower to swap
RED = the tower that is going to be swap with the min
"""
def selection_sort(info):
    lst = info.lst
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if (lst[j] < lst[min_index]):
                min_index = j
        temp = lst[i]
        lst[i] = lst[min_index]
        lst[min_index] = temp
        from main import draw_list
        draw_list(info, {min_index: info.GREEN, i: info.RED}, True)
        yield True

