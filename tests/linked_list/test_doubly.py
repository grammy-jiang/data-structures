from collections.abc import Iterator
from typing import Optional
from unittest import TestCase

from data_structures.linked_list import DoublyNode
from data_structures.linked_list.doubly import DoublyLinkedList


class TestDoublyLinkedList(TestCase):
    def setUp(self) -> None:
        self.node_values = ["a", "b", "c"]

    def test_doubly_linked_list(self) -> None:
        doubly_linked_list = DoublyLinkedList(*self.node_values)

        node_1st: Optional[DoublyNode] = doubly_linked_list.head
        node_2nd: Optional[DoublyNode] = node_1st.next
        node_3rd: Optional[DoublyNode] = node_2nd.next

        self.assertIs(node_1st.value, self.node_values[0])
        self.assertIs(node_2nd.value, self.node_values[1])
        self.assertIs(node_3rd.value, self.node_values[2])

        self.assertIs(node_2nd.previous, node_1st)
        self.assertIs(node_3rd.previous, node_2nd)

        self.assertIsNone(node_1st.previous)
        self.assertIsNone(node_3rd.next)

        doubly_linked_list = DoublyLinkedList()
        self.assertIsNone(doubly_linked_list.head)

    def test_bool(self) -> None:
        doubly_linked_list = DoublyLinkedList(*self.node_values)
        self.assertTrue(bool(doubly_linked_list))

        doubly_linked_list = DoublyLinkedList()
        self.assertFalse(bool(doubly_linked_list))

    def test_contains(self) -> None:
        doubly_linked_list = DoublyLinkedList(*self.node_values)

        node = doubly_linked_list.head
        self.assertIn(node, doubly_linked_list)

        node = DoublyNode("e")
        self.assertNotIn(node, doubly_linked_list)

    def test_iter(self) -> None:
        doubly_linked_list = DoublyLinkedList(*self.node_values)
        previous = None
        for i, node in enumerate(doubly_linked_list):
            self.assertIs(self.node_values[i], node.value)
            self.assertIs(node.previous, previous)
            previous = node

    def test_len(self) -> None:
        doubly_linked_list = DoublyLinkedList(*self.node_values)
        self.assertEqual(len(doubly_linked_list), len(self.node_values))

        doubly_linked_list = DoublyLinkedList()
        self.assertEqual(len(doubly_linked_list), 0)

    def test_reserved(self) -> None:
        doubly_linked_list = DoublyLinkedList(*self.node_values)
        reversed_doubly_linked_list = reversed(doubly_linked_list)

        self.assertIsInstance(reversed_doubly_linked_list, Iterator)
        for node, i in zip(reversed_doubly_linked_list, reversed(self.node_values)):
            self.assertIs(node.value, i)

    def test_is_head(self) -> None:
        doubly_linked_list = DoublyLinkedList(*self.node_values)

        node_a = doubly_linked_list.head
        self.assertTrue(doubly_linked_list.is_head(node_a))

        node_f = DoublyNode("f")
        self.assertFalse(doubly_linked_list.is_head(node_f))

    def test_is_tail(self) -> None:
        doubly_linked_list = DoublyLinkedList(*self.node_values)
        node_a: Optional[DoublyNode] = doubly_linked_list.head
        node_b: Optional[DoublyNode] = node_a.next
        node_c: Optional[DoublyNode] = node_b.next
        self.assertTrue(doubly_linked_list.is_tail(node_c))
        self.assertFalse(doubly_linked_list.is_tail(node_b))

    def test_reverse(self) -> None:
        doubly_linked_list = DoublyLinkedList(*self.node_values)
        self.assertIsNone(doubly_linked_list.reverse())

        for node, i in zip(doubly_linked_list, reversed(self.node_values)):
            self.assertIs(node.value, i)

    def test_search(self) -> None:
        doubly_linked_list = DoublyLinkedList(*self.node_values)

        b = self.node_values[1]

        self.assertIs(doubly_linked_list.search(b).value, b)

        self.assertIsNone(doubly_linked_list.search("d"))

        doubly_linked_list = DoublyLinkedList()
        self.assertIsNone(doubly_linked_list.search("d"))

    def test_search_iter(self) -> None:
        doubly_linked_list = DoublyLinkedList(*self.node_values)

        search_iter = doubly_linked_list.search_iter("b")
        self.assertIsInstance(search_iter, Iterator)
        self.assertIs(next(search_iter).value, "b")

        search_iter = doubly_linked_list.search_iter("d")
        with self.assertRaises(StopIteration):
            _ = next(search_iter)

        doubly_linked_list = DoublyLinkedList()
        search_iter = doubly_linked_list.search_iter("d")
        with self.assertRaises(StopIteration):
            _ = next(search_iter)

    def test_tail(self) -> None:
        doubly_linked_list = DoublyLinkedList(*self.node_values)
        self.assertIs(doubly_linked_list.tail.value, self.node_values[-1])

        doubly_linked_list = DoublyLinkedList()
        self.assertIsNone(doubly_linked_list.tail)
