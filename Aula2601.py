# Grupo Toppo
# Artaxerxes Antônio 	RM86180
# Carla Hilst  	        RM84998
# Fernanda Ribeiro 	    RM85800
# Leandro Guidon 	    RM85756
# Lucas Godoy 	        RM85216

from collections import deque

senha = 0

senhas = deque([])
senhas_prioritarias = deque([])

fila = senhas_prioritarias + senhas

while True:
    print("""
    Menu de opções:
    1 – Imprimir nova senha
    2 – Imprimir nova senha (prioridade)
    3 – Relatório: Mostrar fila de atendimento
    4 – Atender paciente
    5 - Sair
    """)
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        senha += 1
        senhas.append(senha)
        print("Sua senha é ", senha)
    elif opcao == 2:
        senha += 1
        print("Sua senha é ", senha)
        senhas_prioritarias.append(senha)
    elif opcao == 3:
        fila = senhas_prioritarias + senhas
        if fila:
            print("Fila atual: ")
            for i in fila:
                print(i)
        else:
            print("Não há pacientes na fila.")
    elif opcao == 4:
        if senhas or senhas_prioritarias:
            print("Atendendo senha ", fila[0])
            if fila[0] in senhas:
                senhas.remove(fila[0])
            else:
                senhas_prioritarias.remove(fila[0])
            fila.popleft()
        else:
            print("Não há pacientes a serem atendidos.")
    elif opcao == 5:
        break
    else:
        print("Opção inválida.")