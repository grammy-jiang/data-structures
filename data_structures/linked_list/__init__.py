"""
The node classes used in various Linked List classes
"""
from __future__ import annotations

from typing import Any, Optional


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
