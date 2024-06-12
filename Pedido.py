class Pedido:
    def __init__(self, id, prioridade, descricao):
        if prioridade < 1 or prioridade > 3:
            raise ValueError("A prioridade deve estar entre 1 e 3.")
        self.id = id
        self.prioridade = prioridade
        self.descricao = descricao

    def __repr__(self):
        return f"Pedido(id={self.id}, prioridade={self.prioridade}, descricao={self.descricao})"
