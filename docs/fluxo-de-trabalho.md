# Fluxo de trabalho com Git

Este documento descreve como o repositório é organizado. Ele existe para o histórico do projeto ficar claro, tanto para quem lê o GitHub quanto para quem retoma o trabalho depois de alguns dias.

## Princípios

- A branch `main` **sempre funciona**. Só entra nela o que já foi testado.
- Cada fase ou assunto tem a **sua branch**, com nome curto, como `fase-1-rolador` ou `login-mestre`.
- **Commits pequenos**, com mensagem que diz o que mudou.
- Ao fim de cada fase, um **Pull Request** junta a branch na `main`.

## Por que trabalhar assim

- **Segurança:** se algo quebrar na branch, a `main` continua intacta.
- **Histórico legível:** cada fase vira um bloco de commits com começo e fim.
- **Revisão:** o Pull Request mostra todas as mudanças de uma vez, e relê-las antes do merge pega erros.
- **Prática de equipe:** é o fluxo usado na maior parte dos times de software.

## Passo a passo de uma fase

```bash
git switch main
git pull                          # traz a main atualizada
git switch -c fase-2-banco        # cria a branch da fase e entra nela

# ... edita, testa ...
git status                        # o que mudou?
git diff                          # o que exatamente mudou?
git add arquivo.py
git commit -m "adiciona tabela de fichas"
git push -u origin fase-2-banco   # na primeira vez; depois, só git push
```

Ao terminar a fase:

1. Abrir o Pull Request no GitHub.
2. Revisar a aba **Files changed**.
3. Fazer o **merge** na `main`.
4. Voltar ao computador: `git switch main` e `git pull`.

## Mensagens de commit

Curtas, no presente, dizendo o que o commit faz:

- `adiciona rolador de dados com validação de entrada`
- `corrige mensagem de erro no chamador`
- `adiciona testes de faixa e formato do rolador`

## O que não vai para o repositório

`.venv/`, `__pycache__/`, `.pytest_cache/`, `.vscode/`, arquivos de banco local, chaves e senhas. A lista fica no `.gitignore`.