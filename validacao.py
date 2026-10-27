# --- ESTRUTURA BASE PARA TESTES ---
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
simbolo_atual = "X"

# === DIA 2 - COMMIT 2: Validação contra Letras e Símbolos ===

# Validação da Linha
linha_valida = False
while linha_valida == False:
    entrada_linha = input("Digite a linha (1, 2 ou 3): ")
    for n in range(1, 4):  # Passa por 1, 2 e 3
        if entrada_linha == str(n):
            linha_valida = True
            linha = n - 1  # Converte para índice da matriz (0, 1 ou 2)
    if linha_valida == False:
        print("Entrada inválida! Digite apenas os números 1, 2 ou 3.")

# Validação da Coluna
coluna_valida = False
while coluna_valida == False:
    entrada_coluna = input("Digite a coluna (1, 2 ou 3): ")
    for n in range(1, 4):  # Passa por 1, 2 e 3
        if entrada_coluna == str(n):
            coluna_valida = True
            coluna = n - 1  # Converte para índice da matriz (0, 1 ou 2)
    if coluna_valida == False:
        print("Entrada inválida! Digite apenas os números 1, 2 ou 3.")

print("Linha válida escolhida (índice):", linha)
print("Coluna válida escolhida (índice):", coluna)