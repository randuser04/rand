i = 0
t = 1
str_input = input("Enter the string to be parsed: ")

def E():
    T()
    EPRIME()

def EPRIME():
    global i
    if i < len(str_input) and str_input[i] == '+':
        i += 1
        T()
        EPRIME()

def T():
    F()
    TPRIME()

def TPRIME():
    global i
    if i < len(str_input) and str_input[i] == '*':
        i += 1
        F()
        TPRIME()

def F():
    global i, t
    if i < len(str_input) and str_input[i] == 'a':
        i += 1
    elif i < len(str_input) and str_input[i] == '(':
        i += 1
        E()
        if i < len(str_input) and str_input[i] == ')':
            i += 1
        else:
            error()
    else:
        error()

def error():
    global t
    t = -1

E()

if t == 1 and i == len(str_input):
    print("The given string is accepted")
else:
    print("The given string is not accepted")
