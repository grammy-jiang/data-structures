from typing import Optional

from data_structures.linked_list import Node


class SinglyLinkedList:
    """
    This is the simple singly linked list:

    * have only one head point, no tail pointer

    """

    def __init__(self, *args):
        """

        :param args:
        """
        self.head: Optional[Node] = None

        if args:
            self.head = Node(value=args[0])
            current_node = self.head
            for i in args[1:]:
                current_node = Node.after_node(i, current_node)
