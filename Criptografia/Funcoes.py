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


'''
import random

#Calcula o MDC de dois números
def mdc (z, d):
    while d != 0:
        z, d = d, z %d
    return z

#Gera um valor aleatório para D
def defina_d (z, p, q):
    while True:
        d = random.randint(128,100000)

        if mdc(z, d) == 1 and  d :
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
    
from sympy import isprime 
from sympy import randprime

#Escolher como gerar P e Q
print("Escolha como será gerado P e Q:")
op = int(input("1. Manualmente (Você escolhe os valores)\n" \
               "2. Aleatoriamente (O sistema gera os valores)\n"))

if op == 1:
    frase = input("Digite a frase que será criptografada: \n")

    #Verifica se P e Q são primos
    while True:
        p = int(input("Escolha o valor de P: "))
        q = int(input("Escolha o valor de Q: "))

        #Função para verificar se são primos e diferentes
        if isprime(p) and isprime(q) and p != q:
            break
        
            
        else:
            print("Ambos precisam ser primos e distintos, escolha outros valores...")
        

    #Calcula os valores N e Z
    n = p*q
    z = (p-1)*(q-1)

    print ("Valor de Z: ", z)
    #Chama a função para gerar o D
    d = defina_d(z, p, q)

    #Calculo para encontrar o valor de E (Pesquisei como fazer o cálculo de E)
    e = pow(d, -1, z)

    print("Chave Pública (N e E): ", n, " e ", e)
    print("Chave Privada (N e D): ", n, " e ", d)

    #Chama a função para transformar em uma sequência numérica em ASCII
    textoCriptografado = criptografar(frase, e, n)

    #Chama a função que torna o vetor em uma sequência numérica
    textoFinal = criarSequencia(textoCriptografado)

    with open("cifrado.rsa", "w") as f:
        f.write(textoFinal)

    #Exibe resultado final
    print("Texto criptografado: ", textoFinal)

elif op == 2:
    frase = input("Digite a frase que será criptografada: \n")

    #Gera números primos aleatórios 
    print("Gerando aleatoriamente...")
    while True:
        p = randprime(1000,100000)
        q = randprime(1000,100000)

        if p != q:
            break

    print("Valor de P: ", p)
    print("Valor de Q: ", q)

    #Calcula os valores N e Z
    n = p*q
    z = (p-1)*(q-1)

    print ("Valor de Z: ", z)
    #Chama a função para gerar o D
    d = defina_d(z)

    #Calculo para encontrar o valor de E (Pesquisei como fazer o cálculo de E)
    e = pow(d, -1, z)

    print("Chave Pública (N e E): ", n, " e ", e)
    print("Chave Privada (N e D): ", n, " e ", d)

    #Chama a função para transformar em uma sequência numérica em ASCII
    textoCriptografado = criptografar(frase, e, n)

    #Chama a função que torna o vetor em uma sequência numérica
    textoFinal = criarSequencia(textoCriptografado)

    #Exibe resultado final
    print("Texto criptografado: ", textoFinal)

else:
    print("Opção Inválida...")
    
def descriptografar():
    print("\n--- Módulo B: Descriptografar ---")

    try:
        n = int(input("Informe o valor de N: "))
        d = int(input("Informe o valor de D (Chave Privada): "))
    except ValueError:
        print("Erro: N e D precisam ser números inteiros.")
        return

    escolha = input("\nDeseja (1) Digitar a sequência ou (2) Ler o texto criptografado? ")

    cifra = []

    if escolha == '1':
        sequencia = input("Cole a sequência de números separados por vírgula: ")
        cifra = [int(x) for x in sequencia.split(",")]
    elif escolha == '2':
        try:
            conteudo = textoFinal
            cifra = [int(x) for x in conteudo.split(",")]
        except FileNotFoundError:
            print("Arquivo não encontrado.")
            return
    else:
        print("Valor inválido.")
    # descriptografa cada número
    bytes_originais = [pow(num, d, n) for num in cifra]

    # transforma lista em bytes
    dados = bytes(bytes_originais)

    # converte UTF-8 para string
    texto_claro = dados.decode("utf-8")

    print("\n" + "="*30)
    print("Texto original:", texto_claro)
    print("="*30)

# Para fazer funcionar
if __name__ == "__main__":
    descriptografar()
'''
