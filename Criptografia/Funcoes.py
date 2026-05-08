import random

#Calcula o MDC de dois números
def mdc (z, d):
    while d != 0:
        z, d = d, z %d
    return z

#Gera um valor aleatório para D
def defina_d (z):
    while True:
        d = random.randint(1,100000)

        if mdc(z, d) == 1:
            return d

#Pega uma frase, coloca na tabela ASCII e criptogtafa em RSA 
def criptografar(frase, e, n):
    textoCriptografado = []

    for letra in frase:
        fraseAscii = ord(letra)
        #Pesquisei como fazer essa conta em Python
        criptografado = pow(fraseAscii, e, n)

        textoCriptografado.append(criptografado)

    return textoCriptografado

#Transforma o Vetor em uma sequência de números
def criarSequencia(textoC):
    textoFinal = ""

    for num in textoC:
        textoFinal += str(num)

    return textoFinal