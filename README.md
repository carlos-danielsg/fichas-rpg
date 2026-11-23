# Gerenciador de Fichas de RPG

Fichas de RPG de mesa com rolador de dados e painel do mestre, pensado para mesas online no computador.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![Testes](https://img.shields.io/badge/testes-pytest-green)

## O que é

Em mesa, a ficha costuma viver em papel, PDF ou planilha. O mestre perde tempo perguntando PV e atributos, e os jogadores rolam dados em aplicativos separados, sem que ninguém veja o histórico.

Este projeto junta tudo em um só lugar:

- **Jogadores** criam e editam a própria ficha e rolam dados direto nela.
- **Mestre** vê o resumo de todos os personagens da campanha e as rolagens recentes.
- **Vários sistemas** de RPG, começando por Kids on Bikes e depois D&D 5e e Daggerheart.

É um projeto pessoal de estudo, construído em fases. Hoje existe o núcleo em Python, com o rolador de dados e a criação de fichas pelo terminal. O site vem nas próximas fases.

## Status

| Fase | O que entrega | Situação |
|---|---|---|
| 0 | Ambiente, Git e repositório | Concluída |
| 1 | Lógica em Python no terminal | **Em andamento** |
| 2 | Banco de dados (SQLite) | Planejada |
| 3 | API com Flask | Planejada |
| 4 | Frontend: ficha interativa | Planejada |
| 5 | Login, papéis e permissões | Planejada |
| 6 | Painel do mestre | Planejada |
| 7 | Publicação e polimento | Planejada |

## Funcionalidades

**Prontas**
- [x] Rolador de dados no formato `NdX` (`2d6`, `d20`), com modificador (`2d6+3`, `1d20-1`)
- [x] Limites de 1 a 30 dados e de 2 a 100 lados
- [x] Mensagens de erro claras para entradas inválidas
- [x] Criação de ficha de Kids on Bikes pelo terminal, com validações, perguntas repetidas quando a resposta é inválida e confirmação antes de criar
- [x] Testes automatizados com pytest (rolador e ficha)

**Próximas (Fase 1)**
- [ ] Salvar e carregar fichas em JSON
- [ ] Resumo do mestre, com uma linha por ficha
- [ ] Teste de atributo a partir da ficha
- [ ] Menu principal com todas as opções

**Planejadas**
- [ ] Cadastro e login, com papéis de mestre e jogador
- [ ] Campanhas, com entrada de jogadores por código
- [ ] Edição de ficha e rolagem a partir dela, com histórico
- [ ] Painel do mestre com resumo das fichas e rolagens recentes
- [ ] Sistemas: D&D 5e e Daggerheart

## Começando

Requisitos: **Python 3.12 ou superior** e **Git**. O projeto foi desenvolvido em Python 3.14.

```bash
git clone https://github.com/carlos-danielsg/fichas-rpg.git
cd fichas-rpg

python -m venv .venv
.venv\Scripts\Activate.ps1       # Windows (PowerShell)
source .venv/bin/activate        # Linux e macOS

pip install -r requirements.txt
python terminal/main.py          # cria uma ficha pelo terminal
python terminal/dados.py         # roda um exemplo do rolador
```

Para rodar os testes:

```bash
pytest -v
```

## Usando o rolador

```python
from dados import rolar_dados

total, rolagens, modificador = rolar_dados("2d6+3")
print(rolagens)      # por exemplo: [4, 5]
print(modificador)   # 3
print(total)         # 12 (soma dos dados mais o modificador)
```

A função devolve o **total** (já com o modificador), a **lista com cada dado** e o **modificador**. Se a entrada for inválida, levanta `ValueError` com uma mensagem explicativa:

```python
try:
    rolar_dados("31d6")
except ValueError as erro:
    print(f"Erro: {erro}")
```

| Entrada | Resultado |
|---|---|
| `2d6`, `D8` | Aceita, em maiúscula ou minúscula |
| `d20` | Aceita, e vale 1 dado |
| `2d6+3`, `1d20-1`, `2d6 + 3` | Aceita, com o modificador somado uma vez ao total |
| `abc`, `d`, `2d`, `2dx`, `2d6d3` | Recusada: formato inválido |
| `2d6+`, `2d6+x`, `d20+3-1` | Recusada: formato inválido |
| `-2d6`, `2d-6` | Recusada: formato inválido |
| `0d6` | Recusada: quantidade menor que 1 |
| `31d6` | Recusada: mais de 30 dados |
| `d1`, `d0` | Recusada: menos de 2 lados |
| `2d101` | Recusada: mais de 100 lados |

## Criando uma ficha

Execute `python terminal/main.py`. O programa pergunta, um campo por vez:

- Nome do personagem e nome do jogador (obrigatórios)
- Idade (só números)
- Medo e motivação
- Defeitos, separados por vírgula
- O dado de cada atributo: luta, fuga, mente, músculo, charme e garra

Se alguma resposta for inválida, a pergunta se repete. Cada atributo usa um dado diferente entre `d4`, `d6`, `d8`, `d10`, `d12` e `d20`. No fim, o programa mostra a ficha e pede confirmação (`s` ou `n`) antes de criá-la. Por enquanto a ficha ainda **não é salva** em arquivo, o que vem na próxima etapa.

Uma ficha é um dicionário:

```python
{
    "nome": "Carlos",
    "jogador": "Fulano",
    "sistema": "kids-on-bikes",
    "idade": 15,
    "medo": "Altura",
    "motivacao": "Ajudar a família",
    "defeitos": ["Teimoso", "Medroso"],
    "atributos": {
        "luta": "d20", "fuga": "d12", "mente": "d10",
        "musculo": "d8", "charme": "d6", "garra": "d4",
    },
}
```

## Tecnologias

| Camada | Tecnologia | Situação |
|---|---|---|
| Linguagem | Python | Em uso |
| Testes | pytest | Em uso |
| Banco de dados | SQLite | Planejado |
| Backend | Flask | Planejado |
| Frontend | HTML, CSS e JavaScript | Planejado |

## Como vai funcionar

```
  NAVEGADOR (HTML + CSS + JavaScript)
        |  HTTP + JSON
        v
  SERVIDOR FLASK (Python): login, permissões, regras e rolador
        |  SQL
        v
  BANCO SQLITE: usuários, campanhas, fichas e rolagens
```

A rolagem acontece **no servidor**, para o histórico ser confiável.

Cada sistema de RPG tem campos diferentes, então a ficha guarda os dados comuns em colunas e os atributos específicos em um campo JSON.

## Estrutura do projeto

```
fichas-rpg/
  README.md
  requirements.txt
  pytest.ini
  terminal/          # Fase 1: lógica em Python, sem interface web
    dados.py         # rolador de dados
    fichas.py        # regras e criação da ficha
    main.py          # menu de terminal
  tests/             # testes automatizados
    test_dados.py
    test_fichas.py
  docs/              # diário de bordo e documentação do processo
```

Na Fase 3 nasce a pasta `web/`, com a aplicação Flask, as páginas e os arquivos estáticos.

## Decisões técnicas

| Decisão | Motivo |
|---|---|
| Python em todo o backend | Menos linguagens novas, mais foco no fluxo completo |
| Flask | Framework pequeno, em que cada peça fica visível |
| SQLite | Um arquivo só, sem servidor, com SQL de verdade |
| Ficha com dados em JSON | Cada sistema tem campos diferentes |
| Ficha como dicionário | Converte direto para JSON e é simples de começar |
| Chaves em minúsculas e sem acento | Mais fáceis de digitar no código e com menos erros |
| Interpretação da expressão com regex | Descreve o formato inteiro de uma vez e recusa o que não bate |
| `interpretar` separada de `rolar_dados` | Cada função faz uma coisa, o que facilita testar e reaproveitar |
| Validação com `ValueError` | A função avisa o erro e quem chama decide o que mostrar |
| Menu pergunta de novo, função valida | O menu cuida da conversa, e `criar_ficha` é a última barreira para quando os dados vierem de outro lugar |
| Limites de 30 dados e 100 lados | Evitam entradas absurdas e abuso do servidor |
| Rolagem no servidor | Histórico confiável, sem trapaça pelo navegador |
| Computador primeiro, telas menores depois | A maioria das mesas online roda no desktop |
| Kids on Bikes como primeiro sistema | Ficha pequena, ideal para testar o desenho multi-sistema |

## Roadmap

- [x] **Fase 0:** ambiente, Git e repositório
- [ ] **Fase 1:** rolador, ficha, JSON, resumo do mestre, menu de terminal e testes
- [ ] **Fase 2:** banco de dados com SQLite
- [ ] **Fase 3:** API com Flask, testada sem interface
- [ ] **Fase 4:** frontend com ficha interativa
- [ ] **Fase 5:** login e permissões, com senhas em hash, checagem de acesso no servidor e proteção contra injeção de SQL e XSS
- [ ] **Fase 6:** painel do mestre com atualização automática
- [ ] **Fase 7:** publicação, testes com jogadores reais e polimento

**Ideias para depois:** atualização em tempo real, regra de dado que "explode" para Kids on Bikes, consulta a magias por APIs abertas de SRD, envio de rolagens para um canal de chat, painel de estatísticas das rolagens, exportação da ficha em PDF e uma interface em React com TypeScript.

## Documentação

- [Diário de bordo](docs/diario.md): o que foi feito em cada sessão e o que foi aprendido
- [Fluxo de trabalho com Git](docs/fluxo-de-trabalho.md): como as branches, commits e pull requests são usados no projeto

## Aviso sobre regras de jogo

Este projeto guarda os dados que os jogadores digitam e não reproduz o texto dos livros de regras. Regras, nomes e marcas pertencem aos seus respectivos detentores. Ao integrar conteúdo de SRDs, as licenças de cada um são conferidas.

## Autor

**[@carlos-danielsg](https://github.com/carlos-danielsg)**