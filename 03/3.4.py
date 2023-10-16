class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    #  增
    def append(self, key):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    #  删
    def delete(self, value):
        if self.head is None:
            return
        if self.head.key == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.key == value:
                current.next = current.next.next
                return
            current = current.next

    # 改
    def update(self, pos, new_key):
        if self.head is None:
            return
        current = self.head
        position = 0
        while current:
            if position == pos:
                current.key = new_key
                return
            current = current.next
            position += 1

    # 查
    def search(self, value):
        current = self.head
        while current:
            if current.key == value:
                return True
            current = current.next
        return False

    # 打印链表
    def display(self):
        current = self.head
        while current:
            print(current.key, end=" -> ")
            current = current.next
        print("None")
