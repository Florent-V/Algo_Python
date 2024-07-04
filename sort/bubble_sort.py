"""
A Python implementation of the bubble sort algorithm.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Example usage
if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90, 54 ,8, 65, 84, 35, 12, 5, 65, 75, 32]
    print(f"Initial array: {arr}")
    print(f"Sorted array: {bubble_sort(arr)}")