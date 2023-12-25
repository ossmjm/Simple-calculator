from calc import compute
chk = True

while chk:
    op = input('please enter your operation ')
    exp =op
    res = compute(op)
    print(res)
    exp += ' = ' + str(res) + '\n'
    with open('history','a') as f:
        f.write(exp)    
    other = input('do you want to do another operation ')
    if other.lower() == 'yes':
        pass
    else:
        chk = False
