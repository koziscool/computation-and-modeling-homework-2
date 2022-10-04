

class Stack:
    '''a class to implement a stack data structure from an underlying list'''
    def __init__(self):
        self.data = []

    def push(self, elt):
        self.data.append(elt)

    def pop(self):
        return self.data.pop()

    def peek(self):
        ret_elt = self.data.pop()
        self.data.append(ret_elt)
        return ret_elt


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, elt):
        self.data.append(elt)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


