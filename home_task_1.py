
class Stack:

    def __init__(self, data_type=object, limit=None):
        self.data_type = data_type
        self.limit = limit
        self.stack = []

        if not isinstance(self.limit, int):
            print("Введите целое число!")
        elif self.limit < 1:
            print("Введите число больше нуля!")

    def _push(self, obj):
        if not isinstance(obj, self.data_type):
            return TypeError
        elif self.limit < self.stack.__len__():
            print('LimitExceedError')
        else:
            return obj

    def push(self, obj):
        obj = self._push(obj)
        self.stack.append(obj)

    def pull(self):
        if self.stack.__len__() == 0:
            print('EmptyStackError')
        else:
            index = self.stack.__len__() - 1
            return self.stack.pop(index)

    def clear(self):
        self.stack.clear()

    def type(self):
        return self.data_type


if __name__ == '__main__':
    st = Stack(str, 3)
    stack = st.stack
    st.push('rew')
    print(stack)
    print(st.pull())
    print(stack)
    st.clear()
    print(stack)
