# Módulo de Verificação de Vitória - Jogo da Velha
# Integrante: Sílvia

def verificar_vitoria_linhas_colunas(tabuleiro, jogador):
    # Verifica as linhas e colunas usando laços for
    for i in range(3):
        # Verifica linha 'i'
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True
        # Verifica coluna 'i'
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            return True
            
    return False

# Estrutura inicial do tabuleiro de teste
tabuleiro_exemplo = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

print("Módulo de verificação de vitória carregado com sucesso!")