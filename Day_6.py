# ++++++++  CIRCULARLY LINKEDLIST ++++++++++++
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.tail.next:
                break
            node = node.next

    # Creation of circular singly linked list
    def createCSLL(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
        return "The Circular Linked List has been created"

    #     Insertion of a node in circular singly linked list
    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            elif location == 1:
                new_node.next = self.tail.next
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                temp_node = temp_node.next
                temp_node.next = new_node
                new_node.next = temp_node
            return "The node has been successfully inserted"

    #  Traversal in circular singly linked list
    def traversalCSLL(self):
        if self.head is None:
            return "There is no element in list"
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    break

    #  Searching in circular singly linked list
    def searchCSLL(self, value):
        if self.head is None:
            return "There is no element in CSLL"
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == value:
                    return temp_node.value
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    return "The node does not exist in this CSLL"

    #  Delete in circular singly linked list
    def deleteNode(self, location):
        if self.head is None:
            return "There is not any node in list"
        else:
            # delete element from beginning
            if location == 0:
                # if element is one in list
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None
                # if element is more than one in list
                else:
                    self.head = self.head.next
                    self.tail.next = self.head

            # delete element from end
            elif location == 1:
                # if element is one in list
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None
                else:
                    new_node = self.head
                    while new_node is None:
                        if new_node.next == self.tail:
                            break
                        new_node = new_node.next
                    new_node.next = self.head
                    self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next

    #  Delete Entire in circular singly linked list
    def deleteEntireCSLL(self):
        self.head = None
        self.tail = None
        self.tail.next = None


circularSLL = CircularSinglyLinkedList()

circularSLL.createCSLL(1)
circularSLL.createCSLL(12)
circularSLL.insertCSLL(0, 0)
circularSLL.insertCSLL(2, 1)
circularSLL.insertCSLL(4, 1)
# print(circularSLL.traversalCSLL())
# print(circularSLL.searchCSLL(10))
print(circularSLL.deleteNode(0))
circularSLL.deleteEntireCSLL()
print([node.value for node in circularSLL])
