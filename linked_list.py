"""
    File: linked_list.py
    Author: Jake Kravas
    Purpose: Contains LinkedList and Node classes,
    which will be used in friends.py to
    help display display mutual friends
"""

class Node:
    """
        Holds data for name, friends, and next.
        Nodes will be added to linked list
    """
    def __init__(self, name):
        self._name = name
        self._friends = LinkedList()
        self._next = None

class LinkedList:
    """
        Linked list containing nodes that
        contain data about friends
    """
    def __init__(self):
        self._head = None

    def add(self, new):
        """
            Adds new node to beginning of linked list
        """
        new._next = self._head
        self._head = new

    def is_empty(self):
        """
            Returns boolean telling you whether
            linked list is empty or not 
        """
        return self._head == None

    def find(self, name):
        """
            If name is in linkedlist,
            returns node of that name,
            otherwise returns none 
        """
        if not self._head:
            return None

        cur = self._head

        while cur:
            if cur._name == name:
                return cur
            cur = cur._next

        return None

    def print_list(self):
        """
            Prints the name of each
            node of the linked list 
        """
        cur = self._head
        while cur:
            print (cur._name)
            cur = cur._next

    def rm_from_hd(self):
        """
            Removes first node of linked list
        """
        hd = self._head
        self._head = hd._next
        return hd

    def insert_after(self, node1, node2):
        """
            Insert node2 into linkedlist so that it comes right after node1
        """
        temp = node1._next
        node1._next = node2
        node2._next = temp

    def sort(self):
        """
            Returns linked list of self with nodes in ascending order by their _name
        """
    
        if not self._head:
            return None

        # linked list that will hold sorted version of self
        sorted_ll = LinkedList()

        cur_unsorted = self._head

        while cur_unsorted:

            # remove head of self
            self.rm_from_hd()

            name_node = Node(cur_unsorted._name)

            # if sorted is empty, add cur_unsorted unsorted val to sorted
            if sorted_ll.is_empty():
                sorted_ll.add(name_node)

            # if head of sorted is greater than cur_unsorted unsorted val, add cur_unsorted unsorted val to sorted
            elif sorted_ll._head._name > cur_unsorted._name:
                sorted_ll.add(name_node)

            # if head of sorted is less than cur_unsorted unsorted val, add current unsorted val to sorted
            else:
                
                cur_sorted = sorted_ll._head

                while cur_sorted:
                    # if current unsorted val is greater than or equal to current sorted val
                    if cur_unsorted._name >= cur_sorted._name:

                        # if next sorted val is None or next sorted val is greater than current unsorted val
                        if cur_sorted._next == None or cur_sorted._next._name > cur_unsorted._name:

                            # insert node of current unsorted val after node of current sorted
                            sorted_ll.insert_after(cur_sorted, name_node)

                    cur_sorted = cur_sorted._next

            cur_unsorted = cur_unsorted._next

        return sorted_ll
