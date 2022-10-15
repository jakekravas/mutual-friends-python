class Node:
    def __init__(self, name):
        self._name = name
        self._friends = LinkedList()
        self._next = None


class LinkedList:
    def __init__(self):
        self._head = None

    def print_list(self):
        cur = self._head
        while cur:
            print (cur._name)
            cur = cur._next
