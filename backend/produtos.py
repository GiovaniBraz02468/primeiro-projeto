from datetime import datetime

arquivo = 'dados.txt'

def ler_dados():
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            linhas = f.readlines()
            produtos = []
            for linha in linhas:
                partes = linha.strip().split(";")
                if len(partes) == 4:  
                    produtos.append({
                        "id": partes[0],
                        "nome": partes[1],
                        "preco": float(partes[2]),
                        "quantidade": int(partes[3])
                    })
            return produtos  
    except FileNotFoundError:
        return []

def salvar_dados(listar_produtos):
    with open(arquivo, 'w', encoding='utf-8') as f:
        for produto in listar_produtos:
            linha = f"{produto['id']};{produto['nome']};{produto['preco']};{produto['quantidade']}\n"
            f.write(linha)

def criar_produto(nome, preco, quantidade):
    if nome.strip() == "":  
        print("Nome não pode estar vazio.")
        return
    if preco <= 0:
        print("Preço deve ser maior que zero.")
        return
    if quantidade < 0:
        print("A quantidade não pode ser negativa.")
        return
    
    nome = nome.strip()
    id_novo = datetime.now().strftime("%Y%m%d%H%M%S")
    
    with open(arquivo, "a", encoding="utf-8") as f:
        f.write(f"{id_novo};{nome};{preco};{quantidade}\n")
    
    print(f"Produto '{nome}' criado!")

def listar_produtos():
    produtos = ler_dados()
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    
    print("\n=== LISTA DE PRODUTOS ===")
    for p in produtos:
        print(f"ID: {p['id']} | {p['nome']} | R$ {p['preco']:.2f} | Qtd: {p['quantidade']}")

def buscar_produto_por_id(id):
    produtos = ler_dados()
    for produto in produtos:
        if produto['id'] == id:
            print(f"ID: {produto['id']} | {produto['nome']} | R$ {produto['preco']:.2f} | Qtd: {produto['quantidade']}")
            return produto
    print("Produto não encontrado!")
    return None

def atualizar_produto(id, novo_nome, novo_preco, nova_quantidade):
    produtos = ler_dados()
    produto_encontrado = False
    
    for produto in produtos:
        if produto['id'] == id:
            if novo_nome.strip() == '':
                print('Nome inválido!')
                return
            if novo_preco <= 0:
                print('Preço inválido!')
                return
            if nova_quantidade < 0:
                print('Quantidade inválida!')
                return
            
            produto['nome'] = novo_nome.strip()
            produto['preco'] = novo_preco
            produto['quantidade'] = nova_quantidade
            produto_encontrado = True
            break  
    
    if not produto_encontrado:
        print('Produto não encontrado!')
        return
    
    salvar_dados(produtos)  
    print('Produto atualizado com sucesso!')

def deletar_produto(id):
    produtos = ler_dados()
    nova_lista = []
    produto_encontrado = False
    
    for produto in produtos:
        if produto['id'] == id:
            produto_encontrado = True
        else:
            nova_lista.append(produto)
    
    if not produto_encontrado:
        print('Produto não encontrado!')
        return
    
    salvar_dados(nova_lista)
    print('Produto removido com sucesso!')
