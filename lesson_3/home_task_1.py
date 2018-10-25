def read_end_position(file):
    with open(file, 'r+')as infile:
        infile.seek(0, 2)
        return infile.tell()


def read_file_position(file, qty_sym):
    def uncloser(pos):
        with open(file, 'r+') as infile:
            if pos <= qty_sym:
                string = infile.read(pos)
                infile.write(string[::-1])
                return 0
            else:
                infile.seek(pos - qty_sym)
                pos = infile.tell()
                string = infile.read(qty_sym)
                infile.write(string[::-1])
                return pos
    return uncloser


if __name__ == '__main__':
    w = read_end_position('home_3.txt')
    r = read_file_position('home_3.txt', 2)
    while w:
        if w == 0:
            break
        w = r(w)


