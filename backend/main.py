from produtos import *

# MENU E CONTROLE DO SISTEMA

def mostrar_menu():
    print('\n ===== SISTEMA DE PRODUTOS =====')
    print('1 - Criar produto')
    print('2 - Listar produto')
    print('3 - Atualizar produto')
    print('4 - Deletar produto')
    print('5 - Sair')

def main():

    while True:
        mostrar_menu()

        try:
            opcao = int(input('Escolha uma opção: '))
        except ValueError:
            print('Digite apenas números!')
            continue

        if opcao == 1:
            nome =  input('Nome do produto: ')
            try:
                preco = float(input('Preço: '))
                quantidade = int(input('Quantidade: '))
            except ValueError:
                print('Preço e quantidade devem ser números!')
                continue

            criar_produto(nome, preco, quantidade)


        elif opcao == 2:
            listar_produtos()

        elif opcao == 3:
            try:
                id = input('ID do produto: ')
                nome = str(input('Novo nome: '))
                preco = float(input('Novo preço: '))
                quantidade = int(input('Nova quantidade: '))
            except ValueError:
                print('Valor inválido!')
                continue

            atualizar_produto(id, nome, preco, quantidade)

        elif opcao == 4:
            try:
                id = input('Digite o ID do produto a ser removido: ')
            except ValueError:
                print('ID invalido')
                continue

            deletar_produto(id)

        elif opcao == 5:
            print('Volte sempre!')
            print('Saindo do sistema...')
            break

        else:
            print('Ops... Opção inválida. Tente novamente')


main()
