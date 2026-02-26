from datetime import datetime

def criar_produto(nome, preco, quantidade):

# Cria um novo produto e salva no dados.txt
# Recebe nome, preco e quantidade do produto.

    if nome == "":
        print("Nome não pode estar vazio.")
        return
    if preco <= 0:
        print("Preço deve ser maior que zero.")
        return
    if quantidade < 0:
        print("A quantidade não pode ser negativa.")
        return
    
    # Gera o ID baseado na data e hora atual
    id_novo = datetime.now().strftime("%Y%m%d%H%M%S")

    # Salva o produto no txt
    with open("dados.txt", "a") as arquivo:
        arquivo.write(f"{id_novo}|{nome}|{preco}|{quantidade}\n")

    print(f"Produto '{nome}' criado!")

