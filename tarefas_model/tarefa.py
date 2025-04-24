class Tarefa:
    def __init__(self, titulo, descricao, concluida=False):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida

    def is_concluida(self, nome_tarefa):
        self.concluida = True

    def imprimir(self):
        status = "X" if self.concluida else " "
        return f"[{status}] {self.titulo} - {self.descricao}"


    def to_dict(self):
        return {
            "titulo": self.titulo,
            "descricao": self.descricao,
            "concluida": self.concluida
        }

    def from_dict(data):
        return Tarefa(
            titulo=data["titulo"],
            descricao=data["descricao"],
            concluida=data.get("concluida", False),
        )

if __name__ =='__main__':
  pass