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

# Pega uma frase, coloca na tabela UTF-8 e criptografa em RSA
def criptografar(frase, e, n):

    # transforma a frase em bytes UTF-8
    bytes_utf8 = frase.encode("utf-8")

    # criptografa cada byte
    textoCriptografado = [pow(byte, e, n) for byte in bytes_utf8]

    return textoCriptografado

#Transforma o Vetor em uma sequência de números
def criarSequencia(textoC):
    return ",".join(map(str, textoC))
