class LinkedList:
    def __init__(self):
        self._head = None

    def add(self, new):
        new._next = self._head
        self._head = new

    def is_empty(self):
        return self._head == None

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

    def get_friends_of_name(self, name):
        if not self._head:
            # return None
            return []

        # friends = LinkedList()
        friends = []
        cur = self._head

        while cur:
            if cur._name == name:
                curcur = cur._friends._head
                while curcur:
                    # friends.add(curcur)
                    friends.append(curcur._name)
                    curcur = curcur._next
            cur = cur._next

        return friends

    def get_mutual_friends(self, name_1_friends, name_2_friends):
        if not self._head:
            return None

        mutual_friends = LinkedList()
        # mutual_friends.add()

        cur = self._head
        while cur:

            cur = cur._next
