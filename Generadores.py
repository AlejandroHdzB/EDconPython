def multiplos(numero):
    for i in range(1,numero+1):
        if numero % i == 0:
            yield i

for j in multiplos(100):
    print(j)