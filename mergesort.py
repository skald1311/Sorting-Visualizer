"""
Implementation of Merge sort
Recursion
"""
def merge(left,right, info):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]  # copy the rest
    result += right[j:]
    lst = info.lst
    for k in range(len(result)):
        lst[k] = result[k]
        from main import draw_list
        draw_list(info, {k: info.CYAN}, True)
    return result

def recursive_merge_sort(data, info): 
    # Set the base case 
    if len(data) <= 1:
        return data
    #Find the middle of the data list
    middle = len(data) // 2
    #Recursively calling merge sort function for both half of the data list
    left = recursive_merge_sort(data[:middle], info)
    right = recursive_merge_sort(data[middle:], info)
    # merge the two halves of the data list
    return merge(left,right, info)

def helper_merge(info):
    """Helper function"""
    recursive_merge_sort(info.lst, info)