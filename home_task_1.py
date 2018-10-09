
class Stack:

    def __init__(self, data_type, limit):
        self.data_type = data_type
        self.limit = limit
        self.stack = list()

        if not isinstance(self.limit, int):
            print("Введите целое число!")
        elif self.limit < 1:
            print("Введите число больше нуля!")

    def count(self):
        len(self.stack)

    def _push(self, obj):
        if not isinstance(obj, self.data_type):
            return TypeError
        elif self.limit < self.count():
            print('LimitExceedError')
        else:
            return obj

    def push(self, obj):
        obj = self._push(obj)
        self.stack.append(obj)

    def pull(self):
        if self.count() == 0:
            print('EmptyStackError')
        else:
            return self.count()

    def clear(self):
        self.stack.clear()

    def type(self):
        return self.data_type


st = Stack(int, 3)
print(st.count())