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

    def get_friends_of_name(self, name):
        if not self._head:
            return []

        friends = []
        cur = self._head

        while cur:
            if cur._name == name:
                curcur = cur._friends._head
                while curcur:
                    friends.append(curcur._name)
                    curcur = curcur._next
            cur = cur._next

        return friends




def get_friend_data():
    """
        returns linked list of friends from data from user-inputted file
    """
    filename = input('Input file: ')
    file = open(filename, 'r')

    lines = file.readlines()

    name_list = LinkedList()

    for line in lines:

        # list of friends in line
        friends = line.strip().split(' ')

        friend_1_name = friends[0]
        friend_2_name = friends[1]

        # check if name_list already has these names
        friend_1_node = name_list.find(friend_1_name)
        friend_2_node = name_list.find(friend_2_name)

        # if name_list doesn't have name of 1st friend, add node with this name to name_list
        if not friend_1_node:
            friend_1_node = Node(friend_1_name)
            name_list.add(friend_1_node)

        # if name_list doesn't have name of 2nd friend, add node with this name to name_list
        if not friend_2_node:
            friend_2_node = Node(friend_2_name)
            name_list.add(friend_2_node)

        # add the two friends to each other's _friends linked list
        friend_1_node._friends.add(Node(friend_2_name))
        friend_2_node._friends.add(Node(friend_1_name))

    return name_list



def main():
    name_list = get_friend_data()


main()
