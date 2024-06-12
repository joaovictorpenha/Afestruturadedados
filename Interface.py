from Gerenciamentodepedido import GerenciamentoPedidos
from Pedido import Pedido
from Menu import menu

def main():
    gerenciamento = GerenciamentoPedidos()

    while True:
        opcao = menu()
        if opcao == 1:
            id = int(input("ID do Pedido: "))
            while True:
                prioridade = int(input("Prioridade do Pedido (1-3): "))
                if 1 <= prioridade <= 3:
                    break
                else:
                    print("Prioridade inválida. Por favor, insira um valor entre 1 e 3.")
            descricao = input("Descrição do Pedido: ")
            pedido = Pedido(id, prioridade, descricao)
            gerenciamento.adicionar_pedido(pedido)
            print("Pedido adicionado com sucesso!")
        elif opcao == 2:
            id = int(input("ID do Pedido: "))
            gerenciamento.remover_pedido(id)
            print("Pedido removido com sucesso!")
        elif opcao == 3:
            print("Lista de Pedidos Ordenados por Prioridade:")
            gerenciamento.listar_pedidos_ordenados()
        elif opcao == 4:
            id = int(input("ID do Pedido: "))
            pedido = gerenciamento.buscar_pedido(id)
            if pedido:
                print("Pedido encontrado:", pedido)
            else:
                print("Pedido não encontrado.")
        elif opcao == 5:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
