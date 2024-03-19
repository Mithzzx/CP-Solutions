class Node:
    def __init__(self, data=None, n=None):
        self.data = data
        self.next = n


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data, rev=False):
        type_list = type([])
        if type(data) == type_list:
            return self.hande_list(data, rev)

        node = Node(data, self.head)
        self.head = node

    def hande_list(self, data, rev):
        if rev is True:
            length = -len(data)
            counter = -1
            while counter >= length:
                self.insert_at_beginning(data[counter])
                counter -= 1
            return
        else:
            for i in data:
                self.insert_at_beginning(i)
            return

    def insert(self, data, index=0):
        if index == 0:
            self.insert_at_beginning(data)
        itr = self.head
        counter = 0
        while counter < index:
            if counter == index - 1:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next
            counter += 1

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        while itr:
            print(itr.data, "-->", end=" ")
            itr = itr.next


ll = LinkedList()
ll.insert_at_beginning(56)
ll.insert_at_beginning("hello")
ll.insert_at_beginning(["kapil", "opil"])
ll.insert([1, 2, 3, 4, 5])
ll.insert(6)
ll.print()
