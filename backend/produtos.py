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
    
    # Pega o ID baseado em quantos produtos existem.
    try:
        with open("dados.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            id_novo = len(linhas) + 1
    except FileNotFoundError:
        id_novo = 1

    # Salva o produto no txt
    with open("dados.txt", "a") as arquivo:
        arquivo.write(f"{id_novo},{nome},{preco},{quantidade}\n")

    print(f"Produto '{nome}' criado!")
