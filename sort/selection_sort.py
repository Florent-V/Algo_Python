"""
Selection Sort
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage
if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90, 54 ,8, 65, 84, 35, 12, 5, 65, 75, 32]
    print(f"Initial array: {arr}")
    print(f"Sorted array: {selection_sort(arr)}")