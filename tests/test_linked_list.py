import pytest
from data_structure.linked_list import LinkedList

@pytest.fixture
def linked_list():
    elements = [34, 7, 23, 32, 5, 62, 3, 74]
    linked_list = LinkedList()
    for element in elements:
        linked_list.add(element)
    return linked_list

def test_add(linked_list):
    linked_list.add(100)
    assert linked_list.print_list() == [34, 7, 23, 32, 5, 62, 3, 74, 100]

def test_remove(linked_list):
    linked_list.remove(32)
    assert linked_list.print_list() == [34, 7, 23, 5, 62, 3, 74]

def test_size(linked_list):
    assert linked_list.size() == 8

def test_get_head(linked_list):
    assert linked_list.get_head().element == 34

def test_print(linked_list):
    assert linked_list.print_list() == [34, 7, 23, 32, 5, 62, 3, 74]

def test_is_present(linked_list):
    assert linked_list.is_present(34) == 0
    assert linked_list.is_present(62) == 5
    assert linked_list.is_present(74) == 7
    assert linked_list.is_present(100) == -1

def test_remove_at(linked_list):
    linked_list.remove_at(3)
    assert linked_list.print_list() == [34, 7, 23, 5, 62, 3, 74]

def test_element_at(linked_list):
    assert linked_list.element_at(0) == 34
    assert linked_list.element_at(4) == 5
    assert linked_list.element_at(7) == 74
    assert linked_list.element_at(8) is None

def test_insert_at(linked_list):
    linked_list.insert_at(100, 4)
    assert linked_list.print_list() == [34, 7, 23, 32, 100, 5, 62, 3, 74]

def test_reverse(linked_list):
    linked_list.reverse()
    assert linked_list.print_list() == [74, 3, 62, 5, 32, 23, 7, 34]

def test_empty_list():
    ll = LinkedList()
    assert ll.size() == 0
    assert ll.get_head() is None
    assert ll.print_list() == []
    assert ll.is_present(1) == -1

def test_single_element():
    ll = LinkedList()
    ll.add(1)
    assert ll.size() == 1
    assert ll.get_head().element == 1
    assert ll.print_list() == [1]
    ll.reverse()
    assert ll.print_list() == [1]