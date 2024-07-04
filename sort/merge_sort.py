"""
Merge Sort
"""

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    return merge(merge_sort(left), merge_sort(right))


# Example usage
if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90, 54 ,8, 65, 84, 35, 12, 5, 65, 75, 32]
    print(f"Initial array: {arr}")
    print(f"Sorted array: {merge_sort(arr)}")