from Funcoes import mdc, defina_d 

def descriptografar():
    print("\n--- Módulo B: Descriptografar ---")
    
    #  Receber as chaves (com a chave privada)
    try:
        n = int(input("Informe o valor de N: "))
        d = int(input("Informe o valor de D (Chave Privada): "))
    except ValueError:
        print("Erro: N e D precisam ser números inteiros.")
        return

    # Receber a cifra 
    escolha = input("\nDeseja (1) Digitar a sequência ou (2) Ler o arquivo cifrado.rsa? ")
    
    cifra = []
    
    if escolha == '1':
        sequencia = input("Cole a sequência de números separados por vírgula: ")
        cifra = [int(x) for x in sequencia.split(",")]
    else:
        try:
            with open("cifrado.rsa", "r") as f:
                conteudo = f.read()
                # Transforma a string do arquivo em uma lista de números
                cifra = [int(x) for x in conteudo.split(",")]
        except FileNotFoundError:
            print("Erro: Arquivo cifrado.rsa não encontrado.")
            return

    # descriptografia 
    texto_claro = ""
    for num in cifra:
        # A conta inversa: Letra = Cifra ^ D mod N
        # O pow resolve o requisito de inteiros grandes 
        letra_ascii = pow(num, d, n)
        texto_claro += chr(letra_ascii) # Converte o número de volta para caractere UTF-8 

    # mostra o resultado final
    print("\n" + "="*30)
    print(f"Texto Original: {texto_claro}")
    print("="*30)

# Para fazer funcionar
if __name__ == "__main__":
    descriptografar()
