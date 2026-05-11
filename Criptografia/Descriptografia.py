def descriptografar():
    print("\n--- Módulo B: Descriptografar ---")

    try:
        n = int(input("Informe o valor de N: "))
        d = int(input("Informe o valor de D (Chave Privada): "))
    except ValueError:
        print("Erro: N e D precisam ser números inteiros.")
        return

    escolha = input("\nDeseja (1) Digitar a sequência ou (2) Ler o arquivo cifrado.rsa? ")

    cifra = []

    if escolha == '1':
        sequencia = input("Cole a sequência de números separados por vírgula: ")
        cifra = [int(x) for x in sequencia.split(",")]
    else:
        try:
            with open("cifrado.rsa", "r") as f:
                conteudo = f.read()
                cifra = [int(x) for x in conteudo.split(",")]
        except FileNotFoundError:
            print("Arquivo não encontrado.")
            return

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
