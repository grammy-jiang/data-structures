"""
Test Cases for all Node classes
"""
from unittest import TestCase

from data_structures.linked_list import Node


class TestNode(TestCase):
    """
    The test case for the most simple Node class
    """
    def setUp(self) -> None:
        self.node_value = "node value"

    def test_node(self) -> None:
        """
        Test the initialization of Node class
        """
        node_a = Node(self.node_value)

        self.assertIs(node_a.value, self.node_value)
        self.assertIsNone(node_a.next)

        node_b = Node(self.node_value, node_a)
        self.assertIs(node_b.next, node_a)

    def test_after_node(self) -> None:
        """
        test the classmethod of Node class
        """
        node_a = Node(self.node_value)

        node_b = Node.after_node(self.node_value, node_a)
        self.assertIs(node_a.next, node_b)
