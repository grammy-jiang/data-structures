from typing import Optional

from data_structures.linked_list import DoublyNode


class DoublyLinkedList:
    def __init__(self, *args):
        """

        :param args:
        """
        self.head: Optional[DoublyNode] = None

        if args:
            self.head = DoublyNode(value=args[0])
            current_node = self.head
            for i in args[1:]:
                current_node = DoublyNode(i, previous=current_node)
