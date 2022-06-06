def ebatnaxui(a, b = ''):
    for element in a.split():
        if len(element) >= 5:
            c = ''.join(reversed(element))
            b += c + ''
        else:
            b += element + ' '
    return b[:-1]
            

a = input()
print(ebatnaxui(a))
