class Node:
    def __init__(self, name):
        self._name = name
        self._friends = LinkedList()
        self._next = None


class LinkedList:
    def __init__(self):
        self._head = None

    def add(self, new):
        new._next = self._head
        self._head = new

    def find(self, name):
        if not self._head:
            return None

        cur = self._head

        while cur:
            if cur._name == name:
                return cur
            cur = cur._next

        return None

    def print_list(self):
        cur = self._head
        while cur:
            print (cur._name)
            cur = cur._next
