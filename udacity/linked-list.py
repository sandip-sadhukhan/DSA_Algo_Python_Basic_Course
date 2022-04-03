"""
Implementation of Linked List data structure
"""


class Element:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: "Element" | None = None


class LinkedList:
    def __init__(self, head: None | Element = None) -> None:
        self.head: Element | None = head

    def get_position(self, position: int) -> int | None:
        current: Element | None = self.head

        for _ in range(position - 1):
            if current is not None:
                current = current.next
            else:
                return None

        if current is not None:
            return current.value
        else:
            return None

    def __prepend(self, element: Element) -> None:
        """
        It will add elememt at the 0th position
        """
        element.next = self.head
        self.head = element

    def append(self, element: Element) -> None:
        """
        It will add elememt at the end position
        """
        current: Element | None = self.head

        if current is None:
            self.head = element
            return

        while current.next is not None:
            current = current.next

        current.next = element

    def insert(self, position: int, element: Element) -> None:
        if position <= 0:
            print("Invalid position, please enter correct value.")
            return
        elif position == 1:
            return self.__prepend(element)
        prev: Element | None = self.head

        if prev is None:
            print("length is smaller than position")
            return

        for _ in range(1, position - 1):
            if prev.next is not None:
                prev = prev.next
            else:
                print("length is smaller than position")
                return

        element.next = prev.next
        prev.next = element

    def __deleteFirstNode(self) -> None:
        if self.head is not None:
            self.head = self.head.next
        else:
            print("Linkedlist is empty")

    def delete(self, value: int) -> None:
        current: Element | None = self.head

        if current is None:
            print("Linkedlist is empty")
            return

        if current.value == value:
            return self.__deleteFirstNode()

        while current.next is not None:

            if current.next.value == value:
                # delete node
                deletedNode: Element = current.next
                current.next = deletedNode.next
                deletedNode.next = None
                return
            else:
                current = current.next

        print("Value was not in the linkedlist.")

    def __str__(self) -> str:
        result: str = ""
        current: Element | None = self.head
        if current is not None:
            result += "Linkedlist: "
            while current:
                result += f"{str(current.value)}, "
                current = current.next
        else:
            result = "Linkedlist is empty"
        return result


e1 = Element(10)
e2 = Element(20)
e3 = Element(30)

ll = LinkedList(head=e1)
ll.append(e2)
ll.append(e3)

print("----------")
print(ll)

print("----------")
print("2nd element : ", ll.get_position(2))
print("3rd element: ", ll.get_position(3))
print("4th element: ", ll.get_position(4))

print("-------")
e4 = Element(40)
e5 = Element(50)
e6 = Element(60)
ll.insert(1, e4)
print(ll)
ll.insert(5, e5)
print(ll)
ll.insert(3, e6)
print(ll)

print("-------")
ll.delete(40)
print(ll)
ll.delete(30)
print(ll)
ll.delete(50)
print(ll)
ll.delete(50)
print(ll)
