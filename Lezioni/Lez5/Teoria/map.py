def fun(num):
    return num*num

def fun2(num1,num2):
    return num1+num2

def funPrecSucc(num):
    return num-1,num,num+1

lista=[1, 2, 3, 4]
lista1=[5, 6, 7, 8, 9]
mapped = map(fun,lista)

print(type(mapped))
for ele in mapped:
    print(ele,end=" ")
print()

for ele in map(fun2,lista,lista1):
    print(ele,end=" ")
print()

for tuple in map(funPrecSucc,lista):
    print(tuple)