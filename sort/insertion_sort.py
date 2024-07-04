"""
Insertion Sort
"""

def insertion_sort(array):
    i = 1
    while i < len(array):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
        i += 1
    return array

# Example usage
if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90, 54 ,8, 65, 84, 35, 12, 5, 65, 75, 32]
    print(f"Initial array: {arr}")
    print(f"Sorted array: {insertion_sort(arr)}")
