# Gerenciador de Fichas de RPG

Site para guardar fichas de RPG de mesa. O **mestre** vê um resumo rápido de todos os personagens da campanha, e cada **jogador** edita a própria ficha e rola dados direto nela.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![Testes](https://img.shields.io/badge/testes-pytest-green)

> **Projeto pessoal de estudo**, desenvolvido em fases, com foco em aprender de ponta a ponta: lógica em Python, banco de dados, API, frontend, autenticação e publicação.

---

## Sumário

- [Por que este projeto existe](#por-que-este-projeto-existe)
- [Status atual](#status-atual)
- [Funcionalidades](#funcionalidades)
- [Como usar o rolador de dados](#como-usar-o-rolador-de-dados)
- [Tecnologias](#tecnologias)
- [Arquitetura planejada](#arquitetura-planejada)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Como rodar localmente](#como-rodar-localmente)
- [Testes](#testes)
- [Modelo de dados planejado](#modelo-de-dados-planejado)
- [Decisões técnicas](#decisões-técnicas)
- [Roadmap](#roadmap)
- [Fluxo de trabalho com Git](#fluxo-de-trabalho-com-git)
- [Segurança](#segurança)
- [Ideias para o futuro](#ideias-para-o-futuro)
- [Aviso sobre regras de jogo](#aviso-sobre-regras-de-jogo)
- [Autor](#autor)

---

## Por que este projeto existe

Em mesa, a ficha costuma viver em papel, PDF ou planilha. O mestre perde tempo perguntando PV, atributos e habilidades de cada jogador, e os jogadores rolam dados em aplicativos separados, sem que ninguém veja o histórico.

A ideia é juntar **ficha, rolador e visão do mestre** em um só lugar, pensado principalmente para **mesas online usadas no computador**, com o layout adaptável a telas menores.

## Status atual

| Fase | Descrição | Situação |
|---|---|---|
| 0 | Ambiente, Git e repositório | Concluída |
| 1 | Lógica em Python no terminal | **Em andamento** |
| 2 | Banco de dados (SQLite) | Não iniciada |
| 3 | API com Flask | Não iniciada |
| 4 | Frontend (HTML, CSS e JavaScript) | Não iniciada |
| 5 | Login e permissões | Não iniciada |
| 6 | Painel do mestre | Não iniciada |
| 7 | Publicação e polimento | Não iniciada |

## Funcionalidades

**Já implementado**
- [x] Rolador de dados no formato `NdX` (ex.: `2d6`, `d20`), com validação de entrada
- [x] Limites de segurança: de 1 a 30 dados e de 2 a 100 lados
- [x] Mensagens de erro claras para entradas inválidas
- [x] Testes automatizados com pytest (em ampliação)

**Em desenvolvimento (Fase 1)**
- [ ] Modificadores na expressão (`2d6+3`, `1d20-1`)
- [ ] Fichas salvas em JSON
- [ ] Menu de terminal e resumo para o mestre
- [ ] Teste de atributo a partir da ficha

**Planejado**
- [ ] Cadastro e login, com papéis de mestre e jogador
- [ ] Mestre cria campanhas e jogadores entram com um código
- [ ] Edição da ficha (atributos, PV, habilidades)
- [ ] Rolagem a partir da ficha, com histórico por campanha
- [ ] Painel do mestre com resumo das fichas e rolagens recentes

**Sistemas de RPG**
- [ ] Kids on Bikes (sistema inicial de teste, por ter ficha pequena)
- [ ] D&D 5e
- [ ] Daggerheart

## Como usar o rolador de dados

O rolador fica em `terminal/dados.py` e expõe a função `rolar_dados`.

```python
from dados import rolar_dados

total, rolagens = rolar_dados("2d6")
print(rolagens)   # por exemplo: [4, 2]
print(total)      # por exemplo: 6
```

A função devolve uma tupla: o **total** e a **lista com cada dado**. Se a entrada for inválida, levanta `ValueError` com uma mensagem explicativa, e quem chama decide o que mostrar:

```python
try:
    total, rolagens = rolar_dados("31d6")
except ValueError as erro:
    print(f"Erro: {erro}")
```

**Entradas aceitas e recusadas**

| Entrada | Resultado |
|---|---|
| `2d6`, `D8` | Aceita (maiúscula ou minúscula) |
| `d20` | Aceita, e vale 1 dado |
| `abc`, `d`, `2d`, `2dx`, `2d6d3` | Recusada: formato inválido |
| `0d6`, `-2d6` | Recusada: quantidade menor que 1 |
| `31d6` | Recusada: mais de 30 dados |
| `d1` | Recusada: menos de 2 lados |
| `2d101` | Recusada: mais de 100 lados |
| `2d6+3` | Ainda **não suportada** (em desenvolvimento) |

Para ver uma rolagem de exemplo, execute o arquivo diretamente: `python terminal/dados.py`.

## Tecnologias

| Camada | Tecnologia | Situação |
|---|---|---|
| Linguagem | Python | Em uso |
| Testes | pytest | Em uso |
| Controle de versão | Git e GitHub | Em uso |
| Banco de dados | SQLite | Planejado |
| Backend | Flask | Planejado |
| Frontend | HTML, CSS e JavaScript | Planejado |

## Arquitetura planejada

```
  NAVEGADOR (HTML + CSS + JavaScript)
     - ficha, botões de rolar, painel do mestre
        |
        |  HTTP + JSON
        v
  SERVIDOR FLASK (Python)
     - login e permissões, regras, rolador de dados
        |
        |  SQL
        v
  BANCO SQLITE
     - usuários, campanhas, fichas, rolagens
```

A rolagem é feita **no servidor**, para ter histórico confiável e evitar trapaça no navegador.

## Estrutura do projeto

```
fichas-rpg/
  README.md            # esta página
  requirements.txt     # bibliotecas usadas
  pytest.ini           # configuração dos testes
  .gitignore
  terminal/            # Fase 1: lógica em Python, sem interface
    dados.py           # rolador de dados
  tests/               # testes automatizados
    test_dados.py
  docs/                # diário de bordo e anotações
    diario.md
```

Pastas que ainda vão nascer, conforme as fases:

```
  web/                 # Fases 3 a 6
    app.py             # páginas e rotas
    db.py              # conexão com o banco
    schema.sql         # tabelas
    templates/         # páginas HTML
    static/            # CSS e JavaScript
```

## Como rodar localmente

Requisitos: **Python 3.12 ou superior** e **Git**. O projeto foi desenvolvido em Python 3.14.

```bash
# 1. Clonar o repositório
git clone https://github.com/carlos-danielsg/fichas-rpg.git
cd fichas-rpg

# 2. Criar o ambiente virtual
python -m venv .venv

# 3. Ativar o ambiente
.venv\Scripts\Activate.ps1       # Windows (PowerShell)
source .venv/bin/activate        # Linux e macOS

# 4. Instalar as dependências
pip install -r requirements.txt

# 5. Rodar o exemplo do rolador
python terminal/dados.py
```

Quando o ambiente estiver ativo, o terminal mostra `(.venv)` no começo da linha.

## Testes

```bash
pytest -v
```

O arquivo `pytest.ini` aponta para a pasta `terminal/`, para os testes em `tests/` encontrarem o código. Cobertura atual dos testes do rolador:
- Estrutura do resultado (quantidade de dados, soma e intervalo de cada dado)
- Formatos válidos (`d20`, `D8`)
- Formatos inválidos e valores fora dos limites, com conferência das mensagens
- Limites exatos (último valor aceito e primeiro recusado)

## Modelo de dados planejado

| Entidade | Campos principais | Relações |
|---|---|---|
| Usuário | id, nome, senha (hash), papel | pode ser mestre ou jogador |
| Campanha | id, nome, mestre | tem várias fichas |
| Ficha | id, nome, sistema, dono, campanha, dados (JSON) | tem várias rolagens |
| Rolagem | id, ficha, expressão, resultados, total, data | pertence a uma ficha e a uma campanha |

Cada sistema de RPG tem campos diferentes. Por isso, a ficha guarda os dados comuns em colunas e os atributos específicos em um campo JSON. Exemplo ilustrativo, para um sistema em que cada atributo tem um tipo de dado:

```json
{
  "nome": "Mira",
  "sistema": "kids-on-bikes",
  "pv": 12,
  "atributos": { "Brains": "d8", "Brawn": "d4" },
  "habilidades": ["Furtiva", "Corajosa"]
}
```

## Decisões técnicas

| Decisão | Motivo |
|---|---|
| **Python em todo o backend** | Reduz o número de linguagens novas e mantém o foco em aprender o fluxo completo |
| **Flask** | Framework pequeno, em que cada peça (rota, requisição, resposta) fica visível |
| **SQLite** | Um arquivo só, sem servidor, com SQL de verdade |
| **Ficha com dados em JSON** | Cada sistema tem campos diferentes, e o JSON evita uma coluna por atributo |
| **Dicionário em vez de classe, no início** | Converte direto para JSON e é mais simples; as dataclasses podem ser testadas depois |
| **Validação com `ValueError`** | A função avisa o erro e quem chama decide o que mostrar, o que serve para o terminal e para o site |
| **Limites de 30 dados e 100 lados** | Evitam entradas absurdas e abuso do servidor |
| **Rolagem no servidor** | Histórico confiável e sem trapaça pelo navegador |
| **Computador primeiro, telas menores depois** | A maioria das mesas online roda no desktop |
| **Kids on Bikes como primeiro sistema** | Ficha pequena, ideal para testar o desenho multi-sistema antes de D&D e Daggerheart |

## Roadmap

- [x] **Fase 0:** ambiente, Git e repositório
- [ ] **Fase 1:** lógica em Python no terminal (rolador, fichas em JSON, testes)
- [ ] **Fase 2:** banco de dados com SQLite
- [ ] **Fase 3:** API com Flask, testada sem interface
- [ ] **Fase 4:** frontend com ficha interativa
- [ ] **Fase 5:** login, papéis e permissões
- [ ] **Fase 6:** painel do mestre com atualização automática
- [ ] **Fase 7:** publicação, testes com jogadores reais e polimento

## Fluxo de trabalho com Git

- A branch `main` deve estar sempre funcionando.
- Cada fase ou assunto vira uma branch própria, como `fase-1-rolador`.
- Commits pequenos, com mensagem que diz o que mudou.
- Ao fim de cada fase, abre-se um Pull Request e faz-se o merge na `main`.
- O progresso e os bloqueios de cada sessão ficam em [`docs/diario.md`](docs/diario.md).

## Segurança

Itens previstos para as Fases 3 a 5:
- Senhas guardadas apenas como **hash**, nunca em texto
- Permissões checadas no servidor: o jogador só acessa a própria ficha, e o mestre só as da sua campanha
- Consultas ao banco com parâmetros, contra injeção de SQL
- Conteúdo digitado pelos usuários escapado nas páginas, contra XSS
- Chave secreta e configurações fora do repositório, em variáveis de ambiente

## Ideias para o futuro

- Atualização em tempo real do painel do mestre (WebSockets)
- Regra de dado que "explode" (rola de novo ao tirar o valor máximo), para Kids on Bikes, conferida no livro de regras
- Consulta a magias e equipamentos por APIs abertas de SRD, com cache
- Envio das rolagens para um canal de chat
- Atalhos de teclado e modo compacto, para deixar a ficha ao lado da chamada
- Painel de estatísticas das rolagens (média por jogador, sequências de críticos), em Python com Streamlit ou Power BI
- Inventário, magias, condições e iniciativa
- Exportar a ficha em PDF
- Interface em React com TypeScript, reaproveitando a API

## Aviso sobre regras de jogo

Este projeto guarda os dados que os jogadores digitam e não reproduz o texto dos livros de regras. Regras, nomes e marcas pertencem aos seus respectivos detentores. Ao integrar conteúdo de SRDs, confira as licenças de cada um.

## Autor

**[@carlos-danielsg](https://github.com/carlos-danielsg)**