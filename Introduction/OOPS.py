# class Person:
#     def read(self):
#         print('person is reading')
#     def walk(self):
#         print('person is walking')
# #reference=objeect orientation
# obj1=Person()
# #method calling
# obj1.read()
# obj1.walk()
#
# obj2=Person()
# obj2.read()
# obj2.walk()



# class House:
#
#     def person(self,name,age,color,floormaterial):
#         self.name=name
#         self.age=age
#         self.color=color
#         self.floormaterial=floormaterial
#     def myhome(self):
#         print('person name is %s and age of person is %d and color is %s and floor material is %s'%(self.name,self.age,self.color,self.floormaterial))
#
# home=House()
# home.person('neema',23,'white','tile')
# home.myhome()
# print(home.name)


# constructor
# class House:
#
#     def __init__(self,name,age,color,floormaterial):
#         self.name=name
#         self.age=age
#         self.color=color
#         self.floormaterial=floormaterial
#     def myhome(self):
#         print('person name is %s and age of person is %d and color is %s and floor material is %s'%(self.name, self.age, self.color, self.floormaterial))
#
# home=House("neema",23,"white","tile")
# home.myhome()




# class House:
#
#         def __init__(self,name,color,floormaterial):
#             self.name=n
#
#             self.color=c
#             self.floormaterial=f
#         def myhome(self):
#             print('person name is %s and color is %s and floor material is %s'%(self.name, self.color, self.floormaterial))
#
# k=int(input('enter the number of objects to be added'))
# m=0
# l=[]
# for i in range(k):
#     n = input('NAME:')
#     c = input('COLOR:')
#     f = input('MATERIAL:')
#
#     home=House(n,c,f)
#     l.append(home)
#
# for j in l:
#     home.myhome()




# k=int(input('enter the number of books to be added'))
# m=0
# while m<k:
#     n = input('TITLE OF BOOK:')
#     c = input('AUTHOR NAME:')
#     f = int(input('PRICE:'))
#     class book:
#
#         def __init__(self,n,c,f):
#             self.n=n
#
#             self.c=c
#             self.f=f
#         def mybook(self):
#             print('Title of book is %s and authors name is %s and price is %d'%(self.n, self.c, self.f))
#
#     home=book(n,c,f)
#     home.mybook()
#     m=m+1



# class String1:
#
#     def __init__(self):
#         self.s=s
#
#     def string2(self):
#         print(self.s.upper())
# s=input('STRING:')
# v=String1()
# v.string2()


# class Bank:
#
#     def add(self,name,n,w,d,b):
#
#         self.name=name
#         self.n=n
#         self.w=w
#         self.d=d
#         self.b=b
#     def pri(self):
#
#         if k==1:
#             print('ACCOUNT NAME:',name.upper(),'\n''The current balance amount is %d'%(self.n))
#         elif k==2:
#             print('ACCOUNT NAME:',name.upper(),'\n''The withdrawel amount is %d'%(self.w))
#         elif k==3:
#             print('ACCOUNT NAME:',name.upper(),'\n''The deposited amount is %d'%(self.d))
#         else:
#             print('ACCOUNT NAME:',name.upper(),'\n''The balance amount is %d'%(self.b))
# o=0
# a=int(input('number of accounts'))
# while o<a:
#     name = input('NAME')
#     n = int(input('current balance'))
#     w = int(input('withdrawal amount'))
#     d = int(input('deposited amount'))
#     b = (n - w + d)
#     k = int(input('enter opp'))
#     bank1 = Bank()
#     bank1.add(name, n, w, d, b)
#     bank1.pri()
#     o=o+1


# INHERITANCE
# class A:
#     def printa(self,name):
#         self.name=name
#         print('hai',self.name)
# class B(A):
#     def printb(self):
#         print('hello')
# obj1=B()
# obj1.printb()
# obj1.printa('b')

#
# class person:
#     def __init__(self,name):
#         self.name=name
#     def add2(self):
#         print('%s'%(self.name))
# class person1(person):
#     def __init__(self,name,age):
#         person.__init__(self,name)
#         self.age=age
#     def add1(self):
#         print('%s and %d'%(self.name,self.age))
# obj1=person1('araji',23)
# obj1.add2()
# obj1.add1()


# class A:
#     def printa(self):
#
#         print('hai' )
# class B():
#     def printb(self):
#         print('hello')
#
# class C(B,A):
#     def printc(self):
#         print('hello')
# obj1=C()
# obj1.printb()
# obj1.printa()
# obj1.printc()



# class College:
#     def __init__(self):
#         self.name=input('name')
#         self.dep=input('dept')
#     def printa(self):
#         print('name is %s'%(self.name),'\n','dept is %s'%(self.dep) )
#
# class School:
#     def __init__(self):
#         self.schoolname=input('schoolname')
#         self.place=input('place')
#     def printa(self):
#         print('school name is %s'%(self.schoolname),'\n','place is %s'%(self.place) )
# class Student(College,School):
#     def __init__(self):
#         College.__init__(self)
#         School.__init__(self)
#         self.studentname=input('name of student')
#
#     def printa(self):
#         print('\n','Name is %s'%(self.name.upper()),'\n','Dept is %s'%(self.dep.upper()),'\n','School name is %s'%(self.schoolname.upper()),'\n','Place is %s'%(self.place.upper()),'\n','Name of the student:%s'%(self.studentname.upper()) )
# obj1=Student()ṇṇ n
# obj1.printa()

# MULTILEVEL INHERITANCE

# class Person:
#
#     def setvalue(self,name,place,age):
#         self.name=name
#         self.place=place
#         self.age=age
#     def printa(self):
#         print(self.name)
#         print(self.place)
#         print(self.age)
#
# class child(Person):
#     def setchild(self,phn,address):
#         self.phn=phn
#         self.address=address
#     def printb(self):
#         print(self.phn)
#         print(self.address)
# class student(child):
#     def studentset(self,dep):
#         self.dep=dep
#     def printc(self):
#         print(self.name)
#         print(self.place)
#         print(self.age)
#         print(self.phn)
#         print(self.address)
#         print(self.dep)
# obj1=student()
# obj1.setvalue('name','calicut',34)
# obj1.setchild(1234,'thulasi house')
# obj1.studentset('civil')
# obj1.printc()


# POLYMPORPHISM

# class New:
#
#     def add(self,a,b):
#         c=0
#         self.a=a
#         self.b=b
#         print(self.a+self.b)
#     def add(self,x=None,y=None,z=None):
#         self.x=x
#         self.y=y
#         self.z=z
#         # print(self.x + self.y + self.z)
#
#         s=0
#         if x!=None and y!=None and z!=None:
#             s=x+y+z
#         elif x != None and y != None:
#             s=x+y
#         else:
#             s=x
#         return s
# obj1=New()
# print(obj1.add(2,3))



# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self, other):
#         x=self.x+other.x
#         y=self.y+other.y
#         return (x,y)
# p1=Point(1,2)
# p2=Point(2,4)
# print(p1+p2)
# print(p1.__add__(p2))







# ENCASPLULATION

# class Person:
#     def __init__(self,a,b,c):
#         self.a=a
#         self._b=b
#         self.__c=c
#     def printa(self):
#         print(self.a,self._b)
# class Employee(Person):
#     def __init__(self,a,b,c,d):
#         Person.__init__(self,a,b,c)
#         self.d=d
#     def printb(self):
#         print(self.a,self._b,self.d)
# obj1=Employee(1,2,3,4)
# obj1.printb()


##ABSTRACTION##

# from abc import ABC,abstractmethod
# class Mail(ABC):
#     @abstractmethod
#     def mileage(self):
#         print('ok')
#     def add(self):
#         print('add')
# class Child(Mail):
#     def sum(self):
#         print('sum')
#     def mileage(self):
#         print('not ok')
# obj1=Child()
# obj1.mileage()












class hello:
    def __init__(self,name):
        pass
class hello1(hello):
    def fun(self):
        clzzzzz




























