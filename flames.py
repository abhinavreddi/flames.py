name1=list(input("enter the name: "))
name2=list(input("enter the name: "))

concat = (name1+name2)
rem_concat=set(concat)


count=len(rem_concat)

flames =['f','l','a','m','e','s']

index = 0

while len(flames) > 1:
    index = (index + count - 1) % len(flames)
    flames.pop(index)

print( 'result :'+ flames[0])
