# Doubly Circular Linked List using OOP

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    # CREATE
    def create(self):
        ch = True
        while ch:
            data = int(input("Enter data: "))
            self.insert_end(data)

            ch = input("Continue? True/False: ")
            if ch == "True":
                ch = True
            else:
                ch = False

    # INSERT AT END
    def insert_end(self, data):
        cur = Node(data)

        if self.head is None:
            self.head = cur
            cur.next = cur
            cur.prev = cur
        else:
            last = self.head.prev

            last.next = cur
            cur.prev = last

            cur.next = self.head
            self.head.prev = cur

    # DISPLAY FORWARD
    def display(self):
        if self.head is None:
            print("No elements")
            return

        print("Elements (Forward):")
        ptr = self.head

        while True:
            print(ptr.data, end=" ")
            ptr = ptr.next
            if ptr == self.head:
                break
        print()

    # DISPLAY REVERSE
    def display_reverse(self):
        if self.head is None:
            print("No elements")
            return

        print("Elements (Reverse):")
        ptr = self.head.prev   # start from last node

        while True:
            print(ptr.data, end=" ")
            ptr = ptr.prev
            if ptr == self.head.prev:
                break
        print()

    # INSERT AT BEGINNING
    def insert_beg(self, data):
        cur = Node(data)

        if self.head is None:
            self.head = cur
            cur.next = cur
            cur.prev = cur
        else:
            last = self.head.prev

            cur.next = self.head
            cur.prev = last

            last.next = cur
            self.head.prev = cur

            self.head = cur

        print("Inserted at beginning")

    # DELETE FROM BEGINNING
    def delete_beg(self):
        if self.head is None:
            print("No element")
            return

        if self.head.next == self.head:
            print("Deleted:", self.head.data)
            self.head = None
            return

        last = self.head.prev

        print("Deleted:", self.head.data)

        self.head = self.head.next
        self.head.prev = last
        last.next = self.head


# DRIVER CODE
obj = DoublyCircularLinkedList()

obj.create()
obj.display()

obj.insert_beg(5)
obj.display()

obj.display_reverse()

obj.delete_beg()
obj.display()