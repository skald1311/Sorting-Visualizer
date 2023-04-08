"""
Implementation of Bubble Sort
Keep track of the exchanges made
Compare current element with the next and switch if necessary
GREEN = current cursor
RED = next of current
"""

def bubble_sort(info):
    lst = info.lst
    exchange = True
    last = len(lst) - 1
    while exchange and last >= 0:
        exchange = False
        for current in range(last):
            if (lst[current] > lst[current+1]):
                temp = lst[current]
                lst[current] = lst[current + 1]
                lst[current + 1] = temp
                exchange = True
                from main import draw_list
                draw_list(info, {current: info.GREEN, current+1: info.RED}, True)
                yield True  # pause the execution => can use the controls
        last -= 1