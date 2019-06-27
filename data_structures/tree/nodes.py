"""
Nodes used in Trees class:

 * BinaryNode
"""
from __future__ import annotations

from typing import Any, Iterator, List, Optional

from data_structures.exceptions import (
    BinaryNodeRelationshipError,
    BinaryNodeRelationshipExistedError,
    BinaryNodeChildNotExistedError
)
from data_structures.tree import Node

RELATIONSHIP = ["left_child", "right_child"]


class BinaryNode(Node):
    """

    """

    def __init__(
            self,
            value: Any,
            parent: Optional[BinaryNode] = None,
            relationship: Optional[str] = None
    ):
        """

        :param value:
        :type value: Any
        :param parent:
        :type parent: Optional[BinaryNode]
        :param left_child:
        :type left_child: Optional[BinaryNode]
        :param right_child:
        :type right_child: Optional[BinaryNode]
        """

        self._left_child: Optional[BinaryNode] = None
        self._right_child: Optional[BinaryNode] = None

        super().__init__(value, parent, relationship)

    @property
    def children(self) -> List[BinaryNode]:
        """

        :return:
        :rtype: List[BinaryNode]
        """

        children: List[BinaryNode] = []
        try:
            children.append(self.left_child)
        except BinaryNodeChildNotExistedError:
            pass

        try:
            children.append(self.right_child)
        except BinaryNodeChildNotExistedError:
            pass

        return children

    @property
    def left_child(self):
        if self._left_child:
            return self._left_child
        raise BinaryNodeChildNotExistedError

    @left_child.setter
    def left_child(self, node: BinaryNode):
        self.add_child(node, "left_child")

    @property
    def right_child(self):
        if self._right_child:
            return self._right_child
        raise BinaryNodeChildNotExistedError

    @right_child.setter
    def right_child(self, node: BinaryNode):
        self.add_child(node, "right_child")

    def add_child(self, node: BinaryNode, relationship: str) -> None:
        """

        :param node:
        :type node: BinaryNode
        :param relationship:
        :type relationship: str
        :return:
        :rtype: None
        """
        if relationship not in RELATIONSHIP:
            raise BinaryNodeRelationshipError

        try:
            _ = getattr(self, relationship)
        except BinaryNodeChildNotExistedError:
            setattr(self, "_" + relationship, node)
        else:
            raise BinaryNodeRelationshipExistedError

    def is_leaf(self) -> bool:
        """

        :return:
        :rtype: bool
        """

        return self._left_child is None and self._right_child is None

    def remove_child(self, relationship: str) -> None:
        """

        :param relationship:
        :type relationship: str
        :return:
        :rtype: None
        """

        if relationship not in RELATIONSHIP:
            raise BinaryNodeRelationshipError

        setattr(self, "_" + relationship, None)
