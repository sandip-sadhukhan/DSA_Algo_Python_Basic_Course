"""
Implementation of stack using list & linkedlist
"""

# using list
stack_list: list[int] = [3, 4, 5]
stack_list.append(6)
stack_list.append(7)
print(stack_list)
stack_list.pop()
print(stack_list)
print("-------------")


# using linkedlist
class Element:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: "Element" | None = None


class LinkedList:
    def __init__(self, head: None | Element = None) -> None:
        self.head: Element | None = head

    def append(self, new_element: Element) -> None:
        "It will add elememt at the end position"

        current: Element | None = self.head

        if current is None:
            self.head = new_element
            return

        while current.next is not None:
            current = current.next

        current.next = new_element

    def insert_first(self, new_element: Element) -> None:
        "Insert new element as the head of the LinkedList"
        new_element.next = self.head
        self.head = new_element

    def delete_first(self) -> Element | None:
        "Delete the first (head) element in the LinkedList as return it"
        deletedNode: Element | None = self.head
        if deletedNode is not None:
            self.head = deletedNode.next
            deletedNode.next = None
            return deletedNode

        return None


class Stack:
    def __init__(self, top: Element | None) -> None:
        self.ll = LinkedList(top)

    def push(self, new_element: Element) -> None:
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self) -> Element | None:
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print(stack.pop().value)  # type: ignore
print(stack.pop().value)  # type: ignore
print(stack.pop().value)  # type: ignore
print(stack.pop())
stack.push(e4)
print(stack.pop().value)  # type: ignore
