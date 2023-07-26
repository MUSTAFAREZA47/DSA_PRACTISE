# ++++++++++++++++++ STACK DATA STRUCTURE +++++++++++++++

#  ----> CREATE STACK USING LIST WITHOUT SIZE LIMIT
class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty list
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # push method
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"

    # pop method
    def pop(self):
        if self.isEmpty():
            return "There is not any elements in the stack"
        else:
            return self.list.pop()

    # peek method
    def peek(self):
        if self.isEmpty():
            return "There is not any elements in the stack"
        else:
            return self.list[len(self.list) - 1]

    # delete method
    def delete(self):
        self.list = None


customStack = Stack()

customStack.push(1)
customStack.push(2)
customStack.push(3)


# print(customStack)
# # customStack.pop()
# print("peek method")
# # customStack.pop()
# print(customStack.peek())
# print(customStack)


#  ----> CREATE STACK USING LIST WITH SIZE LIMIT
class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    #  Push
    def push(self, value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"

    # Pop
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()

    # peek
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list) - 1]

    #  delete
    def delete(self):
        self.list = None


# customStack = Stack(5)

# customStack.push(1)
# customStack.push(2)
# customStack.push(3)
# customStack.pop()
# customStack.delete()


# print(customStack)

# -----> STACK IN LINKED LIST
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node


# CustomStack = Stack()
# print(customStack.push(5))


