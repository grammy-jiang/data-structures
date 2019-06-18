from __future__ import annotations

from collections.abc import Container, Iterator, Reversible, Sized
from typing import Any, List, Optional, Union

from data_structures.linked_list.nodes import Node


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


class SinglyLinkedListReversedIterator(SinglyLinkedListIterator):
    """

    """

    def __init__(self, singly_linked_list: SinglyLinkedList):
        """

        :param singly_linked_list:
        :type singly_linked_list: SinglyLinkedList
        """
        super(SinglyLinkedListReversedIterator, self).__init__(singly_linked_list)

        self._reversed_singly_linked_list: SinglyLinkedList = SinglyLinkedList()
        _: Optional[Node] = None
        node: Optional[Node] = None
        for i in self.singly_linked_list:
            node = Node(i.value)
            node.next = _
        else:
            self._reversed_singly_linked_list.head = node
            self.current = node


class SinglyLinkedListSearchIterator(SinglyLinkedListIterator):
    """

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

    def __next__(self) -> Node:
        """

        :return:
        :rtype: Node
        """
        while True:
            current: Optional[Node] = self.current
            try:
                self.current = current.next
            except AttributeError:  # if the singly linked list is empty
                raise StopIteration
            if current.value == self.value:
                return current
            if current.next is None:
                raise StopIteration


class SinglyLinkedList(Container, Reversible, Sized):
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
        _ = Node.after_node(value, self.tail)

    def insert_after(
            self, value: Union[Node, Any], node: Optional[Node] = None
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
        if not isinstance(value, Node):
            value = Node(value)

        if node:
            value.next, node.next = node.next, value
        else:
            value.next, self.head = self.head, value

    def is_head(self, node: Node) -> bool:
        """
        Check if the given node is the head of this singly linked list

        Complexity:
          - Space: Θ(1), Ο(1), Ω(1)
          - Time: Θ(1), Ο(1), Ω(1)

        :param node:
        :type node: Node
        :return: If the given node is the head of this singly linked list, return True,
                 otherwise False
        :rtype: bool
        """
        return node is self.head

    def is_tail(self, node: Node) -> bool:
        """
        Check if the given node is the tail of this singly linked list

        Complexity:
          - Space: Θ(1), Ο(1), Ω(1)
          - Time: Θ(1), Ο(1), Ω(1)

        :param node:
        :type node: Node
        :return: If the given node is the tail of this singly linked list, return True,
                 otherwise False
        :rtype: bool
        """
        return node is self.tail

    def pop(self):
        last_two_nodes: List[Optional[Node], Optional[Node]] = [None, None]
        for node in self:
            last_two_nodes = [last_two_nodes[1], node]

        last_two_nodes[0].next = None

        return last_two_nodes[1]

    def remove_after(self, node: Optional[Node] = None) -> None:
        """
        Remove one node after the give node


        :param node: If after_node is not provided, the first node of this singly linked
                     list will be removed
        :type node: Optional[Node]
        :return:
        :rtype: None
        """
        if not len(self):  # for empty linked list nothing happens
            return

        if node is None:  # remove the first node
            self.head = self.head.next
        else:
            for n in self:
                if node is n:
                    if node.next is None:
                        # the give node is the last node in singly linked list, nothing
                        # is removed
                        return
                    else:
                        node.next = node.next.next

    def replace(self, old: Any, new: Any, max: Optional[int] = None) -> None:
        """
        In-place replace the node old value with the given new one

        Complexity:
          - Space: Θ(n), Ο(n), Ω(1)
          - Time: Θ(n), Ο(n), Ω(1)

        :param old: The old value to be replaced
        :type old: Any
        :param new: The new value to replace the old one
        :type new: Any
        :param max: if max is not provided all of nodes equaled to old will be changed to new
        :type max: Optional[int]
        :return: This method is a in-place change and returns None
        :rtype: None
        """
        for node in self:
            if max == 0:
                break

            if node.value == old:
                node.value = new

            if max is None:
                continue
            else:
                max -= 1

    def reverse(self) -> None:
        """
        In-place reverse

        :return:
        :rtype: None
        """
        _ = None
        node: Optional[Node] = None
        for node in self:
            node.next, _ = _, node
        else:
            self.head = node

    def search(self, value: Any) -> Optional[Node]:
        """
        Search for a given value, return immediately when the first node is found

        :param value:
        :type value: Any
        :return:
        :rtype: Optional[Node]
        """
        for node in self:
            if node.value == value:
                return node
        else:
            return None

    def search_iter(self, value: Any) -> SinglyLinkedListSearchIterator:
        """
        Search for a given value, return a iterator

        :param value:
        :type value: Any
        :return:
        :rtype: Generator[Node, None, None]
        """
        return SinglyLinkedListSearchIterator(self, value)

    @property
    def tail(self):
        """
        Because this property has a getter method, this block is empty
        """

    @tail.getter
    def tail(self) -> Optional[Node]:
        """
        The tail node of this singly linked list

        :return:
        :rtype: Optional[Node]
        """
        node: Optional[Node] = None
        for node in self:
            pass
        else:
            return node
