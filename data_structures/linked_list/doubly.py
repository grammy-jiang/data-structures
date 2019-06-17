from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Optional

from data_structures.linked_list import DoublyNode


class DoublyLinkedListIterator(Iterator):
    """

    """

    def __init__(self, doubly_linked_list: DoublyLinkedList):
        """

        :param doubly_linked_list:
        :type doubly_linked_list: DoublyLinkedList
        """
        self.singly_linked_list = doubly_linked_list
        self.current: Optional[DoublyNode] = self.singly_linked_list.head

    def __next__(self) -> DoublyNode:
        """

        :return:
        :rtype: Node
        """
        if self.current is not None:
            current: Optional[DoublyNode] = self.current
            self.current = current.next
            return current
        else:
            raise StopIteration


class DoublyLinkedList(Iterable):
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

    def __bool__(self) -> bool:
        """
        if this doubly linked list is empty return False, otherwise return True
        :return:
        :rtype: bool
        """
        return self.head is not None

    def __contains__(self, node: DoublyNode) -> bool:
        """

        :param node:
        :type node: DoublyNode
        :return:
        :rtype: bool
        """
        for _node in self:
            if node is _node:
                return True
        else:
            return False

    def __iter__(self) -> DoublyLinkedListIterator:
        """

        :return:
        :rtype: DoublyLinkedListIterator
        """
        return DoublyLinkedListIterator(self)

