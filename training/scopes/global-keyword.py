# global keyword


x = 7

def setVar (z):
    y = z
    global x
    global a
    x = y
    a = 8

print('y before setVar: ', x)

setVar(18)
print('y after setVar: ', x)
print('a after setVar: ', a)

