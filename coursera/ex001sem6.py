def computador_escolhe_jogada(n, m):
    # Verifica se é possível deixar um múltiplo de (m+1) peças para o jogador
    for i in range(1, m + 1):
        if (n - i) % (m + 1) == 0:
            return i
    # Caso não seja possível, retira o número máximo de peças permitido
    return m

def usuario_escolhe_jogada(n, m):
    jogada = 0
    # Garante que a jogada seja válida
    while jogada <= 0 or jogada > m or jogada > n:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada <= 0 or jogada > m or jogada > n:
            print("Jogada inválida. Tente novamente.")
    return jogada

def partida():
    n = int(input("Quantas peças no tabuleiro? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m + 1) == 0:
        print("Você começa!")
        vez_do_usuario = True
    else:
        print("Computador começa!")
        vez_do_usuario = False

    while n > 0:
        if vez_do_usuario:
            jogada = usuario_escolhe_jogada(n, m)
            print(f"Você tirou {jogada} peças.")
        else:
            jogada = computador_escolhe_jogada(n, m)
            print(f"O computador tirou {jogada} peças.")

        n -= jogada
        vez_do_usuario = not vez_do_usuario

        print(f"Agora restam {n} peças no tabuleiro.\n")

    if vez_do_usuario:
        print("O computador ganhou!")
    else:
        print("Você ganhou!")

def campeonato():
    placar_usuario = 0
    placar_computador = 0

    for _ in range(3):
        print("\n**** Rodada ****")
        if partida():
            placar_usuario += 1
        else:
            placar_computador += 1

    print("\n**** Placar Final ****")
    print(f"Você {placar_usuario} X {placar_computador} Computador")

def main():
    print("Bem-vindo ao jogo do NIM!")
    escolha = int(input("Escolha:\n1 - Jogar uma partida\n2 - Jogar um campeonato\n"))

    if escolha == 1:
        print("\n**** Partida avulsa ****")
        partida()
    elif escolha == 2:
        print("\n**** Campeonato ****")
        campeonato()
    else:
        print("Escolha inválida. Encerrando o jogo.")

if __name__ == "__main__":
    main()
