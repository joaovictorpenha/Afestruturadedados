class BSTNode:
    def __init__(self, pedido):
        self.pedido = pedido
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, pedido):
        # Insere um novo pedido na árvore.
        if not self.root:
            # Se a árvore está vazia, o novo pedido se torna a raiz.
            self.root = BSTNode(pedido)
        else:
            # Caso contrário, chama a função auxiliar para inserir o pedido na posição correta.
            self._insert(self.root, pedido)

    def _insert(self, current_node, pedido):
        # Função auxiliar para inserir um novo pedido na árvore de forma recursiva.
        if pedido.id < current_node.pedido.id:
            # Se o ID do pedido é menor que o ID do pedido no nó atual, vai para a subárvore esquerda.
            if current_node.left is None:
                # Se não houver subárvore esquerda, insere o pedido aqui.
                current_node.left = BSTNode(pedido)
            else:
                # Caso contrário, continua a busca na subárvore esquerda.
                self._insert(current_node.left, pedido)
        elif pedido.id > current_node.pedido.id:
            # Se o ID do pedido é maior que o ID do pedido no nó atual, vai para a subárvore direita.
            if current_node.right is None:
                # Se não houver subárvore direita, insere o pedido aqui.
                current_node.right = BSTNode(pedido)
            else:
                # Caso contrário, continua a busca na subárvore direita.
                self._insert(current_node.right, pedido)

    def search(self, pedido_id):
        # Procura um pedido na árvore pelo ID.
        return self._search(self.root, pedido_id)

    def _search(self, current_node, pedido_id):
        # Função auxiliar para buscar um pedido de forma recursiva.
        if current_node is None or current_node.pedido.id == pedido_id:
            # Retorna o nó atual se ele for None ou se o pedido tiver o ID procurado.
            return current_node
        if pedido_id < current_node.pedido.id:
            # Se o ID procurado for menor, busca na subárvore esquerda.
            return self._search(current_node.left, pedido_id)
        # Se o ID procurado for maior, busca na subárvore direita.
        return self._search(current_node.right, pedido_id)

    def delete(self, pedido_id):
        # Deleta um pedido da árvore pelo ID.
        self.root = self._delete(self.root, pedido_id)

    def _delete(self, current_node, pedido_id):
        # Função auxiliar para deletar um pedido de forma recursiva.
        if current_node is None:
            # Se o nó atual é None, retorna None.
            return current_node

        if pedido_id < current_node.pedido.id:
            # Se o ID do pedido a ser deletado é menor, vai para a subárvore esquerda.
            current_node.left = self._delete(current_node.left, pedido_id)
        elif pedido_id > current_node.pedido.id:
            # Se o ID do pedido a ser deletado é maior, vai para a subárvore direita.
            current_node.right = self._delete(current_node.right, pedido_id)
        else:
            # Se o ID do pedido é igual, este é o nó a ser deletado.
            if current_node.left is None:
                # Se não houver filho à esquerda, retorna o filho à direita.
                return current_node.right
            elif current_node.right is None:
                # Se não houver filho à direita, retorna o filho à esquerda.
                return current_node.left

            # Se o nó tem dois filhos, encontra o menor valor na subárvore direita.
            temp = self._min_value_node(current_node.right)
            # Substitui o pedido do nó atual pelo pedido encontrado.
            current_node.pedido = temp.pedido
            # Deleta o nó com o menor valor na subárvore direita.
            current_node.right = self._delete(current_node.right, temp.pedido.id)

        return current_node

    def _min_value_node(self, node):
        # Encontra o nó com o menor valor (mais à esquerda) em uma subárvore.
        current = node
        while current.left:
            current = current.left
        return current

    def in_order_traversal(self, node, result):
        # Realiza a travessia in-order da árvore e armazena os pedidos em uma lista.
        if node:
            # Primeiro, visita o filho à esquerda.
            self.in_order_traversal(node.left, result)
            # Depois, visita o nó atual e adiciona seu pedido à lista de resultados.
            result.append(node.pedido)
            # Por fim, visita o filho à direita.
            self.in_order_traversal(node.right, result)
        return result
