#Q.1- Reverse the whole list using list methods.
Li=[1,2,3,4,5]
Li.reverse() 
print("Reverse List:",Li)

#Q.2- Print all the uppercase letters from a string.
String="Its a new day"
upper=""
for letter in String:
    if letter.isupper():
        upper=upper+letter+','
print("All uppercase letters:",upper)

#Q.3-Split the user input on comma's and store the values in a list as integers.
value=input("Enter input:")
a=value.split(',')
b=[]
for i in a:
    b.append(int(i))
print(b)


#Q.4- Check whether a string is palindromic or not.
String="malayalam"
rev=String[::-1]
if String==rev:
    print('String is a palindrome')
else:
    print('String is not a palindrome')

#Q.5- Make a deepcopy of a list.
import copy as c
l1=[1,2,3,[4,6],5]
l2=c.deepcopy(l1)
l1[3][1]='Hi'
l1[2]='Bye'
print(l1)
print(l2)

"""
The difference between shallow copy and deep copy:
->is for objects that contains other object like list containing list inside

1.A shallow copy constructs a new compound object and then inserts references into the objects found in the
original object.
In python, the syntax for shallow copy is "copy()".

2.A deep copy constructs a new compound object and then recursively inserts copies of the objects found in
the original, into it.
In python, the syntax for deep copy is "deepcopy()".

"""












