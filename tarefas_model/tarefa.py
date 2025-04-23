import random
class Tarefa:
    def __init__(self, titulo, descricao, concluida=False):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida

    def is_concluida(self):
        self.concluida = True

    def imprimir(self):
        status = "X" if self.concluida else " "
        return f"[{status}] {self.titulo} - {self.descricao}"

    def def_id(self):
        return random.randint(1, 1000)

    def to_dict(self):
        return {
            "id": self.def_id(),
            "titulo": self.titulo,
            "descricao": self.descricao,
            "concluida": self.concluida
        }

if __name__ =='__main__':
  pass
# temos que passar essa classe para salvar em um json