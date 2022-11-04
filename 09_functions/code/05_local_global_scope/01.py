
# global variable's scope is anywhere within the program
# glob1 are global var
glob1 = 20

def f():
    # Scope of Variables defined in a function is within the function ONLY
    # loc1 is a local variable: visible in f(), but NOT outside
    loc1 = 30
    print(loc1)
    print(glob1)    # is it in local? No. Is it in global? Yes. Use it
    return loc1


f()
print(glob1)    # ok: as global

print(loc1)     # NameError: name 'loc1' is not defined

