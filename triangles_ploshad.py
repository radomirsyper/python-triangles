import math
a = int(input())
b = int(input())
c = int(input())
if a<0 or b<0 or c<0: #проверяет что числа больше или равны рулю
    print("incorect input")
elif a+b<c or a+c<b or c+b<a: #проверяет возможен ли такой треугольник
    print("Треугольник не существует")
else:
    p = (a+b+c)/2 #вычисление полупериметра треугольника
    s = math.sqrt(p*(p-a)*(p-b)*(p-c)) #вычисление площади треугольника 
    print ("Площадь треугольника:",s) #выдача площади