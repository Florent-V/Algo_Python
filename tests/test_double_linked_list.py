import pytest
from data_structure.double_linked_list import DoubleLinkedList

@pytest.fixture
def double_linked_list():
    elements = [34, 7, 23, 32, 5, 62, 3, 74]
    dll = DoubleLinkedList()
    for element in elements:
        dll.add(element)
    return dll

def test_get_head(double_linked_list):
    assert double_linked_list.get_head().element == 34

def test_get_tail(double_linked_list):
    assert double_linked_list.get_tail().element == 74

def test_size(double_linked_list):
    assert double_linked_list.size() == 8

def test_is_empty(double_linked_list):
    assert not double_linked_list.is_empty()
    empty_list = DoubleLinkedList()
    assert empty_list.is_empty()

def test_print(double_linked_list):
    assert double_linked_list.print() == [34, 7, 23, 32, 5, 62, 3, 74]

def test_is_present(double_linked_list):
    assert double_linked_list.is_present(34) == 0
    assert double_linked_list.is_present(74) == 7
    assert double_linked_list.is_present(100) == -1

def test_add(double_linked_list):
    double_linked_list.add(100)
    assert double_linked_list.print() == [34, 7, 23, 32, 5, 62, 3, 74, 100]
    assert double_linked_list.get_tail().element == 100

def test_remove(double_linked_list):
    double_linked_list.remove(32)
    assert double_linked_list.print() == [34, 7, 23, 5, 62, 3, 74]
    double_linked_list.remove(34)
    assert double_linked_list.print() == [7, 23, 5, 62, 3, 74]
    assert double_linked_list.get_head().element == 7
    double_linked_list.remove(74)
    assert double_linked_list.print() == [7, 23, 5, 62, 3]
    assert double_linked_list.get_tail().element == 3

def test_remove_at(double_linked_list):
    double_linked_list.remove_at(3)
    assert double_linked_list.print() == [34, 7, 23, 5, 62, 3, 74]
    double_linked_list.remove_at(0)
    assert double_linked_list.print() == [7, 23, 5, 62, 3, 74]
    assert double_linked_list.get_head().element == 7
    double_linked_list.remove_at(5)
    assert double_linked_list.print() == [7, 23, 5, 62, 3]
    assert double_linked_list.get_tail().element == 3

def test_element_at(double_linked_list):
    assert double_linked_list.element_at(0) == 34
    assert double_linked_list.element_at(4) == 5
    assert double_linked_list.element_at(7) == 74
    assert double_linked_list.element_at(8) is None

def test_insert_at(double_linked_list):
    double_linked_list.insert_at(100, 4)
    assert double_linked_list.print() == [34, 7, 23, 32, 100, 5, 62, 3, 74]
    double_linked_list.insert_at(200, 0)
    assert double_linked_list.print() == [200, 34, 7, 23, 32, 100, 5, 62, 3, 74]
    assert double_linked_list.get_head().element == 200
    double_linked_list.insert_at(300, 10)
    assert double_linked_list.print() == [200, 34, 7, 23, 32, 100, 5, 62, 3, 74, 300]
    assert double_linked_list.get_tail().element == 300

def test_reverse(double_linked_list):
    double_linked_list.reverse()
    assert double_linked_list.print() == [74, 3, 62, 5, 32, 23, 7, 34]
    assert double_linked_list.get_head().element == 74
    assert double_linked_list.get_tail().element == 34

def test_empty_list_operations():
    dll = DoubleLinkedList()
    assert dll.is_empty()
    assert dll.size() == 0
    assert dll.print() == []
    assert dll.is_present(1) == -1
    assert dll.element_at(0) is None
    dll.remove(1)  # Should not raise an error
    dll.remove_at(0)  # Should not raise an error
    dll.insert_at(1, 0)
    assert dll.print() == [1]
    assert dll.get_head().element == 1
    assert dll.get_tail().element == 1