alunos = []

def adicionar():
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    while True:
        nota = float(input("Nota (0 a 10): "))
        if 0 <= nota <= 10:
            break
        print("Nota inválida.")

    alunos.append({"nome": nome, "idade": idade, "nota": nota})
    print("Aluno cadastrado!")

def listar():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print("Nome:", aluno["nome"])
            print("Idade:", aluno["idade"])
            print("Nota:", aluno["nota"])
            print()

def buscar():
    nome = input("Nome do aluno: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            print("Nome:", aluno["nome"])
            print("Idade:", aluno["idade"])
            print("Nota:", aluno["nota"])
            return

    print("Aluno não encontrado.")

def remover():
    nome = input("Nome do aluno: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            alunos.remove(aluno)
            print("Aluno removido!")
            return

    print("Aluno não encontrado.")

def media():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        soma = 0
        for aluno in alunos:
            soma += aluno["nota"]

        print("Média geral:", round(soma / len(alunos), 2))

while True:
    print("\n--- CADASTRO DE ALUNOS ---")
    print("1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Remover aluno")
    print("5 - Média das notas")
    print("6 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        buscar()
    elif opcao == "4":
        remover()
    elif opcao == "5":
        media()
    elif opcao == "6":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")
