class LimitExceedError(Exception):
    pass


class UncorrectValue(Exception):
    pass


class EmptyStackError(Exception):
    pass


class Stack:

    def __init__(self, data_type=object, limit=None):
        self.data_type = data_type
        self.limit = limit
        self.stack = []

    def _push(self, obj):
        if not isinstance(obj, self.data_type):
            raise TypeError
        elif self.limit < self.stack.__len__():
            raise LimitExceedError("Limit over stack")
        else:
            return obj

    def push(self, obj):
        obj = self._push(obj)
        self.stack.append(obj)

    def pull(self):
        if self.stack.__len__() == 0:
            raise EmptyStackError("Stack is empty")
        else:
            return self.stack.pop()

    def count(self):
        return self.stack.__len__()

    def clear(self):
        self.stack.clear()

    @property
    def type(self):
        return self.data_type

    def __str__(self):
        return 'Stack<{}>'.format(str(self.type)[7:-1])
