from produtos import *

def mostrar_menu():
    print('\n===== SISTEMA DE PRODUTOS =====')
    print('1 - Criar produto')
    print('2 - Listar produtos')
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
            print('\n    CRIAR PRODUTO   ')
            nome = input('Digite o nome: ').strip()

            if nome == "":
                print('Nome invalido')
                continue
            
            #preço
            while True:
                try:
                    preco = float(input('Preço: '))
                    if preco <= 0:
                        print('Preço deve ser maior que 0!')
                        continue
                    break
                except ValueError:
                    print('Valor inválido no preço!')

            #quantidade
            while True:
                try:
                    quantidade = int(input('Quantidade: '))
                    if quantidade < 0:
                        print('Quantidade não pode ser negativa!')
                        continue
                    break
                except ValueError:
                    print('Valor inválido na quantidade!')

            criar_produto(nome, preco, quantidade)



        elif opcao == 2:
            listar_produtos()  

        elif opcao == 3:
            print('\n   ATUALIZAR PRODUTO   ')
            id_produto = input('ID do produto: ').strip()  
            nome = input('Novo nome: ').strip()

            
            while True:
                try:
                    preco = float(input('Novo preço: '))
                    if preco <= 0:
                        print('Preço deve ser maior que 0!')
                        continue
                    break
                except ValueError:
                    print('Valor inválido no preço!')

            #quantidade
            while True:
                try:
                    quantidade = int(input('Nova quantidade: '))
                    if quantidade < 0:
                        print('Quantidade não pode ser negativa!')
                        continue
                    break
                except ValueError:
                    print('Valor inválido na quantidade!')

            atualizar_produto(id_produto, nome, preco, quantidade)


        elif opcao == 4:
            print('\n   REMOVER PRODUTO   ')
            id_produto = input('Digite o ID do produto a ser removido: ').strip()
    
            if id_produto == "":
                print("ID não pode estar vazio!")
                continue
        
            deletar_produto(id_produto)

        elif opcao == 5:
            print('Volte sempre!')
            print('Saindo do sistema...')
            break

        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()
