#swap Value
a = int(input("enter the  a number :"))
b = int(input("enter the b number :"))
# swap 1
temp = a
a = b
b = temp
print("a = ",a)
print("b =", b)
# swap 2
a = a+b
b = a-b
a = a-b
# swap 3
[b , a] = [a , b]

