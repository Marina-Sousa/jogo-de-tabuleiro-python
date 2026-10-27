# --- ESTRUTURA BASE PARA TESTES ---
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
simbolo_atual = "X"

# === DIA 1 - COMMIT 1: Leitura Básica ===
# Leitura direta sem tratamento ainda (apenas captura o que o usuário digita)
entrada_linha = input("Digite a linha (1, 2 ou 3): ")
entrada_coluna = input("Digite a coluna (1, 2 ou 3): ")

print("Linha digitada:", entrada_linha)
print("Coluna digitada:", entrada_coluna)