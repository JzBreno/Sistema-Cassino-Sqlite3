

# Sistema de Cassino - Python 3 com SQLite3

Este é um projeto de um sistema de cassino desenvolvido em Python 3, utilizando SQLite3 como banco de dados. O sistema inclui um arquivo com funções (defs) que implementam o CRUD básico para manipulação dos dados de jogadores e suas pontuações.

## Estrutura do Projeto

```
├── main.py               # Arquivo principal do sistema que utiliza as funções do CRUD
├── defs.py               # Arquivo com as funções para operações CRUD no banco de dados
├── casino.db             # Banco de dados SQLite3 que armazena informações dos jogadores
└── README.md             # Este arquivo, documentação do projeto
```

## Funcionalidades

- **Cadastro de Jogadores:** Permite registrar novos jogadores com nome, e-mail, CPF e pontuação inicial.
- **Consulta de Jogadores:** Permite visualizar informações de todos os jogadores cadastrados.
- **Atualização de Pontuação:** Permite atualizar a pontuação de um jogador.
- **Exclusão de Jogadores:** Permite remover jogadores do sistema.

## Tecnologias Utilizadas

- **Python 3:** Linguagem de programação utilizada para a lógica do sistema.
- **SQLite3:** Banco de dados relacional embutido utilizado para armazenar dados dos jogadores.
- **SQLite3 Python Library:** Biblioteca padrão do Python para interação com o SQLite3.

## Instalação e Execução

1. **Clone o repositório:**
   ```
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. **Instale as dependências:**
   - Certifique-se de ter Python 3 instalado em seu ambiente.
   - Não é necessário instalar nenhuma biblioteca adicional além das padrões do Python.

3. **Execute o arquivo principal:**
   ```
   python main.py
   ```

4. **Interaja com o sistema:**
   - Siga as instruções no console para utilizar as funcionalidades do sistema de cassino.

## Exemplo de Uso

```python
# Exemplo de código no arquivo main.py
from defs import *

# Exemplo de utilização das funções do CRUD
# Cadastro de um novo jogador
novo_jogador = {
    'nome': 'João da Silva',
    'email': 'joao@example.com',
    'cpf': '123.456.789-00',
    'pontuacao': 1000
}
inserir_jogador(novo_jogador)

# Consulta de todos os jogadores
todos_jogadores = listar_jogadores()
for jogador in todos_jogadores:
    print(f"ID: {jogador['id']}, Nome: {jogador['nome']}, Pontuação: {jogador['pontuacao']}")

# Atualização da pontuação de um jogador
atualizar_pontuacao(1, 1500)  # Atualiza a pontuação do jogador com ID 1 para 1500 pontos

# Exclusão de um jogador
excluir_jogador(2)  # Remove o jogador com ID 2 do sistema
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir pull requests com melhorias, correções ou novas funcionalidades.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
