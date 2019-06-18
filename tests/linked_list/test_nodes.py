"""
Test Cases for all Node classes
"""
from unittest import TestCase

from data_structures.exceptions import NodeFrozenError
from data_structures.linked_list.nodes import DoublyNode, SecureSinglyNode, SinglyNode


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
        node_a = SinglyNode(self.node_value)

        self.assertIs(node_a.value, self.node_value)
        self.assertIsNone(node_a.next)

        node_b = SinglyNode(self.node_value, node_a)
        self.assertIs(node_b.next, node_a)

    def test_after_node(self) -> None:
        """
        test the classmethod of Node class
        """
        node_a = SinglyNode(self.node_value)

        node_b = SinglyNode.after_node(self.node_value, node_a)
        self.assertIs(node_a.next, node_b)


class TestSecureNode(TestCase):
    def setUp(self) -> None:
        self.node_value: str = "node value"

    def test_node(self) -> None:
        """

        """
        node_a = SecureSinglyNode(self.node_value)

        self.assertIs(node_a.value, self.node_value)
        self.assertIsNone(node_a.next)
        self.assertTrue(node_a.frozen)

        node_b = SecureSinglyNode(self.node_value, node_a)

        self.assertIs(node_b.next, node_a)

        with self.assertRaises(NodeFrozenError):
            node_c = SecureSinglyNode.after_node(self.node_value, node_a)

    def test_after_node(self) -> None:
        """
        test the classmethod of Node class
        """
        node_a = SecureSinglyNode(self.node_value, frozen=False)

        node_b = SecureSinglyNode.after_node(self.node_value, node_a)
        self.assertIs(node_a.next, node_b)
        self.assertTrue(node_b.frozen)

    def test_freeze_and_unfreeze(self):
        node_a = SecureSinglyNode(self.node_value)

        self.assertIsNone(node_a.unfreeze())
        self.assertFalse(node_a.frozen)

        self.assertIsNone(node_a.freeze())
        self.assertTrue(node_a.frozen)


class TestDoublyNode(TestCase):
    """
    The test case for the most simple Node class
    """

    def setUp(self) -> None:
        self.node_value = "node value"

    def test_node(self) -> None:
        """
        Test the initialization of Node class
        """
        node_a = DoublyNode(self.node_value)

        self.assertIs(node_a.value, self.node_value)
        self.assertIsNone(node_a.previous)
        self.assertIsNone(node_a.next)

        node_b = DoublyNode(self.node_value, node_a)
        self.assertIs(node_a.next, node_b)
        self.assertIs(node_b.previous, node_a)
