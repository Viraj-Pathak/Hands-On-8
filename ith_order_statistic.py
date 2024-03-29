def viraj_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def viraj_quickselect(arr, low, high, i):
    if low == high:
        return arr[low]

    pivot_index = viraj_partition(arr, low, high)
    k = pivot_index - low + 1

    if i == k:
        return arr[pivot_index]
    elif i < k:
        return viraj_quickselect(arr, low, pivot_index - 1, i)
    else:
        return viraj_quickselect(arr, pivot_index + 1, high, i - k)

def ith_order_statistic(arr, i):
    if i < 0 or i >= len(arr):
        return None
    return viraj_quickselect(arr, 0, len(arr) - 1, i)

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
i = 5
print(f"The {i}th order statistic is: {ith_order_statistic(arr, i)}")
