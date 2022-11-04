
# from  my_module import arr  as mx
# import  my_module 



# x=dir(my_module)
# print(x)

# print(greating("Abdallah"))


# import http.server

# import my_module.arr
# # tuble 

# x ,y, z = ("a","f",4)


# print(type(y))

# print(x ,y,z )

# ------------------default argument 


# def hello(x=4,y=2):

# #              SyntaxError: non-default argument follows default argumentjedi

#   print(x,y)

# hello(x=100,x=200 )
# -----------------------
# -computr sum 


# def comput_sum(n):

#   sum=0

#   for i in range(1,n):

#     sum+=i
#   print(sum)  



# comput_sum(5)


# ----------------print parameters------------

# print("Abdallah","hello ",sep="dd",end="d")

# def f(n):
#   res =1
#   while n:

#     n-=1
#     res *=2

#   return res


#   print(f(10))  
  
#____________________tuble return type 
# 
# 
 
# def test(a,b,c):


#   return [a ,b,b]


# print(test(4, 5, 5))  
# _______________________emuration 


# or indx ,el in enumerate(range(100)) :
#   print(indx+2,el+1)






# ____________________-___function overrifing 
# def f(x=100):


#   print(x)

# f(2)


# def f(a,b):

#   print("hello override")



# f(44,44)
# _______________________-local and global 


# name  = "ahmed"
# print(name)


# def define():

#   global name
#   name = "hello"

#   print(name)

# define()


# print(name)
# ____________________________nameSpaces??????????????????????????????????????????


# print(dir(__builtins__))

# _____________________________constant 

# not made  programatticaly 

# its convension to use big Capital to 
# 
# constant variable 
# MAX_WIDTH = 100


# ___________________________bounding
# its so important topics 
# 
# 
# 
# print(y)

# global y 
# y=10

# x=100
# print(x)
# def f():
#   return
#   # x=x+10
#   # print(x)

# f()
# _______________________
# def external():

#   x=10
#   def internal():

#     x=x+1

#     print(x+1)

#   internal()  

# external()    
# __________________________postional argument  named argument 

# def f(a,/,b,c,d):


#   print(a, b,c,d)


# # f(d=40,a=10,b=20,c=30)

# # f(40,10,d=20,c=30)

# # f(d=40,a=10,b=20,30) => erorSyntaxError: positional argument follows keyword argument


# f(10,20,30,40)



# ___my try to solve namebinding error without global 



# x= 10

# def f():

#   # n=x+10
#   # x=n+1
#   print(n)

# f()


# _________________________ docString 


def do_som_stuff(a):

   """
   param: a: anumber or string 
   
   
   
   """

   print("hello world")



do_som_stuff(10)


print(do_som_stuff.__doc__)


