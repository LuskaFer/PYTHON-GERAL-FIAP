from _collections import deque

def menu():
    print("1 - Imprimir nova senha")
    print("2 - Imprimir nova senha(Prioridade)")
    print("3 - Relatório - Imprimir fila de atendimento")
    print("4 - Atender paciente")
    print("5 - Sair")

def gerarSenha():
    global i
    i += 1
    return i

def inserir(opcao):
    global i
    global fila
    gerarSenha()
    if opcao == 1:
        fila.append(i)
        print("Senha registrada com sucesso")
    elif opcao == 2:
        fila.appendleft(i)
        print("Senha preferencial registrada com sucesso")

def atenderPaciente():
    global fila
    fila.popleft()

def relatorio():
    global fila
    print("Ordem de atendimento dos pacientes: ")
    for i in fila:
        print(i)

i: int = 0
fila = deque([])
continua = 0

print("Bem vindo. Por favor escolha uma das opções abaixo: ")
while continua == 0:
    menu()
    opcao = int(input("Digite o número da opção desejada: "))
    if opcao == 1 or opcao == 2:
        inserir(opcao)

    elif opcao == 3:
        relatorio()

    elif opcao == 4:
        atenderPaciente()

    elif opcao == 5:
        continua = 1

    else:
        print("Opção inválida. Tente digitar apenas o número de uma das opções")