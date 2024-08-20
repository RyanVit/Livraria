from db import connect, close

def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    isbn = input("Digite o ISBN do livro: ")
    preco = float(input("Digite o preço do livro: "))
    
    conn = connect()
    cur = conn.cursor()
    query = """
    INSERT INTO livros (titulo, autor, isbn, preco)
    VALUES (%s, %s, %s, %s)
    """
    cur.execute(query, (titulo, autor, isbn, preco))
    close(conn)
    print(f"Livro '{titulo}' cadastrado com sucesso.")

def procurar_livros_por_autor():
    autor = input("Digite o nome do autor: ")
    conn = connect()
    cur = conn.cursor()
    query = "SELECT * FROM livros WHERE autor = %s"
    cur.execute(query, (autor,))
    livros = cur.fetchall()
    close(conn)
    
    if livros:
        print("Livros encontrados:")
        for livro in livros:
            print(f"Título: {livro[1]}, Autor: {livro[2]}, ISBN: {livro[3]}, Preço: {livro[4]}")
    else:
        print("Nenhum livro encontrado para esse autor.")

def editar_preco():
    isbn = input("Digite o ISBN do livro que deseja atualizar o preço: ")
    novo_preco = float(input("Digite o novo preço: "))
    
    conn = connect()
    cur = conn.cursor()
    query = "UPDATE livros SET preco = %s WHERE isbn = %s"
    cur.execute(query, (novo_preco, isbn))
    close(conn)
    print(f"Preço do livro com ISBN {isbn} atualizado para {novo_preco}.")

def mostrar_todos_livros():
    conn = connect()
    cur = conn.cursor()
    query = "SELECT * FROM livros"
    cur.execute(query)
    livros = cur.fetchall()
    close(conn)
    
    if livros:
        print("Todos os livros cadastrados:")
        for livro in livros:
            print(f"Título: {livro[1]}, Autor: {livro[2]}, ISBN: {livro[3]}, Preço: {livro[4]}")
    else:
        print("Nenhum livro cadastrado.")

def menu():
    while True:
        print("\nSistema de Cadastro de Livros")
        print("1. Cadastrar Livro")
        print("2. Procurar Livros por Autor")
        print("3. Editar Preço de um Livro")
        print("4. Mostrar Todos os Livros")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            cadastrar_livro()
        elif escolha == '2':
            procurar_livros_por_autor()
        elif escolha == '3':
            editar_preco()
        elif escolha == '4':
            mostrar_todos_livros()
        elif escolha == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

