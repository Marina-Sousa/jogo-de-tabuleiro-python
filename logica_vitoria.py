# Módulo de Verificação de Vitória - Jogo da Velha (correção de requisitos permitidos)
# Integrante: Sílvia

# Estrutura inicial do tabuleiro de teste
tabuleiro_exemplo = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Variável para testar o jogador atual
jogador_atual = "X"
vitoria = False

# Verificação de linhas e colunas usando laços for
for i in range(3):
    if tabuleiro_exemplo[i][0] == jogador_atual and tabuleiro_exemplo[i][1] == jogador_atual and tabuleiro_exemplo[i][2] == jogador_atual:
        vitoria = True
    if tabuleiro_exemplo[0][i] == jogador_atual and tabuleiro_exemplo[1][i] == jogador_atual and tabuleiro_exemplo[2][i] == jogador_atual:
        vitoria = True

# Verificação das diagonais
if tabuleiro_exemplo[0][0] == jogador_atual and tabuleiro_exemplo[1][1] == jogador_atual and tabuleiro_exemplo[2][2] == jogador_atual:
    vitoria = True
if tabuleiro_exemplo[0][2] == jogador_atual and tabuleiro_exemplo[1][1] == jogador_atual and tabuleiro_exemplo[2][0] == jogador_atual:
    vitoria = True

if vitoria:
    print("Vitória detectada!")
else:
    print("Nenhuma vitória ainda.")

    # Verificação de empate (conta quantas casas ainda estão vazias)
vazias = 0
for i in range(3):
    for j in range(3):
        if tabuleiro_exemplo[i][j] == " ":
            vazias = vazias + 1

if vazias == 0 and vitoria == False:
    print("Deu empate!")