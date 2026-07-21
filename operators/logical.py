x=3
y=5
z=3
print(x," > ",y," and ",y," > ",z," = ",x>y and y>z) # 3 > 5 and 5 > 3 = false
print(x," > ",y,"or",x,">=",z," = ",x>y or y>=z) # true 
print(" not( ",y," > ",z,") = ", not(y>z)) # false
print(" not( ",x," > ",y," or ",x, " >= ",z," ) = ",not(x>y or x>=z)) # false

