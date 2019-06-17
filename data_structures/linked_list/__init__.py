"""
The node classes used in various Linked List classes
"""
from __future__ import annotations

from typing import Any, Optional
from data_structures.exceptions import NodeFrozenError


class Node:
    """
    The most simple Node class, only contains `value` and `next` properties, and there
    is no any security mechanism for node properties modification

    Any enhanced Node class should inherit this class
    """
    def __init__(self, value: Any, next: Optional[Node] = None):
        """
        Initial a node with the given value, and its `next` property points to the given
        `next` node

        :param value: The value this node contains
        :type value: Any
        :param next: The next node that this node's `next` property points
        :type next: Optional[Node]
        """
        self.value: Any = value
        self.next: Optional[Node] = next

    @classmethod
    def after_node(cls, value: Any, node: Node):
        """
        Create a node with the given value, and after the given node

        :param value: The value that the node contains
        :type value: Any
        :param node: The node which `next` points to this node
        :type node: Node
        :return: The node created
        :rtype: Node
        """
        node.next = cls(value=value)
        return node.next


class SecureNode(Node):
    """
    A node with secure mechanism - when it is freezed, the value and next cannot be
    changed
    """
    def __init__(self, value: Any, next: Optional[Node] = None, frozen: bool = True):
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
        self._value: Optional[Node] = None
        self._next: Optional[Node] = None
        self.frozen: bool = False

        super().__init__(value, next)

        self.frozen: bool = frozen

    @classmethod
    def after_node(cls, value: Any, node: Node, frozen: bool = True):
        node.next = cls(value=value, frozen=frozen)
        return node.next

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next: Node):
        if self.frozen:
            raise NodeFrozenError
        else:
            self._next = next

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: Optional[Node]):
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
