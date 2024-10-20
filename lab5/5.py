a=int(input())
b=int(input())
c=int(input())
if a==b==c:
    print('Треугольник равносторонний')
if a==b or a==c or b==c:
    print('Треугольник равнобедренный')
else:
    print('Треугольник разносторонний')