from sympy import isprime
from Funcoes import *

p = int(input("Digite o valor de P: "))
q = int(input("Digite o valor de Q: "))

if isprime(p) and isprime(q):
    n = p*q
    z = (p-1)*(q-1)

    print ("Valor de Z: ", z)
    d = int(input("Digite o Valor de D (Precisa ser Primo em relação a Z): "))

    if mdc(z, d) == 1:
        e = pow(d, -1, z)

        print ("Valor de P", p)
        print ("Valor de Q", q)
        print ("Valor de N", n)
        print ("Valor de Z", z)
        print ("Valor de D", d)
        print ("Valor de E", e)
    else:
        print ("D precisa ser um coprimo de Z")
else:
    print ("Ambos, P e Q, precisam ser primos")



