"""
The linked list with only one link property node

 * Singly Linked List
 * Circular Singly Linked List
"""
from __future__ import annotations

from collections.abc import Iterator, Reversible
from typing import Any, List, Optional, Union

from data_structures.exceptions import LinkedListIndexError
from data_structures.linked_list import LinkedList
from data_structures.linked_list.nodes import SinglyNode


class SinglyLinkedListIterator(Iterator):  # pylint: disable=too-few-public-methods
    """
    Iterator for Singly Linked List
    """

    def __init__(self, singly_linked_list: SinglyLinkedList):
        """

        :param singly_linked_list:
        :type singly_linked_list: SinglyLinkedList
        """
        self.singly_linked_list = singly_linked_list
        self.cursor: Optional[SinglyNode] = self.singly_linked_list.head

    def __next__(self) -> SinglyNode:
        """

        :return:
        :rtype: SinglyNode
        """
        if self.cursor:
            cursor: Optional[SinglyNode] = self.cursor
            self.cursor = cursor.next
            return cursor
        raise StopIteration


class SinglyLinkedListReversedIterator(  # pylint: disable=too-few-public-methods
        SinglyLinkedListIterator
):
    """
    Reversed Iterator for Singly Linked List
    """

    def __init__(self, singly_linked_list: SinglyLinkedList):
        """

        :param singly_linked_list:
        :type singly_linked_list: SinglyLinkedList
        """
        super(SinglyLinkedListReversedIterator, self).__init__(singly_linked_list)

        self._reversed_singly_linked_list: SinglyLinkedList = SinglyLinkedList()

        _: Optional[SinglyNode] = None
        node: Optional[SinglyNode] = None

        for i in self.singly_linked_list:
            node = SinglyNode(i.value)
            node.next = _

        self._reversed_singly_linked_list.head = node
        self.cursor = node


class SinglyLinkedListSearchIterator(  # pylint: disable=too-few-public-methods
        SinglyLinkedListIterator
):
    """
    Search Iterator for Singly Linked List
    """

    def __init__(self, singly_linked_list: SinglyLinkedList, value: Any):
        """

        :param singly_linked_list:
        :type singly_linked_list: SinglyLinkedList
        :param value:
        :type value: Any
        """
        super(SinglyLinkedListSearchIterator, self).__init__(singly_linked_list)
        self.value = value

    def __next__(self) -> SinglyNode:
        """

        :return:
        :rtype: SinglyNode
        """
        while True:
            current: Optional[SinglyNode] = self.cursor
            try:
                self.cursor = current.next
            except AttributeError:  # if the singly linked list is empty
                raise StopIteration
            if current.value == self.value:
                return current
            if current.next is None:
                raise StopIteration


class SinglyLinkedList(LinkedList, Reversible):
    """
    This is the simple singly linked list:

    * have only one head point, no tail pointer

    """

    def _init(self, *args) -> None:
        if args:
            self.head = SinglyNode(value=args[0])
            current_node = self.head
            for i in args[1:]:
                current_node = SinglyNode.after_node(i, current_node)

    def __iter__(self) -> SinglyLinkedListIterator:
        """

        :return:
        :rtype: SinglyLinkedListIterator
        """
        return SinglyLinkedListIterator(self)

    def __reversed__(self) -> SinglyLinkedListReversedIterator:
        """

        :return:
        :rtype: SinglyLinkedListReversedIterator
        """
        return SinglyLinkedListReversedIterator(self)

    def append(self, value: Any) -> None:
        """
        Append a node after the tail of this singly linked list

        :param value:
        :type value: Any
        :return:
        :rtype: None
        """
        _ = SinglyNode.after_node(value, self.tail)

    def insert_after(
            self, value: Union[SinglyNode, Any], node: Optional[SinglyNode] = None
    ) -> None:
        """
        If after_node is not provided, the given value will be insert to the beginning
        of this singly linked list

        :param value:
        :type value: Union[Node, Any]
        :param node:
        :type node: Optional[Node]
        :return:
        :rtype: None
        """
        if not isinstance(value, SinglyNode):
            value = SinglyNode(value)

        if node:
            value.next, node.next = node.next, value
        else:
            value.next, self.head = self.head, value

    def pop(self) -> SinglyNode:
        """
        Pop the last node of this singly linked list

        :return:
        :rtype: SinglyNode
        """
        last_two_nodes: List[Optional[SinglyNode]] = [None, None]
        for node in self:
            last_two_nodes = [last_two_nodes[1], node]

        last_two_nodes[0].next = None

        return last_two_nodes[1]

    def remove_after(self, node: Optional[SinglyNode] = None) -> None:
        """
        Remove one node after the give node


        :param node: If after_node is not provided, the first node of this singly linked
                     list will be removed
        :type node: Optional[Node]
        :return:
        :rtype: None
        """
        if not self:  # for empty linked list nothing happens
            return

        if node is None:  # remove the first node
            self.head = self.head.next
        else:
            for node_ in self:
                if node is node_:
                    if node.next is None:
                        # the give node is the last node in singly linked list, nothing
                        # is removed
                        return
                    node.next = node.next.next

    def replace(self, old: Any, new: Any, max_: Optional[int] = None) -> None:
        """
        In-place replace the node old value with the given new one

        Complexity:
          - Space: Θ(n), Ο(n), Ω(1)
          - Time: Θ(n), Ο(n), Ω(1)

        :param old: The old value to be replaced
        :type old: Any
        :param new: The new value to replace the old one
        :type new: Any
        :param max_: if max is not provided all of nodes equaled to old will be changed to new
        :type max_: Optional[int]
        :return: This method is a in-place change and returns None
        :rtype: None
        """
        for node in self:
            if max_ == 0:
                break

            if node.value == old:
                node.value = new

            if max_ is None:
                continue
            else:
                max_ -= 1

    def reverse(self) -> None:
        """
        In-place reverse

        :return:
        :rtype: None
        """
        _: Optional[SinglyNode] = None
        node: Optional[SinglyNode] = None

        for node in self:
            node.next, _ = _, node

        self.head = node

    def search_iter(self, value: Any) -> SinglyLinkedListSearchIterator:
        """
        Search for a given value, return a iterator

        :param value:
        :type value: Any
        :return:
        :rtype: Iterator
        """
        return SinglyLinkedListSearchIterator(self, value)


class CircularSinglyLinkedListIterator(Iterator):
    """

    """

    def __init__(self, circular_singly_linked_list: CircularSinglyLinkedList):
        """

        :param circular_singly_linked_list:
        """
        self.circular_singly_linked_list = circular_singly_linked_list

        self.head = self.circular_singly_linked_list.head
        self.cursor = self.head

        self._stop_iteration: bool = False if self.head else True

    def __next__(self) -> SinglyNode:
        """

        :return:
        """

        if self._stop_iteration:
            raise StopIteration
        else:
            cursor = self.cursor
            self.cursor = cursor.next

            if cursor.next is self.head:
                self._stop_iteration = True

            return cursor


class CircularSinglyLinkedListReversedIterator(Iterator):
    """
    An reversed iterator of CircularSinglyLinkedList
    """

    # TODO: this class needs to improve the code quality

    def __init__(self, circular_singly_linked_list: CircularSinglyLinkedList):
        """

        :param circular_singly_linked_list:
        :type circular_singly_linked_list: CircularSinglyLinkedList
        """

        _: Optional[SinglyNode] = None
        node: Optional[SinglyNode] = None

        for i in circular_singly_linked_list:
            node = SinglyNode(i)
            node.next, _ = _, node

        self.linked_list = CircularSinglyLinkedList()
        self.linked_list.head = node

        self.iter_linked_list = iter(self.linked_list)

    def __next__(self) -> SinglyNode:
        """

        :return:
        :rtype: SinglyNode
        """

        try:
            node = next(self.iter_linked_list)
        except AttributeError:
            raise StopIteration
        else:
            return node.value


class CircularSinglyLinkedListSearchIterator(Iterator):
    def __init__(self, circular_singly_linked_list: CircularSinglyLinkedList, value: Any):
        self.circular_singly_linked_list = circular_singly_linked_list
        self.value = value
        self.iter_circular_singly_linked_list = iter(self.circular_singly_linked_list)

    def __next__(self) -> SinglyNode:
        while True:
            node = next(self.iter_circular_singly_linked_list)
            if node.value == self.value:
                return node


class CircularSinglyLinkedList(LinkedList):
    """

    """

    def _init(self, *args) -> None:
        if args:
            self.head = SinglyNode(value=args[0])
            current_node = self.head
            for i in args[1:]:
                current_node = SinglyNode.after_node(i, current_node)
            current_node.next = self.head

    def __iter__(self) -> CircularSinglyLinkedListIterator:
        return CircularSinglyLinkedListIterator(self)

    def __reversed__(self) -> CircularSinglyLinkedListReversedIterator:
        return CircularSinglyLinkedListReversedIterator(self)

    def append(self, value: Any) -> None:
        """

        :param value:
        :type value: Any
        :return:
        :rtype: None
        """
        if self:  # check this circular linked list is empty or not
            SinglyNode.after_node(value, self.tail).next = self.head
        else:
            self.head = SinglyNode(value)
            self.head.next = self.head

    def pop(self) -> SinglyNode:
        """

        :return:
        :rtype: SinglyNode
        """
        if not self:  # check the circular linked list is emtpy or not
            raise LinkedListIndexError
        elif len(self) == 1:
            node = self.head
            self.head = None
            return node
        else:
            last_two_nodes: List[Optional[SinglyNode]] = [None, None]
            for node in self:
                last_two_nodes = [last_two_nodes[1], node]

            last_two_nodes[0].next = self.head

            return last_two_nodes[1]

    def reverse(self) -> None:
        """
        In-place reverse

        :return:
        :rtype: None
        """
        _: Optional[SinglyNode] = None
        node: Optional[SinglyNode] = None

        for node in self:
            node.next, _ = _, node

        self.head.next, self.head = node, node

    def search_iter(self, value: Any):
        return CircularSinglyLinkedListSearchIterator(self, value)
