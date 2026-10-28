from avl_tree import AVLTree
from rb_tree import RBTree


def ler_inteiro(msg):
    try:
        return int(input(msg).strip())
    except ValueError:
        print("Valor invalido: digite um número inteiro.")
        return None


def escolher_arvore():
    print("Escolha a estrutura:")
    print("1) Árvore AVL")
    print("2) Árvore Rubro-Negra")
    while True:
        op = input("Opcao: ").strip()
        if op == "1":
            return AVLTree()
        if op == "2":
            return RBTree()
        print("Opcao invalida.")


def main():
    arvore = escolher_arvore()
    while True:
        print()
        print(f"[{arvore.name}]")
        print("1) Inserir")
        print("2) Remover")
        print("3) Buscar")
        print("4) Percurso em ordem")
        print("5) Imprimir arvore")
        print("0) Sair")
        op = input("Opção: ").strip()

        if op == "1":
            k = ler_inteiro("ID: ")
            if k is not None:
                if arvore.insert(k):
                    print(f"{k} inserido.")
                else:
                    print(f"{k} já existe. Inserção ignorada.")
        elif op == "2":
            k = ler_inteiro("ID: ")
            if k is not None:
                if arvore.remove(k):
                    print(f"{k} removido.")
                else:
                    print(f"{k} não encontrado.")
        elif op == "3":
            k = ler_inteiro("ID: ")
            if k is not None:
                print(f"{k} encontrado." if arvore.search(k) else f"{k} não encontrado.")
        elif op == "4":
            itens = arvore.inorder()
            print(itens if itens else "Árvore vazia.")
        elif op == "5":
            if isinstance(arvore, RBTree):
                print(arvore.tree_str(use_ansi=True)) #a IA me mostrou esse ansi que bota cor no terminal e achei legal
            else:
                print(arvore.tree_str())
        elif op == "0":
            break
        else:
            print("Opção invalida.")


if __name__ == "__main__":
    main()