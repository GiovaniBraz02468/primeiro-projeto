from datetime import datetime

arquivo = 'dados.txt'

def ler_dados():
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            linhas = f.readlines()
            produtos = []
            for linha in linhas:
                partes = linha.strip().split(";")
                if len(partes) == 5:  # Agora 5 campos: id;nome;preco;qtd;status
                    produtos.append({
                        "id": partes[0],
                        "nome": partes[1],
                        "preco": float(partes[2]),
                        "quantidade": int(partes[3]),
                        "status": partes[4].lower() == 'true'  # Converte string para boolean(retorna true or false)
                    })
            return produtos  
    except FileNotFoundError:
        return []

def salvar_dados(listar_produtos):
    with open(arquivo, 'w', encoding='utf-8') as f:
        for produto in listar_produtos:
            status_str = 'True' if produto['status'] else 'False'
            linha = f"{produto['id']};{produto['nome']};{produto['preco']};{produto['quantidade']};{status_str}\n"
            f.write(linha)

# ->  Verifica se produto existe
def produto_existe(id_produto):
    produtos = ler_dados()
    for produto in produtos:
        if produto['id'] == id_produto:
            return True
    return False

# -> Desativa produto (status = False)
def desativar_produto(id_produto):
    produtos = ler_dados()
    produto_encontrado = False
    
    for produto in produtos:
        if produto['id'] == id_produto:
            produto['status'] = False
            produto_encontrado = True
            break
    
    if not produto_encontrado:
        print('Produto não encontrado!')
        return False
    
    salvar_dados(produtos)
    print('Produto desativado com sucesso!')
    return True

def criar_produto(nome, preco, quantidade, status=True):  # Agora aceita status
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
        status_str = 'True' if status else 'False'
        f.write(f"{id_novo};{nome};{preco};{quantidade};{status_str}\n")
    
    status_texto = "ATIVO" if status else "INATIVO"
    print(f"Produto '{nome}' criado! Status: {status_texto}")

def listar_produtos():
    produtos = ler_dados()
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    
    print("\n=== LISTA DE PRODUTOS ===")
    for p in produtos:
        status_texto = "ATIVO" if p['status'] else "INATIVO"
        print(f"[{p['id']}] {p['nome']} | R$ {p['preco']:.2f} | Qtd: {p['quantidade']} | {status_texto}")

def buscar_produto_por_id(id):
    produtos = ler_dados()
    for produto in produtos:
        if produto['id'] == id:
            status_texto = "ATIVO" if produto['status'] else "INATIVO"
            print(f"ID: {produto['id']} | {produto['nome']} | R$ {produto['preco']:.2f} | Qtd: {produto['quantidade']} | {status_texto}")
            return produto
    print("Produto não encontrado!")
    return None

def atualizar_produto(id_produto, novo_nome, novo_preco, nova_quantidade, status):  # Agora aceita status
    produtos = ler_dados()
    produto_encontrado = False
    
    for produto in produtos:
        if produto['id'] == id_produto:
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
            produto['status'] = status  # Atualiza status
            produto_encontrado = True
            break  
    
    if not produto_encontrado:
        print('Produto não encontrado!')
        return
    
    salvar_dados(produtos)  
    status_texto = "ATIVO" if status else "INATIVO"
    print(f'Produto atualizado! Status: {status_texto}')

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
    print('Produto deletado permanentemente!')