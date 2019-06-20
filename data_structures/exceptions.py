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
