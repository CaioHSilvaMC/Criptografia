from Funcoes import defina_d, criptografar, criarSequencia
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
    #Chama a função para gerar o D  
    try:
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
    except ValueError as erro:
        print(erro)
        exit()

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
    try:
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
    except ValueError as erro:
        print(erro)
        exit()

else:
    print("Opção Inválida...")
