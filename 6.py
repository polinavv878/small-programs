t= str(input())
if t == 'прямоугольник':
    a = int(input())
    b = int(input())
    print (a * b)
elif t == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    print ((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif t == 'круг':
    r = int(input())
    print (3.14 * r **2)