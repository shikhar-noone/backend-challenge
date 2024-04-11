
def get_maxmimum_sum_contiguous_subarray(arr):

    if not arr:
        raise Exception("Invalid input!")
    global_max = 0
    local_max = 0

    for number in arr:
        local_max = max(number, number + local_max)
        global_max = max(local_max, global_max)

    return global_max

arr = [-2, 3, -3, 4, -1, 2, 1, -5, 4]
max_value = get_maxmimum_sum_contiguous_subarray(arr)
print(max_value)

"""
Approach taken:
1. You traverse through the array and maintain a local_max_value and global_max_value.
2. At each point you check whether that number is greater than the sum of local_max and that number,
    this check is necessary because there is no point in adding the previous sum because the overall sum will be less than the number itself. 
3. At each we also compare local max value and global max value, if its local_max is greater than global_max,
    we update global_max.
"""