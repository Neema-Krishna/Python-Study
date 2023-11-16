##1.EVEN OR ODD##

# n=int(input('enter the number'))
# if n==0:
#     print('either positive nor negative')
# elif n%2==0:
#     print('even number')
# else:
#     print('odd no')


##2.POSITIVE OR NEGATIVE##

# n=int(input('enter the number'))
# if n==0:
#     print('neither positive nor negative')
# elif n>0:
#     print('positive no')
# else:
#     print('negative no')

##3.Sum of First N Natural numbers##

# n=int(input('enter the count'))
# sum=0
# for i in range(1,(n+1)):
#     sum=sum+i
# print(sum)\


##4.Sum of N natural numbers#3

# l = list(map(int, input("Enter some coma separated list of integers : ").split(",")))
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)


##5.Sum of numbers in a given range##
#
# v=int(input('enter the range1'))
# n=int(input('enter range2'))
# sum=0
# for i in range(v,(n+1)):
#     sum=sum+i
# print('sum=',sum)


##6.Greatest of two numbers##

# n=int(input('Value 1'))
# v=int(input('Value 2'))
# if n>v:
#     print(n,'is the greatest')
# elif n<v:
#     print(v,'is the greatest')


##7.Greatest of the Three numbers:##

# n=int(input('Value1'))
# m=int(input('Value2'))
# k=int(input('value3'))
# if n>(m and k):
#     print('n greatest')
# elif m>(n and k):
#     print('m greatest')
# elif k>(m and n):
#     print('k is the greatest')


##8.Greatest no in a list##

# list=list(map(int,input('enter comma sep numbers').split(',')))
# print(max(list))


##9.Leap year##

# year = int(input('YEAR='))
# if (year%400 == 0) or (year%4==0 and year%100!=0):
#   print("Leap Year")
# else:
#   print("Not a Leap Year")


##10.Prime number##

# n=int(input('NUMBER='))
# def add(n):
#     for i in range(2, (n - 1)):
#         if n % i != 0:
#             return True
#
#         else:
#             return False
# result=add(n)
# if result==True:
#     print(n,'is a prime number')
# else:
#     print('not prime')


##11.Prime number within a given range##
# low, high = 2, 10
# primes = []
#
# for i in range(low, high + 1):
#     flag = 0
#
#     if i < 2:
#         continue
#     if i == 2:
#         primes.append(2)
#         continue
#
#     for x in range(2, i):
#         if i % x == 0:
#             flag=1
#             break
#
#     if flag == 0:
#         primes.append(i)
#
# print(primes)


##12.Sum of digits of a number##

# n=input('number')
# sum=0
# for i in n:
#     sum=sum+int(i)
# print(sum)


##13.Reverse of a number##

# n=input('number')
# k=n[::-1]
# print(k)


##14.PALINDROME NUMBER##

# n=input('number')
# k=n[::-1]
# if n==k:
#     print('The number is palindrome')
# else:
#     print('The number is not palindrome')


##15.Armstrong number--sum of the digits power of len of number=number##

# n=input('NUMBER=')
# digit=0
# sum=0
# l=len(n)
# for i in range(l):
#     digit=int(n)%10
#     n=int(n)/10
#     k=pow(digit,l)
#     sum=sum+k
# if n==sum:
#     print('number is armstrong')


##16.Armstrong number in a given range##

# digit=0
# sum=0
# flag=0
# o=[]
# for i in range(1,1000):
#     l=len(str(i))
#     for i in range(l):
#         digit = int(i) % 10
#         i=int(i)/10
#         k=pow(digit,l)
#         sum=sum+k
#         if i==sum:
#             flag=1
#     if flag==0:
#         o.append(i)
# print(o)

##17.Fibonacci Series upto nth term-PRINTH Nth TERM##

# n=int(input('enter length of term'))
# n1=0
# n2=1
# count=0
# k=[]
# if n==1:
#     print(n1)
# else:
#     while count < n:
#         k.append(n1)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count=count+1
# print(k)
# print(k[n-1])


##18.FACTORAIL OF A NUMBER##

# n=int(input('NUMBER:'))
# product=1
# for i in range(1,(n+1)):
#     product=product*i
# print(product)


##19.POWER OF A NUMBER##

# n=int(input('NUMBER:'))
# v=int(input('power value:'))
# print(pow(n,v))


##20.FACTOR OF A NUMBER##

# n=int(input('NUMBER:'))
# k=[]
# for i in range(1,(n+1)):
#     if n%i==0:
#         k.append(i)
#     else:
#         continue
# print(k)


##21.PRIME FACTORS OF A NUMBER##

# k=[]
# o=[]
# n=int(input('NUMBER:'))
# for i in range(2,(n+1)):
#     if n%i==0:
#         k.append(i)
#     else:
#         continue
# print(k)
# v=1
# for n in k:
#     for m in range(3,n):
#         if n%m==0:
#             v=0
#             break
#     if v==1:
#         o.append(n)
# print(o)


##22.STRONG NUMBER##

# k=input('number')
# n=k
# digit=0
# sum=0
# product=1
# for i in range(0,len(n)):
#     digit=int(int(n)%10)
#     n=int(int(n)/10)
#     for i in range(1,(digit+1)):
#         product=product*i
#     # print(product)
#     sum=sum+product
#     product=1
#
# print(sum)
# if sum==int(k):
#     print(k,'IS A STRONG NUMBER')
# else:
#     print(k,'IS NOT A STRONG NUMBER')


##23.PERFECT NUMBER-NUMBER WHOSE SUM OF DIVSIORS =NUMBER##

# while True:
#     k = int(input('number'))
#     n = []
#     for i in range(1, k):
#         if k % i == 0:
#             n.append(i)
#     print(n)
#     sum = 0
#     for m in n:
#         sum = sum + m
#     print(sum)
#     if sum == k:
#         print(k, 'is a perfect number')
#     else:
#         print(k, 'is not a perfect number')
#     b=int(input('break-1,continue-2'))
#     if b==1:
#         print('CLOSED')
#         break


##24.PERFECT SQUARE##

# n=int(input('NUMBER:'))
# flag=0
# for i in range(1,n):
#     if i*i==n:
#         flag=1
#
# if flag==0:
#     print('NOT PERFECT NUMBER')
# else:
#     print('perfect number')


##25.AUTOMORPHIC NUMBER:SQ ENDS WITH THE SAME DIGIT AS NUMBER##

# n=int(input('NUMBER:'))
# k=n*n
# if k%10==n:
#     print('its an automorphic number')
# else:
#     print('its not an automorphic number')


##26.HARSHAD NUMBER-A NUMBER DIVISBLE BY SUM OF ITS DIGIT##

# k=input('NUMBER')
# n=k
# sum=0
# for i in range(0,len(n)):
#     digit=int(n)%10
#     n=int(n)/10
#     sum=sum+digit
# print(sum)
# if int(k)%sum==0:
#     print('THE NUMBER IS HARSHAD')
# else:
#     print('THE NUMBER IS NOT HARSHAD')


##27.ABUNDANT NUMBER-the sum of it’s factors must be greater than the number itself##

# m=int(input('NUMBER;'))
# n=m
# k=[]
# for i in range(1,n):
#     if n%i==0:
#         k.append(i)
# print(k)
# sum=0
# for n in k:
#     sum=sum+n
# print(sum)
# if sum>m:
#     print('Its an abundant number')
# else:
#     print('Its not an abundant number')


#28.FREINDLY PAIR##

# n=int(input('FIRST NUMBER'))
# k=n
# m=int(input('SECOND NUMBER'))
# o=m
# first=[]
# second=[]
# for i in range(1,n):
#     if n%i==0:
#         first.append(i)
# for c in range(1,m):
#     if m%c==0:
#         second.append(c)
# print(first)
# print(second)
# sum1=0
# sum2=0
# for a in first:
#     sum1=sum1+a
# print(sum1,':SUM OF FACTORS OF NUMBER1')
# for b in second:
#     sum2=sum2+b
# print(sum2,':SUM OF FACTORS OF NUMBER2')
#
# if k/sum1==o/sum2:
#     print('Its a friendly pair')
# else:
#     print('Its not a friendly pair')


##HIGHEST COMMON FACTOR##

# n=int(input('NUMBER1:'))
# n1=int(input('NUMBER2:'))
# k=[]
# k1=[]
# for i in range(1,(n+1)):
#     if n%i==0:
#         k.append(i)
# for i1 in range(1,(n1+1)):
#     if n1%i1==0:
#         k1.append(i1)
# print(k,',',k1)
# b=0
# m=[]
# for a in k:
#     for a1 in k1:
#         if a==a1:
#             m.append(a)
# # print('THE HIGHEST COMMON FACTOR IS:',max(m))
# m.pop(0)
# print('THE LOWEST COMMON FACTOR IS:',min(m))


##LOWEST COMMON MULTIPLR##

# n=int(input('NUMBER 1:'))
# n1=int(input('NUMBER 2:'))
# m=[]
# m1=[]
# for i in range(1,(n*n1)):
#     k=n*i
#     m.append(k)
#     k1=n1*i
#     m1.append(k1)
# print(m,',',m1)
# o=[]
# h=[o.append(l)for l in m for l1 in m1 if l==l1]
# print('LCM IS:',min(o))


##GREATEST COMMON DIVISOR##

# n=int(input('NUMBER1:'))
# n1=int(input('NUMBER 2'))
# k=[]
# k1=[]
# for i in range(1,(n+1)):
#     if n%i==0:
#         k.append(i)
# for i1 in range(1,(n1+1)):
#     if n1%i1==0:
#         k1.append(i1)
# print(k)
# print(k1)
# m=[]
# flag=0
# for a in k:
#     for a1 in k1:
#         if a==a1:
#             m.append(a1)
# print(m)
# print(max(m))


##Replace all '0' s with 1 in a given integer##
#
# n=input('NUMBER:')
# l=[]
# for i in n:
#     if i=='0':
#         l.append(1)
#     elif i=='2':
#         l.append(3)
#     else:
#         l.append(i)
# print(l)
# n1=''
# for i1 in l:
#     n1=n1+str(i1)
# print(n1)


##Find the prime numbers between 1 to 100##

# m=[]
# for i in range(2,101):
#     flag=0
#     for m in  range(2,i):
#         if i%m==0:
#             flag=1
#     if flag==0:
#         print(i,end=',')


##count od digits in an integer##

# n=input('number')
# sum=0
# for i in n:
#     sum=sum+int(i)
# print('count=',sum)


#COUNT OF A DIGIT##

# x=input('x')
# list1=input('NUMBER')
# sum=0
# for i in list1:
#     if x==i:
#         sum=sum+1
# print('Count of',x,'is',sum)


##Finding number of integers which has exactly x divisors##

# Number = 7
# Divisor = 2
# #count is to count total number of Numbers with exact divisor
# count = 0
# #driver loop
# for i in range(1,Number+1):
#     #count_factors checks the total number of divisors
#     count_factors = 0
#     #loop to find number of divisors
#     for j in range(1,i+1):
#         if i % j == 0:
#             count_factors += 1
#         else:
#             pass
#     if count_factors == Divisor:
#         count +=1
#
# #for break in line between Numbers and total count
# print(count)
#


# PATTERN PRINTING

# for i in range(1,6):
#     for i in range(1,(i+1)):
#         print(i, end=' ')
#     print('\n')

# for i in range(1,6):
#     for i in range(i,0,-1):
#         print(i, end=' ')
#     print('\n')

# for i in range(5,0,-1):
#     for i in range(i,0,-1):
#         print(i, end=' ')
#     print('\n')

# for i in range(5,0,-1):
#     for i in range(1,i+1):
#         print(i, end=' ')
#     print('\n')

# for i in range(5,0,-1):
#     for i in range(i,0,-1):
#         print(i, end=' ')
#     print('\n')
# count=0
# k=0
# for i in range(5,0,-1):
#
#     for j in range(1,i):
#         print(j,end=' ')
#     for k in range(i,0,-1):
#         print(k,end=' ')
#     print('\n')
#
#     for m in range(i,1,-3):
#
#            print('0',end=' ')

# FIBONACCI SERIES  0,1,1,2,3,5,8

# n=0
# n1=1
# k=[n,n1]
# number=int(input('value'))
# n2=0
# count=0
# while count<number-2:
#     n2=n+n1
#     k.append(n2)
#     n=n1
#     n1=n2
#     count=count+1
# print(k)

# PRIME NUMBER

# n=int(input('value'))
# def prime(n,i=2):
#         if n==i:
#                 return True
#         elif n%i==0:
#                 return False
#         else:
#                 return prime(n,(i+1))
# if prime(n):
#         print('prime number')
# else:
#         print('Not prime')

# list=[1,2,12,3]
#
# len=len(list)
# def array(list,len):
#         if len==1:
#                 return list[0]
#         else:
#                 return max(list[len-1],array(list,(len-1)))
# print(array(list,len))

# REVERSING A NUMBER
# HCF
n=int(input('first'))
m=int(input('second'))
k=[]
v=[]
l=[]
for i in range(2,(n+1)):
        if n%i==0:
                k.append(i)
for i in range(2,(m+1)):
        if m%i==0:
                v.append(i)
for i in k:
        for m in v:
                if i==m:
                        l.append(i)
print('HCF',min(l))





























































