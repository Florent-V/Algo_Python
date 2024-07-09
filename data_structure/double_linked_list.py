class Node:
    def __init__(self, element):
        self.element = element
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = self.tail = new_node
            return
        self._add(self.tail, new_node)

    def _add(self, current, new_node):
        if not current.next:
            current.next = new_node
            new_node.prev = current
            self.tail = new_node
        else:
            self._add(current.next, new_node)

    def remove(self, element):
        if not self.head:
            return
        if self.head.element == element:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        else:
            self._remove_recursive(self.head, element)

    def _remove_recursive(self, current, element):
        if not current:
            return
        if current.element == element:
            if current.next:
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next
            if current == self.tail:
                self.tail = current.prev
        else:
            self._remove_recursive(current.next, element)

    def size(self):
        return self._size_recursive(self.head)

    def _size_recursive(self, current):
        if not current:
            return 0
        return 1 + self._size_recursive(current.next)

    def getHead(self):
        return self.head.element if self.head else None

    def getTail(self):
        return self.tail.element if self.tail else None

    def print(self):
        return self._print_recursive(self.head)

    def _print_recursive(self, current):
        if not current:
            return []
        return [current.element] + self._print_recursive(current.next)

    def isPresent(self, element):
        return self._is_present_recursive(self.head, element, 0)

    def _is_present_recursive(self, current, element, position):
        if not current:
            return -1
        if current.element == element:
            return position
        return self._is_present_recursive(current.next, element, position + 1)

    def remove_at(self, index):
        if index < 0:
            return
        if index == 0:
            if self.head:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                else:
                    self.tail = None
        else:
            self._remove_at_recursive(self.head, index, 0)

    def _remove_at_recursive(self, current, index, current_index):
        if not current:
            return
        if current_index == index:
            if current.next:
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next
            if current == self.tail:
                self.tail = current.prev
        else:
            self._remove_at_recursive(current.next, index, current_index + 1)

    def element_at(self, index):
        return self._element_at_recursive(self.head, index, 0)

    def _element_at_recursive(self, current, index, current_index):
        if not current:
            return None
        if current_index == index:
            return current.element
        return self._element_at_recursive(current.next, index, current_index + 1)

    def insert_at(self, element, index):
        if index < 0:
            return
        new_node = Node(element)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if not self.tail:
                self.tail = new_node
        else:
            self._insert_at_recursive(self.head, new_node, index, 0)

    def _insert_at_recursive(self, current, new_node, index, current_index):
        if not current:
            if current_index == index:
                self.tail = new_node
                if self.tail.prev:
                    self.tail.prev.next = self.tail
            return
        if current_index + 1 == index:
            new_node.next = current.next
            new_node.prev = current
            if current.next:
                current.next.prev = new_node
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node
        else:
            self._insert_at_recursive(current.next, new_node, index, current_index + 1)

    def reverse(self):
        self._reverse_recursive(self.head)
        self.head, self.tail = self.tail, self.head

    def _reverse_recursive(self, current):
        if not current:
            return
        current.prev, current.next = current.next, current.prev
        if not current.prev:
            return current
        return self._reverse_recursive(current.prev)
    


if __name__ == "__main__":
    elements = [34, 7, 23, 32, 5, 62, 3, 74, 45, 17, 29, 76, 11, 8, 4, 67, 21, 13, 33, 9]
    linked_list = DoubleLinkedList()
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