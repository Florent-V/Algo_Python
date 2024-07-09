class Node:
    def __init__(self, element):
        """
        Initialize a Node object with an element and a reference to the next node.
        """
        self.element = element
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        return self.head is None
    
    def size(self):
        return self._size(self.head)

    def _size(self, current_node):
        if not current_node:
            return 0
        return 1 + self._size(current_node.next)
    
    def print_list(self):
        return self._print_list(self.head, [])

    def _print_list(self, current_node, arr=[]):
        """
        Print the elements of the linked list.
        """
        if not current_node:
            return arr
        arr.append(current_node.element)
        return self._print_list(current_node.next, arr)
    
    def add(self, element):
        if not self.head:
            self.head = Node(element)
            return
        self._add(element, self.head)
    
    def _add(self, element, current_node):
        if not current_node.next:
            current_node.next = Node(element)
            return
        self._add(element, current_node.next)
    
    
    def isPresent(self, element):
        return self._is_present(self.head, element, 0)

    def _is_present(self, current, element, position):
        if not current:
            return -1
        if current.element == element:
            return position
        return self._is_present(current.next, element, position + 1)
    
    def remove(self, element):
        if not self.head:
            return
        if self.head.element == element:
            self.head = self.head.next
            return
        self._remove(self.head, element)

    def _remove(self, current, element):
        if not current.next:
            return
        if current.next.element == element:
            current.next = current.next.next
            return
        self._remove(current.next, element)

    def remove_at(self, index):
        if index < 0 or index >= self.size() or not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        self._remove_at(self.head, index, 0)

    def _remove_at(self, current, index, current_index):
        if not current or not current.next:
            return
        if current_index + 1 == index:
            current.next = current.next.next
            return
        self._remove_at(current.next, index, current_index + 1)

    def element_at(self, index):
        return self._element_at(self.head, index, 0)

    def _element_at(self, current, index, current_index):
        if not current:
            return None
        if current_index == index:
            return current.element
        return self._element_at(current.next, index, current_index + 1)
    
    def insert_at(self, element, index):
        if index < 0 or index > self.size():
            return
        if index == 0:
            new_node = Node(element)
            new_node.next = self.head
            self.head = new_node
            return
        self._insert_at(self.head, element, index, 0)

    def _insert_at(self, current, element, index, current_index):
        if not current:
            return
        if current_index + 1 == index:
            new_node = Node(element)
            new_node.next = current.next
            current.next = new_node
            return
        self._insert_at(current.next, element, index, current_index + 1)


    def reverse(self):
        self.head = self._reverse(self.head)

    def _reverse(self, current):
        if not current or not current.next:
            return current

        new_head = self._reverse(current.next)
        current.next.next = current
        current.next = None
        return new_head



if __name__ == "__main__":
    elements = [34, 7, 23, 32, 5, 62, 3, 74, 45, 17, 29, 76, 11, 8, 4, 67, 21, 13, 33, 9]
    linked_list = LinkedList()
    print("isEmpty", linked_list.is_empty())

    for element in elements:
        linked_list.add(element)

    print("isEmpty", linked_list.is_empty())
    print("size", linked_list.size())
    print("print", linked_list.print_list())
    print("isPresent 74", linked_list.isPresent(74))
    print("isPresent 92", linked_list.isPresent(92))
    print("get_head", linked_list.get_head().element)
    print("add 85", linked_list.add(85))
    print("print", linked_list.print_list())
    print("size", linked_list.size())
    print("add 85", linked_list.add(12))
    print("print", linked_list.print_list())
    print("size", linked_list.size())
    print("remove 62", linked_list.remove(62))
    print("print", linked_list.print_list())
    print("remove 12", linked_list.remove(12))
    print("print", linked_list.print_list())

    print("remove_at 5", linked_list.remove_at(5))
    print("print", linked_list.print_list())

    print("remove_at 40", linked_list.remove_at(40))
    print("print", linked_list.print_list())

    print("element_at 5", linked_list.element_at(5))
    print("element_at 40", linked_list.element_at(40))


    print("insert_at 10 at 3", linked_list.insert_at(10, 3))
    print("print", linked_list.print_list())
    print("insert_at 10 at 40", linked_list.insert_at(10, 40))
    print("print", linked_list.print_list())

    print("reverse", linked_list.reverse())
    print("print", linked_list.print_list())




