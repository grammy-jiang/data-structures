"""
The node classes used in various Linked List classes
"""
from __future__ import annotations

from typing import Any, Optional

from data_structures.exceptions import NodeFrozenError
from data_structures.linked_list import Node as _Node


class SinglyNode(_Node):
    @classmethod
    def after_node(cls, value: Any, node: SinglyNode) -> SinglyNode:
        """
        Create a node with the given value, and after the given node

        :param value: The value that the node contains
        :type value: Any
        :param node: The node which `next` points to this node
        :type node: SinglyNode
        :return: The node created
        :rtype: SinglyNode
        """
        node.next = cls(value=value)
        return node.next


class SecureSinglyNode(SinglyNode):
    """
    A node with secure mechanism - when it is frozen, the value and next cannot be
    changed
    """

    def __init__(
            self,
            value: Any,
            next: Optional[SecureSinglyNode] = None,
            frozen: bool = True
    ):
        """
        Initial a node with secure mechanism, and as default the node is frozen to
        change after initialized

        :param value:
        :type value: Any
        :param next:
        :type next: Optional[Node]
        :param frozen:
        :type frozen: bool
        """
        self._value: Optional[SecureSinglyNode] = None
        self._next: Optional[SecureSinglyNode] = None
        self.frozen: bool = False

        super().__init__(value, next)

        self.frozen: bool = frozen

    @classmethod
    def after_node(
            cls, value: Any, node: SecureSinglyNode, frozen: bool = True
    ) -> SecureSinglyNode:
        """
        Create a node with the given value, and after the given node

        :param value: The value that the node contains
        :type value: Any
        :param node: The node which `next` points to this node
        :type node: SinglyNode
        :param frozen:
        :type frozen: bool
        :return: The node created
        :rtype: SinglyNode
        """
        node.next = cls(value=value, frozen=frozen)
        return node.next

    @property
    def next(self) -> Optional[SecureSinglyNode]:
        """

        :return: Optional[SecureSinglyNode]
        """
        return self._next

    @next.setter
    def next(self, next: SecureSinglyNode) -> None:
        """

        :param next:
        :type next: SecureSinglyNode
        :return:
        :rtype: None
        """
        if self.frozen:
            raise NodeFrozenError
        else:
            self._next = next

    @property
    def value(self) -> Any:
        """

        :return:
        :rtype: Any
        """
        return self._value

    @value.setter
    def value(self, value: Optional[SecureSinglyNode]) -> None:
        """

        :param value:
        :type value: Optional[SecureSinglyNode]
        :return:
        """
        if self.frozen:
            raise NodeFrozenError
        else:
            self._value = value

    def freeze(self) -> None:
        """
        Freeze this node - the value and next cannot be changed

        :return:
        :rtype: None
        """
        self.frozen = True

    def unfreeze(self) -> None:
        """
        Unfreeze this node - the value and next can be changed

        :return:
        :rtype: None
        """
        self.frozen = False


class DoublyNode(_Node):
    """
    The most simple DoublyNode class, only contains `value` and `next` properties, and
    there is no any security mechanism for node properties modification

    Any enhanced DoublyNode class should inherit this class
    """

    def __init__(
            self,
            value: Any,
            previous: Optional[DoublyNode] = None,
            next: Optional[DoublyNode] = None,
    ):
        """

        :param value:
        :type value: Any
        :param previous:
        :type previous: Optional[DoublyNode]
        :param next:
        :type next: Optional[DoublyNode]
        """
        super().__init__(value, next)

        self.previous: Optional[DoublyNode] = previous
        if previous:
            previous.next = self

        self.next: Optional[DoublyNode] = next
        if next:
            next.previous = self

    @classmethod
    def after_node(cls, value: Any, node: DoublyNode) -> DoublyNode:
        """
        Create a node with the given value, and after the given node

        :param value: The value that the node contains
        :type value: Any
        :param node: The node which `next` points to this node
        :type node: DoublyNode
        :return: The node created
        :rtype: DoublyNode
        """
        return cls(value, node)
