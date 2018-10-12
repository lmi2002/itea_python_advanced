def unpacker(*args):
    a_list = list()
    for arg in args:
        if isinstance(arg, list):
            for item in arg:
                a_list.append(item)
        else:
            a_list.append(arg)

    return a_list


print(unpacker(1, 2, [1, 2, [1, 3]], [1, 2, 3]))
