"""
Abstract class for Node and Tree
"""
from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Any, Optional, Type


class Node(metaclass=ABCMeta):
    """
    Abstract Node class
    """

    def __init__(
            self,
            value: Any,
            parent: Optional[Type[Node]] = None,
            relationship: Optional[str] = None
    ):
        """
        Initial this node with the given parent and relationship with the parent

        :param value:
        :type value: Any
        :param parent:
        :type parent: Optional[Type[Node]]
        :param relationship:
        :type relationship: Optional[str]
        """

        self.value: Any = value
        self.parent: Optional[Type[Node]] = parent

        if parent is not None:
            self.parent.add_child(self, relationship)

    @property
    @abstractmethod
    def children(self):
        """
        Return all children of this node

        :return:
        """

    @property
    def depth(self) -> int:
        """
        Return the depth of this node

        :return:
        :rtype: int
        """

        if self.is_root():
            return 0
        else:
            return 1 + self.parent.depth

    @property
    def height(self) -> int:
        """
        Return the height of this node

        :return:
        :rtype: int
        """
        if self.is_leaf():
            return 0
        else:
            return 1 + max(child.height for child in self.children)

    @abstractmethod
    def add_child(self, node: Node, relationship: str):
        """
        Add the given node as a child of this node, with the given relationship

        :param node:
        :type node: Node
        :param relationship:
        :type relationship: str
        :return:
        :rtype: None
        """

    @abstractmethod
    def is_leaf(self) -> bool:
        """
        Check this node is a leaf or not

        :return:
        :rtype: bool
        """

    def is_root(self) -> bool:
        """
        Check this node is a root or not

        :return:
        :rtype: bool
        """
        return self.parent is None

    def is_sibling(self, node: Node) -> bool:
        """
        Check the given node is the sibling of this node

        :param node:
        :type node: Node
        :return:
        :rtype: bool
        """
        return node in self.parent.children

    @abstractmethod
    def remove_child(self, relationship: str):
        """

        :param relationship:
        :type relationship:
        :return:
        :rtype:
        """
