from dataclasses import dataclass
diaAtual = 0

@dataclass
class Livro:
    id: int
    titulo: str
    autor: str
    disponivel: bool

@dataclass
class Usuario:
    id: int
    nome: str

@dataclass
class Emprestimo:
    id_usuario: int
    id_livro: int
    dia_emprestimo: int
    dia_previsto: int
    dia_devolucao: int = -1  

livros = []
usuarios = []
emprestimos = []

def gerenciar_livros():
    id_livro = len(livros) + 1
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    livros.append(livros(id_livro, titulo, autor))
    print("Livro cadastrado com sucesso!")

def gerenciar_usuario():
    id_usuario = len(usuarios) + 1
    nome = input("Nome do usuário: ")
    usuarios.append(Usuario(id_usuario, nome))
    print("Usuário cadastrado com sucesso!")

def realizar_emprestimo():
    global dia_atual
    id_usuario = int(input("ID do usuário: "))
    id_livro = int(input("ID do livro: "))
    Livro = buscar_livro(id_livro)

    if Livro and Livro.disponivel:
        dias_para_devolver = 7  
        emprestimos.append(Emprestimo(id_usuario, id_livro, dia_atual, dia_atual + dias_para_devolver))
        Livro.disponivel = False
        print("Empréstimo realizado com sucesso!")
    else:
        print("Livro indisponível ou não encontrado.")

def devolucao():
    global dia_atual
    id_livro = int(input("ID do livro a ser devolvido: "))

    for emp in emprestimos:
        if emp.id_livro == id_livro and emp.dia_devolucao == -1:
            emp.dia_devolucao = dia_atual
            Livro = buscar_livro(id_livro)
            Livro.disponivel = True
            dias_atraso = max(0, dia_atual - emp.dia_previsto)
            multa = dias_atraso * 1.5  
            print(f"Livro devolvido. Dias de atraso: {dias_atraso}. Multa: R${multa:.2f}")
            return
    print("Empréstimo não encontrado ou livro já devolvido.")

def buscar_livro(id_livro):
    for Livro in livros:
        if Livro.id == id_Livro:
            return livro
    return None

def gerenciar_tempo():
    global dia_atual
    dias = int(input("Avançar quantos dias? "))
    dia_atual += dias
    print(f"Dia atual: {dia_atual}")

def listar_livros():
    for Livro in livros:
        status = "Disponível" if Livro.disponivel else "Emprestado"
        print(f"ID: {Livro.id} | Título: {Livro.titulo} | Autor: {Livro.autor} | {status}")

def relatorio():
    print("\n===== RELATÓRIO GERAL =====")
    total_livros = len(livros)
    emprestados = sum(not Livro.disponivel for Livro in livros)
    disponiveis = total_livros - emprestados

    total_usuarios = len(usuarios)
    total_emprestimos = len(emprestimos)
    emprestimos_ativos = sum(emp.dia_devolucao == -1 for emp in emprestimos)
    emprestimos_atrasados = sum(
        emp.dia_devolucao == -1 and dia_atual > emp.dia_previsto
        for emp in emprestimos
    )

    print(f"Total de livros: {total_livros}")
    print(f" - Disponíveis: {disponiveis}")
    print(f" - Emprestados: {emprestados}")
    print(f"Total de usuários: {total_usuarios}")
    print(f"Total de empréstimos realizados: {total_emprestimos}")
    print(f"Empréstimos em aberto: {emprestimos_ativos}")
    print(f"Empréstimos em atraso: {emprestimos_atrasados}")

def menu():
    while True:
        print("\n==== BIBLIOTECA ====")
        print("Dia atual do sistema:", dia_atual)
        print("1: Cadastrar Livro")
        print("2: Cadastrar Usuário")
        print("3: Emprestar Livro")
        print("4: Devolver Livro")
        print("5: Listar Livros")
        print("6: Avançar Dia")
        print("7: Gerar relatório")
        print("0: Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            gerenciar_livros()
        elif opcao == "2":
            gerenciar_usuario()
        elif opcao == "3":
            realizar_emprestimo()
        elif opcao == "4":
            devolucao()
        elif opcao == "5":
            listar_livros()
        elif opcao == "6":
            gerenciar_tempo()
        elif opcao == "7":
            relatorio()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

