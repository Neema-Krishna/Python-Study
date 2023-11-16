
# number=int(input('enter the number'))
# def prime_number(number):
#     if  number<2:
#         return False
#     for i in range(2,number):
#         if number%i ==0:
#             return False
#     return True
#
# result=prime_number(number)
# if result == True:
#     print(number,'is prime')
# else:
#     print(number,'is not prime')
#
#
# print(prime_number(number))

#####FIBONACCI SERIES###

# num=int(input('enter number of terms'))
# n1=0
# n2=1
# count=0
#
# if num<=0:
#     print('please enter a positive number')
# elif num==1:
#     print('fibonacci series:', n1)
# else:
#     while count<num:
#         # print(n1)
#         nth=n1+n2
#         n1=n2
#         n2=nth
#         print(n1)
#         count=count+1




#####to shift last and first chara of a word#####
import re
# string=input('please enter a word')
# y=list(string)
# y[0],y[-1]=y[-1],y[0]
# y=''.join(y)
# print(y)

#Take first two and last two and create new string#

# string=input('enter a word')
# z=string[0:2]+ string[-3:-1]
# print('new word is:',z)

# #to change spec. chara expect first#ex.5
# inter=input('value')
# z=inter.replace('c','@')
# y=inter[0]+z[1:-1]+z[-1]
# print(y)

###Factorial of a number

# product=1
# number=int(input('number'))
# if number==0:
#     print('factorial is 1')
#
# for i in range(1,(number+1)):
#     product=product*i
# print(product)

#########sum of , sep numbers########
# s=0
# str=input('comma sep nuumbes')
# str=str.split(',')
# for i in str:
#     s=s+int(i)
# print(s)


#frequency of chara in  string
# dict1={}
# import re
# how=input('enter the string')
# for i in how:
#     if i not in dict1:
#         dict1[i]=1
#     else:
#         dict1[i]=dict1[i]+1
# print(dict1)
#

# while 1:
#     phonebook = {'raju': {'name': 'raju', 'ph.no': 7025017054, 'email id': 'raju@gmail.com'},
#                  'ravu': {'name': 'ravu', 'ph.no': 9768567054, 'email id': 'ravu@gmail.com'}}
#     operation = input('please enter the operation to be performed:ADD,UPDATE,VIEW,DELTE')
#     # end=input('pls type ;1; to stop and 2 to continue')
#
#     # dict1 = {}
    # dict2 = {}
    # if operation == 'view':
    #     vie = input('please provide the name')
    #     print(phonebook[vie])
    # elif operation == 'delete':
    #     delt = input('please provide the name of the student to be deleted')
    #     del phonebook[delt]
    #     print(phonebook)
    # elif operation == 'add':
    #     names = input('please provide the name to be added')
    #     phones = input('ples provide phone no')
    #     email = input('please input mailid')
    #     phonebook.update({names: {"name": names, "phone": phones, "mail": email}})
    #     print(phonebook)
    # elif operation == 'update':
    #     v = input('enter the contact name to be updated')
    #     print(phonebook[v])
    #     s = int(input('detail to be updated:4-NAME,5-PHONENO,6-EMAIL'))
    #     if s == 4:
    #         n = input('pls input name')
    #         phonebook[v].update({'name': n})
    #         phonebook[n] = phonebook[v]
    #         del phonebook[v]
    #         print(phonebook)
    #     elif s == 5:
    #         e = input('pls input mail id')
    #         phonebook[v].update({'mail': e})
    #         print(phonebook)
    #     elif s == 6:
    #         p = input('entr phone no')
    #         phonebook[v].update({'phone': p})
    #         print(phonebook)
    # else:
    #     print('invalid')
    #     break







# positive number from from list
# k=[]
# l=list(map(int,input("Enter some coma separated list of integers : ").split(",")))
# for i in l:
#     z=i*i
#     k.append(z)
# print(k)

# z=input('enter a word')
# for i in z:
#     if i in 'aeiou':
#         print(i)


# list of numbers over 100 ads 100
# z=[]
# l=list(map(int,input("Enter some coma separated list of integers : ").split(",")))
#
# for i in l:
#     if i>100:
#         z.append('over')
#     elif 1<100:
#         z.append(i)
# print(z)



# COUNT OF A
# z=[]
# l=input('enter words:')
# h=l.split(',')
# # for i in h:
# #     z.append(i)
# # print(h)
# sum=0
# for i in h:
#     n=i.count('a')
#     sum=sum+n
#     print('count of a in',i,'is',n)
#
# print('total a is',sum)


# TO SORT VALUES IN DICT
#
# d={}
# l=[]
# n=int(input('entr range'))
# for i in range(n):
#     keys=int(input('keys'))
#     values=int(input('values'))
#     d[keys]=values
# print(d)
# l=sorted(d.keys())
# l1=sorted(d.keys(),reverse=True)
# print(l)
# print(l1)


# # SUM USING FUNCTION
#
# one=int(input('first number='))
# two=int(input('second number='))
# three=int(input('third number'))
#
# def add():
#     x=one+two+three
#     print('sum is:',x)
#     z=3*x
#     print('thrise of sum is',z)
# add()


# sum of digits of a number
# sum=0
# z=list(map(int,input('enter number')))
# for i in z:
#     sum=sum+i
# print(sum)


# # NUMBER OF UPPERCASE AND LOWER CASE OF A WORD
# import re
# n=[]
# v=[]
# z= input('word:')
# for i in z:
#     k=re.search('[A-Z]',i)
#     p = re.search('[a-z]',i)
#     if k:
#         v.append('ok')
#     elif p:
#         n.append('not ok')
# print(v,n)
# print(('number of upper case:',v.count('ok')),('number of lower case:',n.count('not ok')))








# import re
# # prime number
# z=int(input('enter a number'))
# def add(z):
#     for i in range(2,z):
#         if z%i==0:
#             return False
#     return True
# result=add(z)
# if result==True:
#     print(z,'is prime')
# else:
#     print(z,'is not prim,e')


# d = {}
# n = int(input("Enter number of persons : "))
# for i in range(n):
#     print("Details for person:", i + 1)
#     n2 = int(input("Enter number of information you wish to provide: "))
#     for j in range(n2):
#         key = input("Enter any type of info: ")
#         val = input("Enter its value: ")
#         d.update({key: val})
#         print(d)



# Length of longest word
# while True:
#     m = []
#     v = input('enter comma sep words')
#     z = v.split(',')
#     for i in z:
#         k = len(i)
#         m.append(k)
#     print(m)
#     print('max is',max(m))
#     n=int(input('to stp press1 else 2'))
#     if n==1:
#         break

# z=input('enter the word')
# print('The entered eord is ',z)
# str1=z[-1:-4]
# if str1=='ing':
#     z=z+'ly'
# else:
#     z=z+'ing'
# print(z)

# b={'Raju':{'Name':'Raju','ph no':7025017054},'Rajuu':{'Name':'Rajuu','ph no':7005017054}}
# while True:
#     k=int(input('operation'))
#     if k==1:
#         name=input('name')
#         phone=int(input('phone.no'))
#         b.update({name:{'name':name,'ph np':phone}})
#         print(b)
#     elif k==2:
#         name1=input('name of the person whose detail has to be deleted')
#         b.pop(name1)
#         print(b)
#     elif k==5:
#         m=int(input('DETAIL TO BE UPDATED'))
#         if m==8:
#             name2=input('enter name of student')
#             w=input('actual name')
#             print(b[name2])
#             b[name2].update({'Name':w})
#             b[w]=b[name2]
#             print(b)
#     else:
#         m=int(input('continue-3 of break-4'))
#         if m==4:
#             print('closing..')
#             break



# for i in range(1,6):
#     for i in range(1,1+i):
#         print(i,end='')
#     print('\n')

# for i in range(0,6):
#     for i in range(1+i,0,-1):
#         print(i,end='')
#     print('\n')
#
# for i in range(6,0,-1):
#     for i in range(1,i):
#         print(i,end='')
#     print('\n')
# x=int(input('value1'))
# y=int(input('value2'))
# sum=0
# def add(x,y):
#     sum=x+y
#     return sum
# print(add())
y=int(input('value1'))
x=int(input('value2'))
z=(lambda x,y:x*3*y)
print(z(x,y))

















































