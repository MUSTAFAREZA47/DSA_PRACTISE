#  OBJECT ORIENTATION PROGRAMMING

#  CLASS ATTRIBUTES METHOD

class Bottle:
    madeOf = 'Plastic'

    def timeForFilling(self):
        print('It takes five minutes to fill')

    def __init__(self, color, size):
        self.color = color
        self.size = size


bottleOne = Bottle("Yellow", 15)
bottleTwo = Bottle("Blue", 45)


# print(bottleOne.timeForFilling())
# print(bottleTwo.__dict__)

# LINKED LIST

# Node Class Constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Print Linked List - __str__
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' --> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # Insert an Element at the beginning of singly linked list - Prepend Method
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # Insert Method in Singly Linked List
    def insert(self, index, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    # Traversal of Singly Linked List
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    # Search Method in Singly Linked List
    def search(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return False

    # Get Method in Singly Linked List
    def get(self, index):
        if index == -1:
            return self.tail.value

        if index < 0 or index >= self.length:
            return None

        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    # Set Method in Singly Linked List
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    # Pop First Method in Singly Linked List
    def pop_first(self):
        if self.length == 0:
            return None

        if self.length == 1:
            self.head = None
            self.tail = None

        popped_node = self.head
        self.head = self.head.next
        self.length -= 1
        return popped_node.value

    # Pop Last Method in Singly Linked List
    def pop_last(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
                self.tail = temp
                temp.next = None
        self.length -= 1
        return popped_node

    # Remove Method in Singly Linked List
    def remove(self, index):
        if index >= self.length or index < -1:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1 or index == -1:
            return self.pop_last()
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    # Delete All Method in Singly Linked List

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0


new_linked_list = LinkedList()
# new_linked_list.insert(0, 115)
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.prepend(320)
new_linked_list.prepend(125)
# new_linked_list.insert(3, 115)
# new_linked_list.insert(2, 1500)
# new_linked_list.insert(0, 115)
# print(new_linked_list)
# new_linked_list.traverse()
# print(new_linked_list.search(10))
# print(new_linked_list.get(1))
# print(new_linked_list.set_value(0, 1250))
# print(new_linked_list.pop_first())
# print(new_linked_list.pop_first())
# # print(new_linked_list.pop_first())
# # print(new_linked_list.pop_first())
# print(new_linked_list)
# print(new_linked_list.pop_last())
# print(new_linked_list.remove(2))
# print(new_linked_list.delete_all())
# print(new_linked_list)
