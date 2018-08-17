#Create a list with user defined inputs.
a=[]
b=int(input("Enter First Element"))
a.append(b)
print(a)

#Add the following list to above created list: [‘google’,’apple’,’facebook’,’microsoft’,’tesla’]
c=["google","apple","facebook","microsoft","tesla"]
c.append(a)
print(c)

#Count the number of time an object occurs in a list.
c=[1,6,8,3,8]
n=int(input("find element"))
x=c.count(n)

print(x)

# create a list with numbers and sort it in ascending order.

a=[1,6,8,3,8]
a.sort()
print(a)

# - Given are two one-dimensional arrays A and B which are sorted in ascending order. Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]
c=[]
b=[1,2,3,4]
c=a+b
c.sort()
print(c)

#Count even and odd numbers in that list.
codd=ceven=0
for i in range(0,len(a)):
    if(c[i]%2==0):
        ceven=ceven+1
    else:
        codd=codd+1
print("total even ",ceven)
print("total even ",codd)


#Print a tuple in reverse order.
t=()
t=('556','5564','98685')
t=t[::-1]
print(t)

#Q.2-Find largest and smallest elements of a tuples.
t=(1,2,3,4,5)
x=max(tup)
c=min(tup)
print("max",x)
print("min ",c)

#Convert a string to uppercase.
s='hello world'
print(s.upper())

#Print true if the string contains all numeric characters.
s="6515469259685616326"
print(bool(s.isdigit()))

#Replace the word "World" with your name in the string "Hello World". 
s="hello world"
s1=s.replace('world','tarun rao')
print(s1)




