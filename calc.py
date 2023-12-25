import re
from functools import reduce

def add(*num):
    return sum(num)

def mult(*num):
    return reduce(lambda x, y: x * y, num)

def div(*num):
    return reduce(lambda x, y: x / y, num)


operators = ['+', '*', '/', '-']

def compute(op):
    op = op.replace(' ', '')
    bracket = False
    indbe = 0
    inadaf = 0
    for i in range(len(op)):
        if op[i] == '(':
            bracket =True
            indbe = i
        if op[i] == ')':
            indaf = i
    if bracket:
        res = compute(op[indbe+1:indaf])
        op = op.replace(op[indbe:indaf+1],str(res))

    dic = {}
    temp = ''
    for i in range(len(op)):
        if op[i] in operators:
            if op[i] in operators and op[i-1] in operators:
                continue
            if op[i] in ('*', '/'):
                if op[i] == temp:
                    continue
                dic[i] = 2
                
            else:
                dic[i] = 1
            temp = op[i]

    lst = list(dic.keys())
    newop = op
    for i in range(len(lst)):
        indbe = 0
        indaf = 0
        if dic[lst[i]] == 2:
            if i==0 and i==len(lst) -1:
                indbe = 0
                indaf = len(op) - 1
            elif i == 0:
                indbe = 0
                indaf = lst[i + 1] - 1
            elif i == len(lst) - 1:
                indaf = len(op) - 1
                indbe = lst[i - 1] + 1
            else:
                indaf = lst[i + 1] - 1
                indbe = lst[i - 1] + 1

            text = re.findall(r'[-+]?\d*\.\d+|\d+', op[indbe:indaf + 1])
            num = [float(j) for j in text]
            if op[lst[i]] == '*':
                res = mult(*num)
            elif op[lst[i]] == '/':
                res = div(*num)
            newop = newop.replace(op[indbe:indaf+1],str(res))
    op = newop
    numbers_with_signs = re.findall(r'[+-]?\d+', op)

    numbers = [float(num) for num in numbers_with_signs]
    res = add(*numbers)
    return res 