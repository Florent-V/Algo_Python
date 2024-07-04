"""
Quick Sort
"""

def quick_sort_base(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_base(left) + middle + quick_sort_base(right)

def partition(array, low, high):
    pivot = array[high]
    curseur = low

    for i in range(low, high):
        if array[i] < pivot:
            array[curseur], array[i] = array[i], array[curseur]
            curseur += 1

    array[curseur], array[high] = array[high], array[curseur]
    return curseur

def quick_sort_optimized(array, low, high):
    if low < high:
        curseur = partition(array, low, high)
        quick_sort_optimized(array, low, curseur - 1)
        quick_sort_optimized(array, curseur + 1, high)
    return array

def quick_sort(array):
    return quick_sort_optimized(array, 0, len(array) - 1)


# Example usage
if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90, 54 ,8, 65, 84, 35, 12, 5, 65, 75, 32]
    print(f"Initial array: {arr}")
    print(f"Sorted array: {quick_sort(arr)}")