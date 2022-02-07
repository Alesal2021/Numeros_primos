print('NUmeros primos de 2 a 99')
for numero in range(2,100,1):
    s1 = 0
    for i in range(2,numero,1):
      if numero % i == 0:
        s1 = 1
        break
    if not s1:
        print(numero)
