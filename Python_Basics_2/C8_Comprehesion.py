# manera de agregar elementos en una lista
numbers=[]


for element in range(1,11):
        numbers.append(element)
print(numbers)

# manera 2 de agregar elementos

numbers_v2=[element for element in range(1,20)]
print(numbers_v2)

#"Se pueden realizar operaciones por elementos"
numbersPlus2=[element * 2 for element in range(1,6)]
print(numbersPlus2)

#Condicional 1

numbersIf=[]
for i in range (1,11):
        if i%2 ==0:
                numbersIf.append(i*2)
print(numbersIf)

#Condicional 2

numbersIf2=[i * 2 for i in range(1,11) if i%2==0]
print(numbersIf2)