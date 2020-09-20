A = int(input())
B = int(input())
H = int(input())
if B>= H >= A:
    print('Это нормально')
elif H>=B:
    print('Пересып')
else:
    print('Недосып')