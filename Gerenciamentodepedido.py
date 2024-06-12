from Lista import ListaSimplesEncadeada
from Arvore import BST
from Bubble import bubble_sort

class GerenciamentoPedidos:
    def __init__(self):
        # Inicializa a classe de gerenciamento de pedidos.
        self.lista_pedidos = ListaSimplesEncadeada()
        self.arvore_pedidos = BST()

    def adicionar_pedido(self, pedido):
        # Adiciona um pedido na lista e na árvore.
        self.lista_pedidos.append(pedido)
        self.arvore_pedidos.insert(pedido)

    def remover_pedido(self, pedido_id):
        # Remove um pedido da lista e da árvore pelo ID.
        node = self.arvore_pedidos.search(pedido_id)
        if node:
            # Se o pedido for encontrado na árvore, remove da lista e da árvore.
            self.lista_pedidos.remove(node.pedido)
            self.arvore_pedidos.delete(pedido_id)

    def listar_pedidos_ordenados(self):
        # Lista todos os pedidos de forma ordenada.
        pedidos = self.lista_pedidos.to_list()
        # Converte a lista ligada em uma lista comum para ordenar.
        bubble_sort(pedidos)
        # Ordena a lista de pedidos usando bubble sort.
        self.lista_pedidos.from_list(pedidos)
        # Converte a lista ordenada de volta para a lista ligada.
        self.lista_pedidos.display()
        # Exibe a lista de pedidos ordenada.

    def buscar_pedido(self, pedido_id):
        # Busca um pedido na árvore pelo ID.
        node = self.arvore_pedidos.search(pedido_id)
        if node:
            # Se o pedido for encontrado, retorna o pedido.
            return node.pedido
        # Se não for encontrado, retorna None.
        return None
