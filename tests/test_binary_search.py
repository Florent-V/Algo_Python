from search.binary_search import binary_search

arr = [
    12, 14, 16, 20, 22,
    24, 32, 35, 41, 45,
    53, 54, 63, 67, 71,
    78, 87, 88, 91, 99
]

def test_binary_search():
  assert binary_search(arr, 88) == 17
  assert binary_search(arr, 85) == -1
  assert binary_search([], 16) == -1
