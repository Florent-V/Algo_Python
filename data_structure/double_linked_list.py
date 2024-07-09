class Node:
    def __init__(self, element):
        self.element = element
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail
    
    def size(self):
        return self._size(self.head)

    def _size(self, current):
        if not current:
            return 0
        return 1 + self._size(current.next)

    def is_empty(self):
        return self.head is None

    def print(self):
        return self._print(self.head)

    def _print(self, current):
        if not current:
            return []
        return [current.element] + self._print(current.next)

    def is_present(self, element):
        return self._is_present(self.head, element, 0)

    def _is_present(self, current, element, position):
        if not current:
            return -1
        if current.element == element:
            return position
        return self._is_present(current.next, element, position + 1)

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
            return
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
            return
        self._remove(self.head, element)

    def _remove(self, current, element):
        if not current:
            return
        if current.element == element:
            if current.next:
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next
            if current == self.tail:
                self.tail = current.prev
            return
        self._remove(current.next, element)

    def remove_at(self, index):
        if index < 0 or index >= self.size() or not self.head:
            return
        if index == 0:
            if self.head:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                else:
                    self.tail = None
            return
        self._remove_at(self.head, index, 0)

    def _remove_at(self, current, index, current_index):
        if not current:
            return
        if current_index == index:
            if current.next:
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next
            if current == self.tail:
                self.tail = current.prev
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
        new_node = Node(element)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if not self.tail:
                self.tail = new_node
            return
        self._insert_at(self.head, new_node, index, 0)

    def _insert_at(self, current, new_node, index, current_index):
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
            return
        self._insert_at(current.next, new_node, index, current_index + 1)

    def reverse(self):
        self._reverse(self.head)
        self.head, self.tail = self.tail, self.head

    def _reverse(self, current):
        if not current:
            return
        current.prev, current.next = current.next, current.prev
        if not current.prev:
            return current
        return self._reverse(current.prev)
    


if __name__ == "__main__":
    elements = [34, 7, 23, 32, 5, 62, 3, 74, 45, 17, 29, 76, 11, 8, 4, 67, 21, 13, 33, 9]
    dll = DoubleLinkedList()
    print("isEmpty", dll.is_empty())

    for element in elements:
        dll.add(element)

    print("isEmpty", dll.is_empty())
    print("size", dll.size())
    print("get_head", dll.get_head().element)
    print("get_tail", dll.get_tail().element)
    print("print", dll.print())
    print("is_present 74", dll.is_present(74))
    print("is_present 92", dll.is_present(92))
    print("add 85", dll.add(85))
    print("print", dll.print())
    print("size", dll.size())

    print("remove 62", dll.remove(62))
    print("print", dll.print())
    print("remove 12", dll.remove(12))
    print("print", dll.print())

    print("remove_at 5", dll.remove_at(5))
    print("print", dll.print())

    print("remove_at 40", dll.remove_at(40))
    print("print", dll.print())

    print("element_at 5", dll.element_at(5))
    print("element_at 40", dll.element_at(40))

    print("insert_at 10 at 3", dll.insert_at(10, 3))
    print("print", dll.print())
    print("insert_at 10 at 40", dll.insert_at(10, 40))
    print("print", dll.print())

    print("reverse", dll.reverse())
    print("print", dll.print())
