"""
Exceptions for data structures implementation
"""


class DataStructureError(Exception):
    """
    The base exception, all exceptions in this package should derive from this one
    """


class NodeFrozenError(DataStructureError):
    """
    When a property of a frozen node is attempted to modify, this exception raises
    """


class LinkedListIndexError(DataStructureError):
    """
    When visit or remove the node not in the linked list, this exception raises
    """


# BinaryNode used in BinaryTree


class BinaryNodeError(DataStructureError):
    """
    The base exception for BinaryNode
    """


class BinaryNodeRelationshipError(BinaryNodeError):
    """
    When a parent-child relationship is invalidated, this exception raises
    """


class BinaryNodeRelationshipExistedError(BinaryNodeError):
    """
    When a parent-child relationship already exists, this exception raises
    """


class BinaryNodeChildNotExistedError(BinaryNodeError):
    """
    When visit a not existed child of a BinaryNode, this exception raises
    """
