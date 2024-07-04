# test_sorting.py
from sort.bubble_sort import bubble_sort
import unittest

def test_sorted_array():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted_array():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_unsorted_array():
    assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_empty_array():
    assert bubble_sort([]) == []

def test_single_element_array():
    assert bubble_sort([1]) == [1]


class TestBubbleSort(unittest.TestCase):
    
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([64, 25, 12, 22, 11]), [11, 12, 22, 25, 64])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(bubble_sort([2, 1]), [1, 2])
        self.assertEqual(bubble_sort([5, 1, 4, 2, 8]), [1, 2, 4, 5, 8])

if __name__ == '__main__':
    unittest.main()