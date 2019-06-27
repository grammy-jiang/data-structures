"""
Test cases for nodes in tree

"""
from collections.abc import Iterator
from unittest import TestCase

from data_structures.tree.nodes import BinaryNode
from data_structures.exceptions import (
    BinaryNodeRelationshipError,
    BinaryNodeRelationshipExistedError,
    BinaryNodeChildNotExistedError
)


class TestBinaryNode(TestCase):
    """
    Test case for BinaryNode
    """

    def setUp(self) -> None:
        self.value_a = "a"
        self.value_b = "b"
        self.value_c = "c"
        self.value_d = "d"

    def test_binary_node(self) -> None:
        """

        :return:
        """

        node_a = BinaryNode(self.value_a)

        self.assertIs(node_a.value, self.value_a)
        self.assertIsNone(node_a.parent)
        with self.assertRaises(BinaryNodeChildNotExistedError):
            _ = node_a.left_child
        with self.assertRaises(BinaryNodeChildNotExistedError):
            _ = node_a.right_child

        node_b = BinaryNode(self.value_b, node_a, "left_child")

        self.assertIs(node_b.parent, node_a)
        self.assertIs(node_a.left_child, node_b)

        node_c = BinaryNode(self.value_c, node_a, "right_child")

        self.assertIs(node_c.parent, node_a)
        self.assertIs(node_a.left_child, node_b)

    def test_children(self) -> None:
        """

        :return:
        """

        node_a = BinaryNode(self.value_a)

        node_b = BinaryNode(self.value_b, node_a, "left_child")
        node_c = BinaryNode(self.value_c, node_a, "right_child")

        node_d = BinaryNode(self.value_d, node_b, "left_child")

        self.assertSequenceEqual(node_a.children, [node_b, node_c])
        self.assertSequenceEqual(node_b.children, [node_d])
        self.assertSequenceEqual(node_c.children, [])

    def test_depth(self) -> None:
        """

        :return:
        """

        node_a = BinaryNode(self.value_a)

        node_b = BinaryNode(self.value_b, node_a, "left_child")
        node_c = BinaryNode(self.value_c, node_a, "right_child")

        node_d = BinaryNode(self.value_d, node_b, "left_child")

        self.assertEqual(node_a.depth, 0)
        self.assertEqual(node_b.depth, 1)
        self.assertEqual(node_c.depth, 1)
        self.assertEqual(node_d.depth, 2)

    def test_height(self) -> None:
        """

        :return:
        """

        node_a = BinaryNode(self.value_a)
        node_b = BinaryNode(self.value_b, node_a, "left_child")
        node_c = BinaryNode(self.value_c, node_a, "right_child")
        node_d = BinaryNode(self.value_d, node_b, "left_child")

        self.assertEqual(node_a.height, 2)
        self.assertEqual(node_b.height, 1)
        self.assertEqual(node_c.height, 0)
        self.assertEqual(node_d.height, 0)

    def test_add_child(self) -> None:
        """

        :return:
        """

        node_a = BinaryNode(self.value_a)
        node_b = BinaryNode(self.value_b)

        self.assertSequenceEqual(node_a.children, [])
        self.assertIsNone(node_a.add_child(node_b, "left_child"))
        self.assertSequenceEqual(node_a.children, [node_b])

        node_c = BinaryNode(self.value_c)

        with self.assertRaises(BinaryNodeRelationshipError):
            node_a.add_child(node_c, "right")

        with self.assertRaises(BinaryNodeRelationshipExistedError):
            node_a.add_child(node_c, "left_child")

    def test_is_leaf(self) -> None:
        """

        :return:
        """

        node_a = BinaryNode(self.value_a)
        node_b = BinaryNode(self.value_b, node_a, "left_child")
        node_c = BinaryNode(self.value_c, node_a, "right_child")
        node_d = BinaryNode(self.value_d, node_b, "left_child")

        self.assertFalse(node_a.is_leaf())
        self.assertFalse(node_b.is_leaf())
        self.assertTrue(node_c.is_leaf())
        self.assertTrue(node_d.is_leaf())

    def test_is_root(self) -> None:
        """

        :return:
        """

        node_a = BinaryNode(self.value_a)
        node_b = BinaryNode(self.value_b, node_a, "left_child")

        self.assertTrue(node_a.is_root())
        self.assertFalse(node_b.is_root())

    def test_is_sibling(self) -> None:
        """

        :return:
        """

        node_a = BinaryNode(self.value_a)
        node_b = BinaryNode(self.value_b, node_a, "left_child")
        node_c = BinaryNode(self.value_c, node_a, "right_child")
        node_d = BinaryNode(self.value_d, node_b, "left_child")

        self.assertTrue(node_b.is_sibling(node_c))
        self.assertFalse(node_d.is_sibling(node_c))
