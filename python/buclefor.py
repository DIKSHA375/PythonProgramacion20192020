a=int(input("dame el valor de la tabla que quieres desarrollar"))
b=int(input("dame hasta que valor"))
print("===tabla del ",a," ===")
for i in range(b+1):
    print(a,"x",i,"=",a*i)
print("=====================")
