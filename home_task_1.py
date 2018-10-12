class LimitExceedError(Exception):
    """
    Raises when trying to push item when stack limit exceeded.
    """
    pass


class ZeroValue(Exception):
    """
    Raises when the number is zero
    """
    pass


class EmptyStackError(Exception):
    """
    Raises when trying to pull item from empty stack.
    """
    pass


class Stack:
    """
    Class <Stack>
    Data structure based the principle of last in first out by default, it accepts values
    data_type = object, limit = None
    """

    def __init__(self, data_type=object, limit=None):
        """
        data_type: the type of data that will be stored in stack
        limit: the amount of elements that should be stored in stack
        """
        self.data_type = data_type
        self.limit = limit
        self.stack = []

        if limit == 0:
            raise ZeroValue("Number must be greater than zero!")

    def _push(self, obj):
        """
        Checks incoming element for type and limit and returns it
        """
        if not isinstance(obj, self.data_type):
            raise TypeError
        elif self.limit < self.stack.__len__():
            raise LimitExceedError("Limit over stack!")
        else:
            return obj

    def push(self, obj):
        """
        Adds element to the stack
        """
        obj = self._push(obj)
        self.stack.append(obj)

    def pull(self):
        """
        Removes an last element from the stack and returns it
        """
        if self.stack.__len__() == 0:
            raise EmptyStackError("Stack is empty!")
        else:
            return self.stack.pop()

    def count(self):
        """
        Counts the number of elements in the stack and returns it
        """
        return self.stack.__len__()

    def clear(self):
        """
        Removes all elements from the stack
        """
        self.stack.clear()

    @property
    def type(self):
        """
        Adds an object to the property
        """
        return self.data_type

    def __str__(self):
        """
        Returns a string with an object of type
        """
        return 'Stack<{}>'.format(str(self.type)[7:-1])
