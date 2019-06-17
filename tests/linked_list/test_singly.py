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

    def test_append(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)
        self.assertIsNone(singly_linked_list.append("d"))
        self.assertEqual(len(singly_linked_list), len(self.node_values) + 1)
        self.assertIs(singly_linked_list.tail.value, "d")

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

    def test_pop(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)
        node = singly_linked_list.pop()
        self.assertIs(node.value, self.node_values[-1])
        self.assertFalse(singly_linked_list.is_tail(node))
        self.assertIs(singly_linked_list.tail.value, self.node_values[-2])
        self.assertIsNone(singly_linked_list.tail.next)

    def test_replace(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)

        self.assertIsNone(singly_linked_list.replace("b", "a"))
        self.assertIs(singly_linked_list.head.next.value, "a")

        singly_linked_list.replace("a", "b")
        self.assertIs(singly_linked_list.head.value, "b")
        self.assertIs(singly_linked_list.head.next.value, "b")

        singly_linked_list.replace("b", "a", 0)
        self.assertIs(singly_linked_list.head.value, "b")

        singly_linked_list.replace("b", "a", 1)
        self.assertIs(singly_linked_list.head.value, "a")
        self.assertIs(singly_linked_list.head.next.value, "b")

        singly_linked_list = SinglyLinkedList()
        self.assertIsNone(singly_linked_list.replace("a", "b"))
        self.assertIsNone(singly_linked_list.head)
        self.assertFalse(bool(singly_linked_list))

    def test_reverse(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)
        self.assertIsNone(singly_linked_list.reverse())

        for node, i in zip(singly_linked_list, reversed(self.node_values)):
            self.assertIs(node.value, i)

    def test_search(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)

        b = self.node_values[1]

        self.assertIs(singly_linked_list.search(b).value, b)

        self.assertIsNone(singly_linked_list.search("d"))

        singly_linked_list = SinglyLinkedList()
        self.assertIsNone(singly_linked_list.search("d"))

    def test_search_iter(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)

        search_iter = singly_linked_list.search_iter("b")
        self.assertIsInstance(search_iter, Iterator)
        self.assertIs(next(search_iter).value, "b")

        search_iter = singly_linked_list.search_iter("d")
        with self.assertRaises(StopIteration):
            _ = next(search_iter)

        singly_linked_list = SinglyLinkedList()
        search_iter = singly_linked_list.search_iter("d")
        with self.assertRaises(StopIteration):
            _ = next(search_iter)

    def test_tail(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)
        self.assertIs(singly_linked_list.tail.value, self.node_values[-1])

        singly_linked_list = SinglyLinkedList()
        self.assertIsNone(singly_linked_list.tail)

