from datetime import datetime
import os
arquivo = 'dados.txt'


def ler_dados():
    pass

def salvar_dados():
    with open(arquivo, 'w', encoding='utf-8') as arquivo:
        for produto in listar_produtos:
            linha = f'{produto['id']}, {produto['nome']}, {produto['preco']}, {produto['quantidade']} \n'
            arquivo.write(linha)


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

def listar_produtos():
    pass

def buscar_produto_por_id(id):
    pass

def atualizar_produto(id, novo_nome, novo_preco, nova_quantidade):
    produtos = ler_dados()
    produto_encontrado = False

    for produto in produtos:
        if produto['id'] ==  id:
            
            if novo_nome.strip() == '':
                print('Nome inválido!')
                return

            if novo_preco <= 0:
                print('Preço inválido!')
                return
            
            if nova_quantidade < 0:
                print('Quantidade inválida')
                return
            
            produto['nome'] = novo_nome
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
    pass