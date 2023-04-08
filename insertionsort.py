"""
Implementation of Insertion sort
Take an element on the right and put it in its right place on the left
Shift instead of swap
RED = the tower which is considering to be swapped
GREEN = the correct position of that tower
"""
def insertion_sort(info):
    lst = info.lst
    for i in range(1, len(lst)):
        temp = lst[i]
        position = i
        while position > 0 and lst[position - 1] > temp:
            lst[position] = lst[position - 1]
            position = position - 1
        lst[position] = temp
        from main import draw_list
        draw_list(info, {position: info.GREEN, i: info.RED}, True)
        yield True
