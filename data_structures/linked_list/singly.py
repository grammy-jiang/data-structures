from __future__ import annotations

from collections.abc import Iterator
from typing import Optional

from data_structures.linked_list import Node


class SinglyLinkedListIterator(Iterator):
    """

    """
    def __init__(self, singly_linked_list: SinglyLinkedList):
        """

        :param singly_linked_list:
        :type singly_linked_list: SinglyLinkedList
        """
        self.singly_linked_list = singly_linked_list
        self.current: Optional[Node] = self.singly_linked_list.head

    def __next__(self) -> Node:
        """

        :return:
        :rtype: Node
        """
        if self.current is not None:
            current: Optional[Node] = self.current
            self.current = current.next
            return current
        else:
            raise StopIteration


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

    def __bool__(self) -> bool:
        """
        if this singly linked list is empty return False, otherwise return True
        :return:
        :rtype: bool
        """
        return self.head is not None

    def __contains__(self, node: Node) -> bool:
        """

        :param node:
        :type node: Node
        :return:
        :rtype: bool
        """
        for _node in self:
            if node is _node:
                return True
        else:
            return False

    def __iter__(self) -> SinglyLinkedListIterator:
        """

        :return:
        :rtype: SinglyLinkedListIterator
        """
        return SinglyLinkedListIterator(self)

