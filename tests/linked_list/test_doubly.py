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
        singly_linked_list = DoublyLinkedList(*self.node_values)
        self.assertTrue(bool(singly_linked_list))

        singly_linked_list = DoublyLinkedList()
        self.assertFalse(bool(singly_linked_list))

    def test_iter(self) -> None:
        doubly_linked_list = DoublyLinkedList(*self.node_values)
        previous = None
        for i, node in enumerate(doubly_linked_list):
            self.assertIs(self.node_values[i], node.value)
            self.assertIs(node.previous, previous)
            previous = node
