import pytest
from data_structure.binary_tree import BinaryTree

@pytest.fixture
def binary_tree():
    elements = [30, 20, 40, 15, 25, 35, 45, 10, 18, 22, 28, 32, 38, 42, 48, 5, 12, 16, 24, 26, 31, 34, 39, 41, 46, 49, 3, 8, 14, 21]
    tree = BinaryTree()
    for element in elements:
        tree.insert(element)
    return tree

def test_insert_and_is_present(binary_tree):
    assert binary_tree.is_present(30)
    assert binary_tree.is_present(3)
    assert binary_tree.is_present(49)
    assert not binary_tree.is_present(100)

def test_find_min(binary_tree):
    assert binary_tree.find_min() == 3

def test_find_max(binary_tree):
    assert binary_tree.find_max() == 49

def test_find_min_height(binary_tree):
    assert binary_tree.find_min_height() == 3

def test_find_max_height(binary_tree):
    assert binary_tree.find_max_height() == 5

def test_is_balanced(binary_tree):
    assert not binary_tree.is_balanced()

def test_inorder(binary_tree):
    expected = [3, 5, 8, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 28, 30, 31, 32, 34, 35, 38, 39, 40, 41, 42, 45, 46, 48, 49]
    assert binary_tree.inorder() == expected

def test_preorder(binary_tree):
    expected = [30, 20, 15, 10, 5, 3, 8, 12, 14, 18, 16, 25, 22, 21, 24, 28, 26, 40, 35, 32, 31, 34, 38, 39, 45, 42, 41, 48, 46, 49]
    assert binary_tree.preorder() == expected

def test_postorder(binary_tree):
    expected = [3, 8, 5, 14, 12, 10, 16, 18, 15, 21, 24, 22, 26, 28, 25, 20, 31, 34, 32, 39, 38, 35, 41, 42, 46, 49, 48, 45, 40, 30]
    assert binary_tree.postorder() == expected

def test_level_order(binary_tree):
    expected = [30, 20, 40, 15, 25, 35, 45, 10, 18, 22, 28, 32, 38, 42, 48, 5, 12, 16, 21, 24, 26, 31, 34, 39, 41, 46, 49, 3, 8, 14]
    assert binary_tree.level_order() == expected

def test_reverse_level_order(binary_tree):
    expected = [3, 8, 14, 5, 12, 16, 21, 24, 26, 31, 34, 39, 41, 46, 49, 10, 18, 22, 28, 32, 38, 42, 48, 15, 25, 35, 45, 20, 40, 30]
    assert binary_tree.reverse_level_order() == expected

def test_invert(binary_tree):
    original_inorder = binary_tree.inorder()
    binary_tree.invert()
    inverted_inorder = binary_tree.inorder()
    assert inverted_inorder == list(reversed(original_inorder))

def test_remove(binary_tree):
    binary_tree.remove(20)
    assert not binary_tree.is_present(20)
    assert binary_tree.is_present(21)  # 21 should replace 20
    binary_tree.remove(3)
    assert not binary_tree.is_present(3)
    binary_tree.remove(49)
    assert not binary_tree.is_present(49)
    binary_tree.remove(30)  # removing root
    assert not binary_tree.is_present(30)
    assert binary_tree.is_present(31)  # 31 should replace 30 as root

def test_size(binary_tree):
    assert binary_tree.size() == 30

def test_empty_tree():
    empty_tree = BinaryTree()
    assert empty_tree.size() == 0
    assert empty_tree.find_min() is None
    assert empty_tree.find_max() is None
    assert empty_tree.find_min_height() == -1
    assert empty_tree.find_max_height() == -1
    assert empty_tree.is_balanced()
    assert empty_tree.inorder() == []
    assert empty_tree.preorder() == []
    assert empty_tree.postorder() == []
    assert empty_tree.level_order() == []
    assert empty_tree.reverse_level_order() == []

def test_single_node_tree():
    single_node_tree = BinaryTree()
    single_node_tree.insert(1)
    assert single_node_tree.size() == 1
    assert single_node_tree.find_min() == 1
    assert single_node_tree.find_max() == 1
    assert single_node_tree.find_min_height() == 0
    assert single_node_tree.find_max_height() == 0
    assert single_node_tree.is_balanced()
    assert single_node_tree.inorder() == [1]
    assert single_node_tree.preorder() == [1]
    assert single_node_tree.postorder() == [1]
    assert single_node_tree.level_order() == [1]
    assert single_node_tree.reverse_level_order() == [1]