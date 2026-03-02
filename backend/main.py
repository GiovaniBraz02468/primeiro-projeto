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

            # Criar produto com status ATIVO por padrão (True)
            criar_produto(nome, preco, quantidade, True)

        elif opcao == 2:
            listar_produtos()  

        elif opcao == 3:
            print('\n   ATUALIZAR PRODUTO   ')
            id_produto = input('ID do produto: ').strip()
            
            if id_produto == "":
                print("ID não pode estar vazio!")
                continue
              
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

            while True:
                try:
                    quantidade = int(input('Nova quantidade: '))
                    if quantidade < 0:
                        print('Quantidade não pode ser negativa!')
                        continue
                    break
                except ValueError:
                    print('Valor inválido na quantidade!')

            # Perguntar sobre status após validação
            print('\nStatus atual do produto será mantido.')
            print('Deseja manter o produto ATIVO ou DESATIVAR?')
            print('1 - Manter ATIVO')
            print('2 - Desativar')
            
            while True:
                try:
                    escolha_status = int(input('Escolha (1 ou 2): '))
                    if escolha_status == 1:
                        status = True
                        break
                    elif escolha_status == 2:
                        status = False
                        break
                    else:
                        print('Digite apenas 1 ou 2!')
                except ValueError:
                    print('Digite apenas números!')
            
            atualizar_produto(id_produto, nome, preco, quantidade, status)

        elif opcao == 4:
            print('\n   GERENCIAR PRODUTO   ')
            id_produto = input('Digite o ID do produto: ').strip()

            if id_produto == "":
                print("ID não pode estar vazio!")
                continue
            
            # Confirmar se produto existe antes das opções
            if not produto_existe(id_produto):
                print("Produto não encontrado!")
                continue
            
            print('\nO que deseja fazer com este produto?')
            print('1 - Desativar (soft delete)')
            print('2 - Deletar permanentemente')
            print('3 - Voltar ao menu principal')
            
            while True:
                try:
                    escolha = int(input('Escolha (1, 2 ou 3): '))
                    
                    if escolha == 1:
                        desativar_produto(id_produto)
                        break
                        
                    elif escolha == 2:
                        confirmacao = input('TEM CERTEZA? Digite "SIM" para confirmar: ').strip().upper()
                        if confirmacao == "SIM":
                            deletar_produto(id_produto)
                        else:
                            print('Operação cancelada!')
                        break
                        
                    elif escolha == 3:
                        print('Voltando ao menu principal...')
                        break
                    
                    else:
                        print('Opção inválida! Digite 1, 2 ou 3.')
                        
                except ValueError:
                    print('Digite apenas números!')

        elif opcao == 5:
            print('Volte sempre!')
            print('Saindo do sistema...')
            break

        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()