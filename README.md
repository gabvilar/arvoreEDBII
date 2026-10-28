# Amazon Engineering Challenge — Árvores Balanceadas (AVL e Rubro-Negra)

**Autor:** Gabriel Brandão Vilar — 20250035487 — IMD0039 Estruturas de Dados Básicas II

Protótipo em Python para registrar, localizar e remover identificadores de 
encomendas durante a Black Friday. Implementa, do zero, uma árvore AVL e
uma árvore Rubro-Negra, sem bibliotecas de balanceamento.

## Arquivos
| Arquivo | Descrição |
|---|---|
| `avl_tree.py` | Árvore AVL (rotações LL, RR, LR, RL) |
| `rb_tree.py` | Árvore Rubro-Negra (recoloração e rotações, nó sentinela NIL) |
| `main.py` | Programa interativo: o usuário escolhe AVL ou Rubro-Negra na execução |
| `comparison.py` | Comparação de altura e rotações com os mesmos dados |

## Como executar
```bash
python main.py          # programa interativo
python comparison.py    # comparação de altura, rotações e tempo em uma seed fixa
```

## Operações
Inserção, remoção, busca, percurso em ordem e impressão da árvore. 
Na Rubro-Negra, cada nó aparece com `(R)` ou `(B)` e cores ANSI no terminal.

## Decisões de implementação
- Valores repetidos não são inseridos.
- Busca ou remoção de elemento inexistente não gera erro.
- Remoção de nó com dois filhos usa o sucessor em ordem.
- Altura contada em nós (vazia = 0, folha = 1).
- Rotação dupla (LR/RL) conta como 2 rotações.

## Comparações
- Utilização de 10 mil ID's nas árvores de comparação 
- Seed fixa - 20250035487
- Utilização de mediana no tempo para evitar erros de benchmark
