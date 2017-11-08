statements = []
atomic = True
while atomic == True:
    user = input("Premise: ")
    if user != '':
        statements.append([i for i in user])
    else:
        atomic = False

statements.append(input("Conclusion: "))


operators = ['(',')','-','&','v','>']

# Figure out the variables
var = []
for state in statements:
    for i in state:
        if (i not in operators 
                and i not in var 
                and i != ' '):
            var.append(i)

#All possible T/F combinations

lines = 2**(len(var))

possible = []
for row in range(lines):
    var_case = {}
    for column in range(len(var)):
        if row % 2**(len(var) - column) < 2**((len(var)-(column + 1))):
            var_case[var[column]] = "T"
        else:
            var_case[var[column]] = "F"
    possible.append(var_case) 



#rules
def imply_result(a,b):
    if a == "T" and b == "T":
            return "T"
    if a == "T" and b == "F":
            return "F"
    if a == "F" and b == "T":
            return "T"
    if a == "F" and b == "F":
            return "T"
        

def and_result(a,b):
    if a == "T" and b == "T":
            return "T"
    if a == "T" and b == "F":
            return "F"
    if a == "F" and b == "T":
            return "F"
    if a == "F" and b == "F":
            return "F"


def or_result(a,b):
    if a == "T" and b == "T":
            return "T"
    if a == "T" and b == "F":
            return "T"
    if a == "F" and b == "T":
            return "T"
    if a == "F" and b == "F":
            return "F"

def not_result(a):
    if a == "T":
            return "F"
    if a == "F":
            return "T"


def substitute(a, num):
    a = [possible[num][i] if i in var else i if i in operators else ' ' for i in a]
    return [i for i in a if i != ' ']

#def parser(a)
#    b = []
#    op = min([a.find(i) for i in [">","&","v"]]
#
#    return b

def solver(a):
    #solves parantheses first
    if "(" in a:
        first = a.index("(") 
        a.reverse()
        last = len(a) - a.index(")") - 1
        a.reverse()
        b = solver(a[first+1:last])
        a = a[0:first] + b + a[last+1:]


    #solves not statements
    a.reverse()
    solved_nots = False
    while solved_nots == False:
        if "-" in a:
            ind = a.index("-")
            replace = not_result(a[ind-1])
            a.insert(ind-1, replace) 
            a.pop(ind)
            a.pop(ind)
        else:
            solved_nots = True
    a.reverse()

    #solves the rest
    for i in range(len([i for i in a if i in operators])):
        o = a[1]
        if o == "&":
            sub = and_result(a[0], a[2])
            for i in range(3):
                a.pop(0)
            a.insert(0, sub)
        elif o == "v":
            sub = or_result(a[0], a[2])
            for i in range(3):
                a.pop(0)
            a.insert(0, sub)
        elif o == ">":
            sub = imply_result(a[0], a[2])
            for i in range(3):
                a.pop(0)
            a.insert(0, sub)
    return a

#centers result
def center(a, length):
    beg = True
    while len(a) != length:
        if beg == True:
            a.insert(0," ")
        else:
            a.append(" ")
        beg = not beg
    return a 


def table(a):

    
    print()
    print()

#first line

    for i in var:
        print(i, end = " ")

    for i in statements:
        print("|", end = " ")

        print("".join(i), end = " ")

    print()

#second line
    for i in range(len(var)):
        print("--", end = "")

    for state in statements:
        print("|", end = "")
        for i in range(len(state)+2):
            print("-", end = "")
      
    print()

#meat of table
    for case in possible:

        for c in case:
                print(case[c], end = " ")

        results = []
        for state in statements:
            results.append(solver(substitute(state, possible.index(case))))
            print("|", end = " ")
             
            print("".join(center(solver(substitute(state, possible.index(case))), len(state))), end = " ")
        
        if results[-1] == ["F"] and results[:-1] == [["T"] for i in results[:-1]]:
            a = False
            print("<---", end = "")

        print()
    return a

a = True
b = table(a)
if b:
    print("Valid!")
else:
    print("Invalid!")

#for testing
#print(solver(substitute(state, 1)))

