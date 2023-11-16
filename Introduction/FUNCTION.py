# def fun():
#     print('hello')
# fun()

# def add():
#     x=int(input('enter the value1'))
#     y=int(input('enter the value2'))
#     sum=x+y
#     print('sum=',sum)
# add()

# def add(x,y):
#     product=x*y
#     print(product)
# add(int(input('value1')),int(input('value2')))


# def add(x,y,z=3):
#     return x*y*z
#
# print(add(6,2))

# def add(*nums):
#   print(nums)
#   sum1=sum(nums)
#   print(sum1)
# add(1,8,9,10)


# def add(num):
#     num=int(input('enter the value'))
#     sum=0
#     for i in range(1,num+1):
#         sum=sum+i
#     print(sum)
#
# add(10)




# num=int(input('value'))
#
# def add(num):
#
#     product=1
#     if num==0:
#         print('factorial is 1')
#
#     elif num<0:
#         print('factorial cannot be found')
#
#     else:
#         for i in range(1,num+1):
#             product = product*i
#         print(product)
# add(num)


# operation=input('Enter the operation to be performed')
# while True:
#     if operation == 'addition':
#         def add(x, y, z):
#             sum1 = x + y + z
#             print(sum1)
#
#
#         add(int(input('x=')), int(input('y=')), int(input('z=')))
#
#
#     elif operation == 'substraction':
#         def sub(x, y):
#             subtrahend = x - y
#             print(subtrahend)
#
#
#         sub(int(input('x=')), int(input('y=')))
#
#
#     elif operation == 'multiplication':
#         def pro(x, y):
#             product = x * y
#             print(product)
#
#
#         pro(int(input('x=')), int(input('y=')))
#
#
#     elif operation == 'division':
#         def div(x, y):
#             z = x / y
#             print(z)
#
#
#         div(int(input('x=')), int(input('y=')))
#     else:
#         print('NOT POSSIBLE')
#         break


# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def pro(x,y):
#     return x*y
# def div(x,y):
#     return x/y
# print('Select operation:')
# print('1-ADDITION,2-SUBSTRACTION,3-MULTIPLICATION,4-DIVSION')
# while True:
#     choice1 = input('enter the operation')
#     if choice1 in ('1', '2', '3', '4'):
#         num1 = int(input('enter first number'))
#         num2 = int(input('num2'))
#
#         if choice1 == '1':
#             print(num1, '+', num2, '=', add(num1,num2))
#         elif choice1 == 2:
#             print(num1, '+', num2, '=', sub(num1,num2))
#         elif choice1 == 3:
#             print(num1, '+', num2, '=', pro(num1,num2))
#         elif choice1 == 4:
#             print(num1, '+', num2, '=', div(x, y))
#         nextcalc = input('YES/NO')
#         if nextcalc == 'NO':
#             break
#     else:
#         print('invalid input')
#         break

# x=int(input('first number'))
# y=int(input('second number'))
# z=(lambda x,y:x*y)
# print('product is',z(3,4))




# x=input('pls enter the statement')
# y=(lambda x: x.upper() [::-1])
# print(y(x))

# def add(x,y):
#     z=x+y
#     return(z)
# def pro(x,y):
#     z=x*y
#     return(Z)
# def div(x,y):
#     z=x/y
#     return(Z)
# def sub(x,y):
#     z=x-y
#     return
# print('OPERATION:1.ADDITION,2.SUBSTRACTION,3.DIVISION,4.MULTIPLICATION')
#
# while True:
#     operation=input('pls select operation to be performed')
#     if operation in ('1','2','3','4'):
#         num1=int(input('value1'))
#
#         num2=int(input('value2'))
#         if operation == '1':
#             print(num1, '+', num2, '=', add(num1,num2))
#         elif operation==2:
#             print(num1 , '+',num2,'=',sub(num1,num2))
#         nextcalc=input('YES/NO')
#         if nextcalc=='NO':
#             print('stop')
#             break
#     else:
#         print('invalid input')
#         break
#
#
#

# list1=[1,2,3,4,5,6,7,8,9,10]
#
# list2=list(filter(lambda x:x%2==0,list1))
# print(list2)

#
# list1=['a','c','d','a','b','a' ]
# list2=list(filter(lambda x:x in 'a',list1))
# print(list2)
#
# list3=['ramu','raju','dolu','bolu','rema','raju']
# def add(x):
#     return 'a' in x
# print(list(filter(add ,list3)))



# x=[1,2,3,4]
# y=[1,4,5]
# z=set(zip(x,y))
# print(z)
#
# list1=[1,2,3,4]
# list2=list(map(lambda x: pow(x,3),list1))
# print(list2)

# list1=['raju','ravi','neama']
# list2=list(map(lambda x:len(x),list1))
# print(list2)

# list1=['ravi','raju','ramu']
# list2=['ramu','dolu','bolu']
#
# list3=list(map(lambda x,y:(x+y),list1,list2))
# print(list3)
#
# list1=[1,2,3]
# list2=[4,5,6]
# list3=list(map(lambda x,y:(x+y),list1,list2))
# print(list3)

# lsi1=[1,2,34,5]
# x=enumerate(lsi1)
# print(list(x))

# str1='hello'
# # for i in str1:
# x=enumerate(str1)
# print(list(x))

# dict1={11:'raju',13:'ramu',14:'ravi'}
# for i in dict1:
#     print(i,'=',dict1[i])

# print(list(enumerate(dict1.keys())))




# pin=input('enter the pin')
#
# def validinput(pin):
#     if len(pin) in [4,6]:
#         for i in pin:
#             if i not in ['1','3','5','9','7']:
#                  return 'invalid'
#         return 'valid'
#     else:
#         return 'invalid'
#
# print(validinput(pin))


# RECURSION

n=int(input('Number:'))
def fact(n):
    if n<1:
        return 0
    else:
        return (n+fact(n-1))
print(fact(n))




