from itertools import product
from tabulate import tabulate

def conjunction(a, b):
    return a and b

def disjunction(a, b):
    return a or b

def negation(a):
    return not a

def implication(a, b):
    return disjunction(negation(b), a)

def equivalence(a, b):
    return a == b

d = {
    '^': 'conjunction(stack.pop(),stack.pop())',
    'v': 'disjunction(stack.pop(),stack.pop())',
    '=': 'equivalence(stack.pop(),stack.pop())', 
    '~': 'negation(stack.pop())', 
    '>': 'implication(stack.pop(),stack.pop())'
}

def calctruthtable(f):
    vals={} 
    header=[]
    row=[]
    truthtable=[] 
    print(f'Truth table for formula "{f}"')
    for char in f: 
        if char not in d:
            vals[char]='' 
    for key in vals.keys():
        header.append(key)  
    header.append('result')
    for elem in product((0,1),repeat=len(vals.keys())):
        for pos,key in enumerate(vals.keys()):
            vals[key]=elem[pos]  
        stack=[]
        for char in f:
            if char in d:
                temp = eval(d[char])
                stack.append(temp)
            else:
                stack.append(vals[char]) 
        
        row=list(vals.values())
        row.append(int(stack.pop())) 
        truthtable.append(row) 
    result = tabulate(truthtable, headers=header, tablefmt="pretty")
    return result  
if __name__=='__main__':
    print(calctruthtable(input('Input your formula here\n')))
