f = open('home_3.txt', 'r+', encoding='utf8')
end = f.seek(0, 2) - 1
i = 0
n = 0
if end % 2 != 0:
    finish = (end + 1)/2
else:
    finish = end / 2

while n < finish:
    f.seek(i)
    string_1 = f.read(1)
    f.seek(end)
    string_2 = f.read(1)
    f.seek(i)
    f.write(string_1)
    f.seek(end)
    f.write(string_2)
    i += 1
    end -= 1
    n += 1

f.close()