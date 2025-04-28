mytuple = ( 0 , 1 , 2 , "hi" , 4 , 5 )
lst =[]
lst=list(mytuple)

lst[3]= 3
mytuple=tuple(lst)
print(mytuple)
