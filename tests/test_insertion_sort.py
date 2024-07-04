from sort.insertion_sort import insertion_sort

def test_sorted_array():
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted_array():
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_unsorted_array():
    assert insertion_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_empty_array():
    assert insertion_sort([]) == []

def test_single_element_array():
    assert insertion_sort([1]) == [1]
