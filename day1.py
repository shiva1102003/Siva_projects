#Numeric Data types
num=100
percentage=9.5
c=2+3j
print(num,type(num))
print(percentage,type(percentage))
print(c,type(c))

#Sequence data types
s='siva'
lst=[10,'siva',9.5]
t=(1,5,7,9,0)
print(s,type(s))
print(lst,type(lst))
print(t,type(t))

#Boolean data types (True/False)
B1=True
B2=False
print(B1,B2,type(B1),type(B2))
print(B1+B2)

#Mapping data types(Dictionary) key value pairs
d={'name':'siva',
   'age':23,
   'percentage':85}
print(d,type(d))

#Set data types
s=[1,2,3,4,4]
print(s,type(s))

lst1=[] #list()
t1=() #tuple()
str1=' ' #str()
d1={} #dict()
s1=set()
print(lst1,type(lst1))
print(t1,type(t1))
print(str1,type(str1))
print(d1,type(d1))
print(s1,type(s1))

#Type casting
#1)Implicit type casting
#2)Explicit type casting


#user input
num=int(input())
s=input()
list1=list(map(int,input().split(",")))
tuple1=tuple(map(int,input().split()))
set1=set(map(int,input().split()))
print(num)
print(s)
print(list1)
print(tuple1)
print(set1)