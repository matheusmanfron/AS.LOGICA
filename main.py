from dataclasses import dataclass

diaAtual = 0

@dataclass
class Livro:
    id: int
    titulo: str
    autor: str
    disponivel: bool = True 

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
    livros.append(Livro(id_livro, titulo, autor, True)) 
    print("Livro cadastrado com sucesso!")

def gerenciar_usuario():
    id_usuario = len(usuarios) + 1
    nome = input("Nome do usuário: ")
    usuarios.append(Usuario(id_usuario, nome))
    print("Usuário cadastrado com sucesso!")

def realizar_emprestimo():
    global diaAtual 
    id_usuario = int(input("ID do usuário: "))
    id_livro = int(input("ID do livro: "))
    livro_encontrado = buscar_livro(id_livro) 

    if livro_encontrado and livro_encontrado.disponivel:
        dias_para_devolver = 7
        emprestimos.append(Emprestimo(id_usuario, id_livro, diaAtual, diaAtual + dias_para_devolver))
        livro_encontrado.disponivel = False
        print("Empréstimo realizado com sucesso!")
    else:
        print("Livro indisponível ou não encontrado.")

def devolucao():
    global diaAtual
    id_livro = int(input("ID do livro a ser devolvido: "))

    for emp in emprestimos:
        if emp.id_livro == id_livro and emp.dia_devolucao == -1:
            emp.dia_devolucao = diaAtual
            livro_encontrado = buscar_livro(id_livro)
            if livro_encontrado:
                livro_encontrado.disponivel = True
            dias_atraso = max(0, diaAtual - emp.dia_previsto)
            multa = dias_atraso * 1.5
            print(f"Livro devolvido. Dias de atraso: {dias_atraso}. Multa: R${multa:.2f}")
            return
    print("Empréstimo não encontrado ou livro já devolvido.")

def buscar_livro(id_livro):
    for livro_obj in livros: 
        if livro_obj.id == id_livro:
            return livro_obj
    return None

def gerenciar_tempo():
    global diaAtual
    dias = int(input("Avançar quantos dias? "))
    diaAtual += dias
    print(f"Dia atual: {diaAtual}")

def listar_livros():
    if not livros:
        print("Não há livros cadastrados.")
        return
    for livro_obj in livros:
        status = "Disponível" if livro_obj.disponivel else "Emprestado"
        print(f"ID: {livro_obj.id} | Título: {livro_obj.titulo} | Autor: {livro_obj.autor} | {status}")

def relatorio():
    print("\n===== RELATÓRIO GERAL =====")
    total_livros = len(livros)
    emprestados = sum(not livro_obj.disponivel for livro_obj in livros)
    disponiveis = total_livros - emprestados

    total_usuarios = len(usuarios)
    total_emprestimos = len(emprestimos)
    emprestimos_ativos = sum(emp.dia_devolucao == -1 for emp in emprestimos)
    emprestimos_atrasados = sum(
        emp.dia_devolucao == -1 and diaAtual > emp.dia_previsto
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
        print("Dia atual do sistema:", diaAtual)
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
            print("Saindo do sistema")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
