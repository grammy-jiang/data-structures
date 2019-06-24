from collections.abc import Iterator
from typing import Optional
from unittest import TestCase

from data_structures.exceptions import LinkedListIndexError
from data_structures.linked_list.nodes import SinglyNode
from data_structures.linked_list.singly import (
    CircularSinglyLinkedList,
    SinglyLinkedList,
)


class TestSinglyLinkedList(TestCase):
    def setUp(self) -> None:
        self.node_values = ["a", "b", "c"]

    def test_singly_linked_list(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)

        node: Optional[SinglyNode] = singly_linked_list.head
        self.assertIs(node.value, self.node_values[0])

        node: Optional[SinglyNode] = node.next
        self.assertIs(node.value, self.node_values[1])

        node: Optional[SinglyNode] = node.next
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

        node = SinglyNode("e")
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

    def test_insert_after(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)

        node_value = "d"
        head = singly_linked_list.head
        singly_linked_list.insert_after(node_value, head)
        self.assertIs(head.next.value, node_value)

        node_value = "f"
        singly_linked_list.insert_after(node_value)
        self.assertIs(singly_linked_list.head.value, node_value)

    def test_is_head(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)

        node_a = singly_linked_list.head
        self.assertTrue(singly_linked_list.is_head(node_a))

        node_f = SinglyNode("f")
        self.assertFalse(singly_linked_list.is_head(node_f))

    def test_is_tail(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)
        node_a: Optional[SinglyNode] = singly_linked_list.head
        node_b: Optional[SinglyNode] = node_a.next
        node_c: Optional[SinglyNode] = node_b.next
        self.assertTrue(singly_linked_list.is_tail(node_c))
        self.assertFalse(singly_linked_list.is_tail(node_b))

    def test_pop(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)
        node = singly_linked_list.pop()
        self.assertIs(node.value, self.node_values[-1])
        self.assertFalse(singly_linked_list.is_tail(node))
        self.assertIs(singly_linked_list.tail.value, self.node_values[-2])
        self.assertIsNone(singly_linked_list.tail.next)

    def test_remove_after(self) -> None:
        singly_linked_list = SinglyLinkedList(*self.node_values)
        node_1st: Optional[SinglyNode] = singly_linked_list.head
        node_2nd: Optional[SinglyNode] = node_1st.next
        node_3rd: Optional[SinglyNode] = node_2nd.next
        singly_linked_list.remove_after(node_1st)
        self.assertEqual(len(singly_linked_list), len(self.node_values) - 1)
        self.assertIs(node_1st.next, node_3rd)

        singly_linked_list.remove_after(node_3rd)
        self.assertEqual(len(singly_linked_list), len(self.node_values) - 1)

        singly_linked_list = SinglyLinkedList(*self.node_values)
        node_1st = singly_linked_list.head
        node_2nd = node_1st.next
        singly_linked_list.remove_after()
        self.assertEqual(len(singly_linked_list), len(self.node_values) - 1)
        self.assertTrue(singly_linked_list.is_head(node_2nd))

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


class TestCircularSinglyLinkedList(TestCase):
    def setUp(self) -> None:
        self.node_values = ["a", "b", "c"]

    def test_circular_singly_linked_list(self) -> None:
        linked_list = CircularSinglyLinkedList(*self.node_values)

        head: Optional[SinglyNode] = linked_list.head
        self.assertIs(head.value, self.node_values[0])

        node: Optional[SinglyNode] = head.next
        self.assertIs(node.value, self.node_values[1])

        node: Optional[SinglyNode] = node.next
        self.assertIs(node.value, self.node_values[2])

        self.assertIs(node.next, head)

        linked_list = CircularSinglyLinkedList()
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

        with self.assertRaises(AttributeError):
            _ = linked_list.head.next
        with self.assertRaises(AttributeError):
            _ = linked_list.tail.next

    def test_bool(self) -> None:
        linked_list = CircularSinglyLinkedList(*self.node_values)
        self.assertTrue(bool(linked_list))

        linked_list = CircularSinglyLinkedList()
        self.assertFalse(bool(linked_list))

    def test_contains(self) -> None:
        linked_list = CircularSinglyLinkedList(*self.node_values)

        node = linked_list.head
        self.assertIn(node, linked_list)

        node = SinglyNode("e")
        self.assertNotIn(node, linked_list)

        linked_list = CircularSinglyLinkedList()

        node = SinglyNode("e")
        self.assertNotIn(node, linked_list)

    def test_iter(self) -> None:
        linked_list = CircularSinglyLinkedList(*self.node_values)

        for i, node in enumerate(linked_list):
            self.assertIs(self.node_values[i], node.value)

        linked_list = CircularSinglyLinkedList()
        iter_linked_list = iter(linked_list)

        with self.assertRaises(StopIteration):
            next(iter_linked_list)

    def test_len(self) -> None:
        linked_list = CircularSinglyLinkedList(*self.node_values)
        self.assertEqual(len(linked_list), len(self.node_values))

        linked_list = CircularSinglyLinkedList()
        self.assertEqual(len(linked_list), 0)

    def test_reserved(self) -> None:
        linked_list = CircularSinglyLinkedList(*self.node_values)
        iter_reversed_linked_list = reversed(linked_list)

        self.assertIsInstance(iter_reversed_linked_list, Iterator)
        for node, i in zip(iter_reversed_linked_list, reversed(self.node_values)):
            self.assertIs(node.value, i)

    def test_append(self) -> None:
        linked_list = CircularSinglyLinkedList(*self.node_values)
        head = linked_list.head

        self.assertIsNone(linked_list.append("d"))
        self.assertEqual(len(linked_list), len(self.node_values) + 1)

        tail = linked_list.tail
        self.assertIs(tail.value, "d")
        self.assertIs(tail.next, head)

        linked_list = CircularSinglyLinkedList()

        self.assertIsNone(linked_list.append("d"))
        self.assertEqual(len(linked_list), 1)

        head = linked_list.head
        tail = linked_list.tail
        self.assertIs(tail.value, "d")
        self.assertIs(tail.next, head)

    def test_pop(self) -> None:
        linked_list = CircularSinglyLinkedList(*self.node_values)

        tail = linked_list.tail

        node = linked_list.pop()  # return "c" node

        self.assertIs(node, tail)
        self.assertFalse(linked_list.is_tail(node))
        self.assertEqual(len(linked_list), len(self.node_values) - 1)

        tail = linked_list.tail

        self.assertIs(tail.value, self.node_values[-2])
        self.assertIs(tail.next, linked_list.head)

        _ = linked_list.pop()  # return "b" node

        _ = linked_list.pop()  # return "a" node, and linked_list is empty

        self.assertIsNone(linked_list.head)
        with self.assertRaises(LinkedListIndexError):
            linked_list.pop()

    def test_reverse(self) -> None:
        linked_list = CircularSinglyLinkedList(*self.node_values)
        self.assertIsNone(linked_list.reverse())

        for node, i in zip(linked_list, reversed(self.node_values)):
            self.assertIs(node.value, i)

    def test_search(self) -> None:
        linked_list = CircularSinglyLinkedList(*self.node_values)

        b = self.node_values[1]

        result = linked_list.search(b)
        self.assertIsInstance(result, SinglyNode)
        self.assertIs(result.value, b)

        self.assertIsNone(linked_list.search("d"))

        linked_list = SinglyLinkedList()
        self.assertIsNone(linked_list.search("d"))

    def test_search_iter(self) -> None:
        linked_list = CircularSinglyLinkedList(*self.node_values)

        search_iter = linked_list.search_iter("b")
        self.assertIsInstance(search_iter, Iterator)
        self.assertIs(next(search_iter).value, "b")

        search_iter = linked_list.search_iter("d")
        with self.assertRaises(StopIteration):
            _ = next(search_iter)

        linked_list = SinglyLinkedList()
        search_iter = linked_list.search_iter("d")
        with self.assertRaises(StopIteration):
            _ = next(search_iter)

    def test_tail(self) -> None:
        linked_list = CircularSinglyLinkedList(*self.node_values)
        head = linked_list.head
        tail = linked_list.tail
        self.assertIs(tail.value, self.node_values[-1])
        self.assertIs(tail.next, head)

        linked_list = SinglyLinkedList()
        self.assertIsNone(linked_list.tail)
