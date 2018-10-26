def get_sym(file, index):
    file.seek(index)
    return file.read(1)


def record(file, index, sym):
    file.seek(index)
    file.write(sym)


f = open('home_3.txt', 'r+', newline='\n')
end = f.seek(0, 2) - 1
i = 0
n = 0
if end % 2 != 0:
    finish = (end + 1)/2
else:
    finish = (end - 1)/2

while n < finish:
    sym_1 = get_sym(f, i)
    sym_2 = get_sym(f, end)
    record(f, i, sym_2)
    record(f, end, sym_1)
    i += 1
    end -= 1
    n += 1
f.close()
