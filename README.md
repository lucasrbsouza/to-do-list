# 📋 Gerenciador de Tarefas (CLI)

Este é um projeto simples de **gerenciador de tarefas** feito em Python, com persistência de dados em arquivo JSON. Ele permite **criar**, **listar**, **concluir** e **remover tarefas** por meio de um menu interativo no terminal.

## 🧠 Funcionalidades

- [x] Criar tarefa com título e descrição  
- [x] Listar todas as tarefas  
- [x] Marcar uma tarefa como concluída  
- [x] Remover tarefa  
- [ ] Deletar tarefas em massa (em breve)

## 📁 Estrutura do Projeto

```
gerenciador_tarefas/
├── tarefas_model/
│   ├── tarefa.py
│   └── lista_de_Tarefas.py
├── data_tarefas/
│   └── data_tarefas.py
├── db_/
│   └── tarefa.json
├── main.py
└── README.md
```

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/gerenciador_tarefas.git
   cd gerenciador_tarefas
   ```

2. Execute o programa:
   ```bash
   python3 main.py
   ```

## 💡 Exemplo de Uso

```
O que você quer fazer?
a) Criar tarefa
b) Listar tarefas
c) Deletar tarefas (em breve)
d) Concluir tarefa
e) Sair do programa
> a
Título da tarefa: Estudar Python
Descrição da tarefa: Rever listas e dicionários
--- Tarefa criada com sucesso! ---
```

## 🛠️ Tecnologias Utilizadas

- Python 3
- Módulo `json` para persistência de dados
- Módulo `pathlib` para manipulação de arquivos

## 📌 Melhorias Futuras

- Deletar múltiplas tarefas de uma vez
- Interface gráfica com Tkinter ou Web
- Adição de categorias/tags por tarefa
- Suporte a datas de vencimento

## 🤝 Contribuição

Sinta-se à vontade para abrir issues ou pull requests. Qualquer contribuição é bem-vinda!

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
