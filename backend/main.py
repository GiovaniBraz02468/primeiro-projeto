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
            nome = input('Nome do produto: ').strip()
            try:
                preco = float(input('Preço: '))
                quantidade = int(input('Quantidade: '))
                criar_produto(nome, preco, quantidade) 
            except ValueError:
                print('Preço e quantidade devem ser números!')
                continue

        elif opcao == 2:
            listar_produtos()  

        elif opcao == 3:
            try:
                id_produto = input('ID do produto: ').strip()  
                nome = input('Novo nome: ').strip()
                preco = float(input('Novo preço: '))
                quantidade = int(input('Nova quantidade: '))
                atualizar_produto(id_produto, nome, preco, quantidade)  
            except ValueError:
                print('Valor inválido!')
                continue

        elif opcao == 4:
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
