from collections.abc import Iterator
from typing import Optional
from unittest import TestCase

from data_structures.linked_list import Node
from data_structures.linked_list.singly import SinglyLinkedList


class TestSinglyLinkedList(TestCase):
    def setUp(self) -> None:
        self.node_values = ["a", "b", "c"]

    def test_singly_linked_list(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)

        node: Optional[Node] = singly_linked_list.head
        self.assertIs(node.value, self.node_values[0])

        node: Optional[Node] = node.next
        self.assertIs(node.value, self.node_values[1])

        node: Optional[Node] = node.next
        self.assertIs(node.value, self.node_values[2])

        self.assertIsNone(node.next)

        singly_linked_list = SinglyLinkedList()
        self.assertIsNone(singly_linked_list.head)

        with self.assertRaises(AttributeError):
            _ = singly_linked_list.head.next

    def test_bool(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)
        self.assertTrue(bool(singly_linked_list))

        singly_linked_list = SinglyLinkedList()
        self.assertFalse(bool(singly_linked_list))

    def test_contains(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)

        node = singly_linked_list.head
        self.assertIn(node, singly_linked_list)

        node = Node("e")
        self.assertNotIn(node, singly_linked_list)

    def test_iter(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)
        for node, value in zip(singly_linked_list, self.node_values):
            self.assertIs(node.value, value)

        for i, node in enumerate(singly_linked_list):
            self.assertIs(self.node_values[i], node.value)

    def test_len(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)
        self.assertEqual(len(singly_linked_list), len(self.node_values))

        singly_linked_list = SinglyLinkedList()
        self.assertEqual(len(singly_linked_list), 0)

    def test_reserved(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)
        reversed_singly_linked_list = reversed(singly_linked_list)

        self.assertIsInstance(reversed_singly_linked_list, Iterator)
        for node, i in zip(reversed_singly_linked_list, reversed(self.node_values)):
            self.assertIs(node.value, i)

    def test_tail(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)
        self.assertIs(singly_linked_list.tail.value, self.node_values[-1])

        singly_linked_list = SinglyLinkedList()
        self.assertIsNone(singly_linked_list.tail)

    def test_is_head(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)

        node_a = singly_linked_list.head
        self.assertTrue(singly_linked_list.is_head(node_a))

        node_f = Node("f")
        self.assertFalse(singly_linked_list.is_head(node_f))

    def test_is_tail(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)
        node_a: Optional[Node] = singly_linked_list.head
        node_b: Optional[Node] = node_a.next
        node_c: Optional[Node] = node_b.next
        self.assertTrue(singly_linked_list.is_tail(node_c))
        self.assertFalse(singly_linked_list.is_tail(node_b))

