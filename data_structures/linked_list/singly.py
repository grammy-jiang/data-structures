"""
The linked list with only one link property node

 * Singly Linked List
 * Circular Singly Linked List
"""
from __future__ import annotations

from collections.abc import Iterator, Reversible
from typing import Any, List, Optional, Union

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

    def __bool__(self) -> bool:
        """
        if this singly linked list is empty return False, otherwise return True
        :return:
        :rtype: bool
        """
        return self.head is not None

    def __iter__(self) -> SinglyLinkedListIterator:
        """

        :return:
        :rtype: SinglyLinkedListIterator
        """
        return SinglyLinkedListIterator(self)

    def __len__(self) -> int:
        """

        :return:
        :rtype: int
        """
        _len = 0
        for _ in self:
            _len += 1
        return _len

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

    def is_head(self, node: SinglyNode) -> bool:
        """
        Check if the given node is the head of this singly linked list

        Complexity:
          - Space: Θ(1), Ο(1), Ω(1)
          - Time: Θ(1), Ο(1), Ω(1)

        :param node:
        :type node: SinglyNode
        :return: If the given node is the head of this singly linked list, return True,
                 otherwise False
        :rtype: bool
        """
        return node is self.head

    def is_tail(self, node: SinglyNode) -> bool:
        """
        Check if the given node is the tail of this singly linked list

        Complexity:
          - Space: Θ(1), Ο(1), Ω(1)
          - Time: Θ(1), Ο(1), Ω(1)

        :param node:
        :type node: SinglyNode
        :return: If the given node is the tail of this singly linked list, return True,
                 otherwise False
        :rtype: bool
        """
        return node is self.tail

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

    def search(self, value: Any) -> Optional[SinglyNode]:
        """
        Search for a given value, return immediately when the first node is found

        :param value:
        :type value: Any
        :return:
        :rtype: Optional[SinglyNode]
        """
        for node in self:
            if node.value == value:
                return node

        return None

    def search_iter(self, value: Any) -> SinglyLinkedListSearchIterator:
        """
        Search for a given value, return a iterator

        :param value:
        :type value: Any
        :return:
        :rtype: Iterator
        """
        return SinglyLinkedListSearchIterator(self, value)

    @property
    def tail(self):
        """
        Because this property has a getter method, this block is empty
        """

    @tail.getter
    def tail(self) -> Optional[SinglyNode]:
        """
        The tail node of this singly linked list

        :return:
        :rtype: Optional[SinglyNode]
        """
        node: Optional[SinglyNode] = None

        for node in self:
            pass

        return node
