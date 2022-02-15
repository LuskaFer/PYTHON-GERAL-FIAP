janela = []
corredor = []
ocupacao = 0

for i in range(24):
    janela.append(ocupacao)
    corredor.append(ocupacao)
while True:
    print("""
    Menu
    1 - Vender passagem
    2 - Cancelar compra
    3 - Mostrar mapa de ocupação
    4 - Sair
    """)
    opcao = int(input("Digite a opção desejada: "))
    if opcao < 1 or opcao > 4:
        print("Opção inválida.")
    elif opcao == 1:
        if sum(janela) == 24 and sum(corredor) == 24:
                print("Ônibus lotado. Opção inválida!")
        else:
            escolha_lado = int(input("Digite 1 para poltrona no corredor e 2 para poltrona na janela: "))
            if escolha_lado != 1 and escolha_lado != 2:
                print("Opção inválida.")
            else:
                escolha_poltrona = int(input("Digite o número da poltrona: "))
                if escolha_poltrona < 0 or escolha_poltrona > 23:
                    print("Opção inválida.")
                elif escolha_lado == 1:
                    if corredor[escolha_poltrona] == 0:
                        corredor[escolha_poltrona] = 1
                        print("Venda realizada com sucesso!")
                    else:
                        print("Poltrona ocupada. Venda não realizada!")
                else:
                    if janela[escolha_poltrona] == 0:
                        janela[escolha_poltrona] = 1
                        print("Venda realizada com sucesso!")
                    else:
                        print("Poltrona ocupada. Venda não realizada!")
    elif opcao == 2:
        if sum(janela) == 0 and sum(corredor) == 0:
            print("Todas as poltronas estão livres. Opção inválida!")
        else:
            cancelamento_lado = int(input("Digite 1 para poltrona no corredor e 2 para poltrona na janela: "))
            if cancelamento_lado != 1 and cancelamento_lado != 2:
                print("Opção inválida.")
            else:
                cancelamento_poltrona = int(input("Digite o número da poltrona: "))
                if cancelamento_poltrona < 0 or cancelamento_poltrona > 23:
                    print("Opção inválida.")
                elif cancelamento_lado == 1:
                    if corredor[cancelamento_poltrona] == 1:
                        print("Compra cancelada com sucesso!")
                        corredor[cancelamento_poltrona] = 0
                    else:
                        print("Poltrona livre. Compra não cancelada!")
                else:
                    if janela[cancelamento_poltrona] == 1:
                        print("Compra cancelada com sucesso!")
                        janela[cancelamento_poltrona] = 0
                    else:
                        print("Poltrona livre. Compra não cancelada!")
    elif opcao == 3:
        print("Corredor")
        for i, val in enumerate(corredor):
            if val == 0:
                print(i, "- Livre")
            else:
                print(i, "- Ocupada")
        print("Janela")
        for i, val in enumerate(janela):
            if val == 0:
                print(i, "- Livre")
            else:
                print(i, "- Ocupada")
    else:
        break
