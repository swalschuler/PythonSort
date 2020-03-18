def merge(a, b):
    c = []
    i, j = 0, 0

    while True:
        if i >= len(a): # no more elements in a
            while j < len(b):
                c.append(b[j])
                j += 1
            break
        if j >= len(b):
            while i < len(a):
                c.append(a[i])
                i += 1
            break

        if a[i] < b[j] and not i >= len(a):
            c.append(a[i])
            i += 1
            continue
        elif not j >= len(b):
            c.append(b[j])
            j += 1
            continue
        break
    return c



def sort(l):
    if len(l) == 1:
        return l

    a = sort(l[:int(len(l) / 2)])
    b = sort(l[int(len(l) / 2):])
    return merge(a, b)

foo = [2, 1, 3, 5, 9, 11]

blah = sort(foo)
print(blah)