#Context = type('Context', (), {})


class Context(type):
    dct = {}
    def __call__(cls, **kwds):
        pass





c = Context(a=2, d=4)
print(c.a)
