

x = 10

def f1():
    x = 1       # x is now local var
    print(x)    # 1 = local var

def f2():
    print(x)    # 10 = use global var

def f3():
    print(y)    # NameError: name 'y' is not defined

def f4():
    # UnboundLocalError: local variable 'x' referenced before assignment
    print(y)    # Read next line first. BUT y not yet bounded to value
    y = 2       # this means through f: y is local var

def f5():
    # UnboundLocalError: local variable 'x' referenced before assignment
    print(x)    # same as above. But even global x is cancelled
    x = 2

def f6():
    # UnboundLocalError: local variable 'x' referenced before assignment
    x = x + 1   # similar issue. x = make it local. right side x+1: not bound yet!

def f7():
    # UnboundLocalError: local variable 'x' referenced before assignment
    x += 1  # same as x = x+1 in binding (though a bit more efficient)

def f8():
    global x
    x += 1  # cool


f7()