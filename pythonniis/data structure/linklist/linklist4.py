# Circular Linked List using OOP

class Node:
    def __init__(self, ele):
        self.data = ele
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # CREATE
    def create(self):
        ch = True
        c = 0
        ptr = None

        while ch:
            c += 1
            print("Enter node", c, "data")
            ele = int(input())

            cur = Node(ele)

            if self.head is None:
                self.head = cur
                ptr = cur
                cur.next = self.head   # circular link
            else:
                ptr.next = cur
                cur.next = self.head   # last node points to head
                ptr = cur

            print("Do you continue? Press True/False")
            ch = input()

            if ch == "True":
                ch = True
            else:
                ch = False

    # DISPLAY
    def display(self):
        if self.head is None:
            print("No elements")
            return

        print("Elements are:")
        ptr = self.head

        while True:
            print(ptr.data)
            ptr = ptr.next
            if ptr == self.head:
                break

    # INSERT AT BEGINNING
    def insertbeg(self, data):
        cur = Node(data)

        if self.head is None:
            self.head = cur
            cur.next = cur
            return

        ptr = self.head

        # go to last node
        while ptr.next != self.head:
            ptr = ptr.next

        cur.next = self.head
        ptr.next = cur
        self.head = cur

        print("Inserted at beginning")

    # DELETE FROM BEGINNING
    def deletebeg(self):
        if self.head is None:
            print("No element")
            return

        if self.head.next == self.head:
            print("Deleted element =", self.head.data)
            self.head = None
            return

        ptr = self.head

        # go to last node
        while ptr.next != self.head:
            ptr = ptr.next

        print("Deleted element =", self.head.data)
        ptr.next = self.head.next
        self.head = self.head.next


# DRIVER CODE
obj = CircularLinkedList()

obj.create()
obj.display()

obj.insertbeg(5)
obj.display()

obj.deletebeg()
obj.display()