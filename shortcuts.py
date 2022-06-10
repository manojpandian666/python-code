#F Strings
# name = "Mano"
# print(f"Hello {name} {[1,2,3]} {5 + 6} {5 == 6}.")

#Unpacking
# tup=(1,2,3,4,5)
# lst=[1,2,3,4,5]
# string = "hello"
# dic = {"a":1,"b":2}
# coords = [4,5]

# a,b = dic.values()
# print(a,b)
# ---------------------------

#Multiple Assignment
# width,height = 400,500

# temp=width
# width=height
# height=temp

# width,height=height,width
# print(width,height)
# ---------------------------

#Comprehensions - any
# x=[[0 for _ in range(5)] for _ in range(10)]
# y = [[j for i in range(3)] for j in range(10)]
# print(y)
# ---------------------------

#Object Multiplication
# x = [[1,2,3]] * 5
# print(x)

#Inline/Ternary Condition
# x = 1 if 2 > 3 else 0
# print(x)
#x = 2 > 3 ? 1 : 0
# ---------------------------

#Zip
# names=['tim','joe','billy','sally']
# ages = [21,19,18,43]
# eye_colors=['blue','brown','brown','green']
# # print(list(zip(names,ages,eye_colors)))

# for name,age,eye_color in zip(names,ages,eye_colors):
#     if age>20:
#         print(name)
#     #print(eye_color)
# ---------------------------

#*args and ** kwargs
# def func1(arg1,arg2,arg3):
#     print(arg1,arg2,arg3)
# def func2(arg1=None,arg2=None,arg3=None):
#     print(arg1,arg2,arg3)
# args=[2,2,3]
# kwargs={"arg2":2,"arg1":1,"arg3":3}
# func1(args)
# ---------------------------

#For Else&While Else
# search = [1,2,3,4,5,6,7]
# target=8
# for element in search:
#     if element == target:
#         print('Ifound it!')
#         break
# else:
#     print("Ididn't find it!")
# i = 0
# while i < len(search) :
#     element  = search[i]
#     if element == target:
#         print("Found")
#     i +=1
# else:
#     print("Not Found")
# ---------------------------

#Sort By Key
lst=[[1,2],[3,4],[4,2],[-1,3],[4,5],[2,3]]
#lst.sort(reverse=True)
lst.sort(key=lambda x: x[1])
print(lst)