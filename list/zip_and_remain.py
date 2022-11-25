

def remain(s,t):
 conc = ''
 for l, i  in zip(s,t):
    l +=i
    conc += l
 if len(s) > len:
    s,t = t,s
 conc += t[:len(s)] 
 return conc

if __name__=="__main__":
    s ,t = map(str, input().split())
    print(type(s),t)
    res = remain(s, t)
    print(res)


