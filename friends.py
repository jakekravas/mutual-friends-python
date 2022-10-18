"""
    File: friends.py
    Author: Jake Kravas
    Purpose: Display mutual friends of
    two user-inputted names, with friend
    data coming from user-inputted file
"""

from linked_list import *

def get_friend_data():
    """
        Returns linked list of friends from data from user-inputted file
    """
    filename = input('Input file: ')
    file = open(filename, 'r')

    lines = file.readlines()

    # linked list that will hold names from file
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

    file.close()
    return name_list


def display_mutual_friends(name_1_node, name_2_node):
    # if name_1_node or name_2_node is None, exit the function
    if not name_1_node or not name_2_node:
        return

    # linked list that will hold mutual friends
    mutual_friends = LinkedList()

    # head of name_1_node
    name_1_cur = name_1_node._friends._head

    while name_1_cur:

        # head of name_2_node
        name_2_cur = name_2_node._friends._head

        while name_2_cur:

            # if name of current name_2 friend == name
            # of current name_1 friend, add a node
            # containing this name to mutual_friends
            if name_2_cur._name == name_1_cur._name:
                mutual_friends.add(Node(name_1_cur._name))

            name_2_cur = name_2_cur._next

        name_1_cur = name_1_cur._next

    # if there are any mutual friends, sort and print them
    if not mutual_friends.is_empty():
        # linked list of mutual friends sorted in alphabetical order
        mutual_friends_sorted = mutual_friends.sort()

        # print mutual friends from mutual_friends_sorted
        print('Friends in common:')
        mutual_friends_sorted.print_list()


def get_names_from_input(name_list):
    name_1 = input('Name 1: ')
    name_2 = input('Name 2: ')

    # get nodes of friends for each name input
    name_1_node = name_list.find(name_1)
    name_2_node = name_list.find(name_2)

    # if a name is invalid, display error
    if not name_1_node:
        print('ERROR: Unknown person ' + name_1)
    if not name_2_node:
        print('ERROR: Unknown person ' + name_2)

    return name_1_node, name_2_node


def main():
    
    name_list = get_friend_data()

    name_1_node, name_2_node = get_names_from_input(name_list)

    display_mutual_friends(name_1_node, name_2_node)


main()
