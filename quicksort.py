"""
Implementation of Quick Sort
In place
Credit: Prof. Osmar R. Zaiane - UAlberta
"""
def quick_sort(data, info):
    quick_sort_helper(data,0,len(data) - 1, info)

def quick_sort_helper2(info):
    data = info.lst
    quick_sort(data, info)

def quick_sort_helper(data,first,last, info):
    if first < last:
        pivot = partition(data, first, last, info)  # partition around a pivot
        quick_sort_helper(data,first,pivot-1, info)  # sort 1st half
        quick_sort_helper(data,pivot+1,last, info)  # sort 2nd half

def partition(data, first, last, info):
    pivotValue = data[first]  # choosing the pivot as the first element in the list
    leftMark = first + 1  # leftmark indicates the end of the first partition (+1)
    rightMark = last  # rightmark indicates the beginning of the second partion
    done = False

    from main import draw_list
    draw_list(info, {pivotValue: info.CYAN, rightMark: info.RED, leftMark: info. GREEN}, True)

    while not done:
        while leftMark <= rightMark and data[leftMark] <= pivotValue:
            leftMark += 1  # shifting pointer to the right
            
        while rightMark >= leftMark and data[rightMark] >= pivotValue:
            rightMark -= 1  # shifting pointer to the left
        if rightMark < leftMark:  # the partitioning is done
            done = True
        else:  # elements blocking the partitioning need to be swapped around pivot
            temp = data[leftMark]
            data[leftMark] = data[rightMark]
            data[rightMark] = temp
            
    temp = data[first]  # putting pivot in place
    data[first] = data[rightMark]
    data[rightMark] = temp
    
    return rightMark
