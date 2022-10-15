from linked_list import *

class Node:
    def __init__(self, name):
        self._name = name
        self._friends = LinkedList()
        self._next = None

def get_friend_data():
    """
        returns linked list of friends from data from user-inputted file
    """
    filename = input('Input file: ')
    # filename = 'in10.txt'
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


def display_mutual_friends(name_1_friends, name_2_friends):

    mutual_friends_ll = LinkedList()

    name_1_cur = name_1_friends._friends._head

    while name_1_cur:
        n1_friend = name_1_cur._name

        name_2_cur = name_2_friends._friends._head
        while name_2_cur:

            if name_2_cur._name == n1_friend:
                mutual_friends_ll.add(Node(n1_friend))
            name_2_cur = name_2_cur._next

        name_1_cur = name_1_cur._next

    if not mutual_friends_ll.is_empty():
        print('Friends in common:')
        mutual_friends_ll.print_list()


def get_friends_from_name_input(name_list):
    name_1 = input('Name 1: ')
    name_2 = input('Name 2: ')
    # name_1 = 'William'
    # name_2 = 'Abigail'

    name_1_friends = name_list.find(name_1)
    name_2_friends = name_list.find(name_2)

    return name_1_friends, name_2_friends


def main():
    name_list = get_friend_data()
    name_1_friends, name_2_friends = get_friends_from_name_input(name_list)
    display_mutual_friends(name_1_friends, name_2_friends)


main()
