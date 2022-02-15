# Grupo Toppo - 1TDSF
# Artaxerxes Antônio 	RM86180
# Carla Hilst 	        RM84998
# Fernanda Ribeiro 	    RM85800
# Leandro Guidon 	    RM85756
# Lucas Godoy 	        RM85216
#
# Erros:
# Relatório:
# - Primeiro são exibidas todas as vendas de todos os vendedores e só depois são exibidas
# as relações de vendas totais, salário e comissão para cada vendedor.
# - O relatório é exibido duplicado.

cod_vend = []
nm_vend = []

cod_prod = []
desc_prod = []
vl_prod = []

cvend_vend = []
cprod_vend = []
qprod_vend = []

salario = 1585
acrescimo = 0.05


def cadastrar_vendedores():
    cont = 1
    while len(cod_vend) < 5:
        cod_vendedor = int(input("Digite o código do vendedor: "))
        if cod_vendedor <= 0:
            print("O código deve ser maior do que 0. Código não registrado.")
        else:
            if cod_vendedor not in cod_vend:
                nome = input("Digite o nome do vendedor: ")
                cod_vend.append(cod_vendedor)
                nm_vend.append(nome)
                cont += 1
                print("Falta(m) {} vendedor(es).".format(6 - cont))
            else:
                print("Código de vendedor já inserido.")


def cadastrar_produtos():
    cont_prod = 1
    while len(cod_prod) < 10:
        codigo_produto = int(input("Digite o código do produto: "))
        if codigo_produto <= 0:
            print("O código deve ser maior do que 0. Código não registrado.")
        else:
            if codigo_produto not in cod_prod:
                descricao = input("Digite a descrição do produto: ")
                valor = float(input("Digite o valor unitário do produto: R$"))
                cod_prod.append(codigo_produto)
                desc_prod.append(descricao)
                vl_prod.append(valor)
                print("Falta(m) {} produto(s).".format(10 - cont_prod))
                cont_prod += 1
            else:
                print("Código de produto já inserido.")


def vender_produtos():

    if len(cod_vend) == 0 or len(cod_prod) == 0:
        print("Opção inválida. Cadastre os vendedores e os produtos antes de acessá-la.")
    else:
        codigo_produto = int(input("Digite o código do produto: "))

        if codigo_produto in cod_prod:
            codigo_vendedor = int(input("Digite o código do vendedor: "))

            if codigo_vendedor in cod_vend:
                qtde_vendida = int(input("Digite a quantidade vendida: "))

                if qtde_vendida > 0:
                    if codigo_vendedor in cvend_vend:
                        if codigo_produto in cprod_vend:
                            if cvend_vend[cvend_vend.index(codigo_vendedor)] == cvend_vend[cprod_vend.index(codigo_produto)]:
                                qprod_vend[cprod_vend.index(codigo_produto)] += qtde_vendida
                            else:
                                cvend_vend.append(codigo_vendedor)
                                cprod_vend.append(codigo_produto)
                                qprod_vend.append(qtde_vendida)
                        else:
                            cvend_vend.append(codigo_vendedor)
                            cprod_vend.append(codigo_produto)
                            qprod_vend.append(qtde_vendida)
                    else:
                        cvend_vend.append(codigo_vendedor)
                        cprod_vend.append(codigo_produto)
                        qprod_vend.append(qtde_vendida)
                else:
                    print("A quantidade deve ser maior do que 0.")
            else:
                print("Vendedor não registrado.")
        else:
            print("Produto não registrado.")


def listar_produtos():
    if len(cvend_vend) == 0:
        print("Nenhum produto foi vendido.")
    else:
        for j in range(len(cvend_vend)-1, 0, -1):
            for i in range(j):
                if cvend_vend[i] > cvend_vend[i + 1]:
                    aux = cvend_vend[i]
                    cvend_vend[i] = cvend_vend[i + 1]
                    cvend_vend[i + 1] = aux

                    aux_prod = cprod_vend[i]
                    cprod_vend[i] = cprod_vend[i + 1]
                    cprod_vend[i+1] = aux_prod

                    aux_quant = qprod_vend[i]
                    qprod_vend[i] = qprod_vend[i + 1]
                    qprod_vend[i+1] = aux_quant

        prod_vend1 = []
        prod_vend2 = []
        prod_vend3 = []
        prod_vend4 = []
        prod_vend5 = []

        q1 = []
        q2 = []
        q3 = []
        q4 = []
        q5 = []

        for x in range(len(cvend_vend)):
            if cvend_vend[x] == cod_vend[0]:
                prod_vend1.append(cprod_vend[x])
                q1.append(qprod_vend[x])
            elif cvend_vend[x] == cod_vend[1]:
                prod_vend2.append(cprod_vend[x])
                q2.append(qprod_vend[x])
            elif cvend_vend[x] == cod_vend[2]:
                prod_vend3.append(cprod_vend[x])
                q3.append(qprod_vend[x])
            elif cvend_vend[x] == cod_vend[3]:
                prod_vend4.append(cprod_vend[x])
                q4.append(qprod_vend[x])
            elif cvend_vend[x] == cod_vend[4]:
                prod_vend5.append(cprod_vend[x])
                q5.append(qprod_vend[x])

        for j in range(len(prod_vend1)-1, 0, -1):
            for i in range(j):
                if prod_vend1[i] > prod_vend1[i + 1]:
                    aux = prod_vend1[i]
                    prod_vend1[i] = prod_vend1[i + 1]
                    prod_vend1[i + 1] = aux

                    aux_qt = q1[i]
                    q1[i] = q1[i+1]
                    q1[i+1] = aux_qt

        for j in range(len(prod_vend2)-1, 0, -1):
            for i in range(j):
                if prod_vend2[i] > prod_vend2[i + 1]:
                    aux = prod_vend2[i]
                    prod_vend2[i] = prod_vend2[i + 1]
                    prod_vend2[i + 1] = aux

                    aux_qt = q2[1]
                    q2[1] = q2[i+1]
                    q2[i+1] = aux_qt

        for j in range(len(prod_vend3)-1, 0, -1):
            for i in range(j):
                if prod_vend3[i] > prod_vend3[i + 1]:
                    aux = prod_vend3[i]
                    prod_vend3[i] = prod_vend3[i + 1]
                    prod_vend3[i + 1] = aux

                    aux_qt = q3[1]
                    q3[1] = q3[i+1]
                    q3[i+1] = aux_qt

        for j in range(len(prod_vend4)-1, 0, -1):
            for i in range(j):
                if prod_vend4[i] > prod_vend4[i + 1]:
                    aux = prod_vend4[i]
                    prod_vend4[i] = prod_vend4[i + 1]
                    prod_vend4[i + 1] = aux

                    aux_qt = q4[1]
                    q4[1] = q4[i+1]
                    q4[i+1] = aux_qt

        for j in range(len(prod_vend5)-1, 0, -1):
            for i in range(j):
                if prod_vend5[i] > prod_vend5[i + 1]:
                    aux = prod_vend5[i]
                    prod_vend5[i] = prod_vend5[i + 1]
                    prod_vend5[i + 1] = aux

                    aux_qt = q5[1]
                    q5[1] = q5[i+1]
                    q5[i+1] = aux_qt

        for i in range(len(cvend_vend)):

            index_nome = cod_vend.index(int(cvend_vend[i]))
            nome = nm_vend[index_nome]
            print("Vendedor:", cvend_vend[i], " - ", nome)

            if cvend_vend[i] == cod_vend[0]:
                for p in range(len(prod_vend1)):
                    print("Código do Produto: ", int(prod_vend1[p]))
                    index_desc = cod_prod.index(int(prod_vend1[p]))
                    descricao = desc_prod[index_desc]
                    print("Descrição do Produto: ", descricao)
                    print("Quantidade Vendida: ", int(q1[p]))

                    index_prec = cod_prod.index(int(prod_vend1[p]))
                    preco = vl_prod[index_prec]
                    print("Valor Unitário: ", preco)
                    print("Valor Total: ", preco * int(q1[p]))
                    print()

            elif cvend_vend[i] == cod_vend[1]:
                for p in range(len(prod_vend2)):
                    print("Código do Produto: ", int(prod_vend2[p]))

                    index_desc = cod_prod.index(int(prod_vend2[p]))
                    descricao = desc_prod[index_desc]
                    print("Descrição do Produto: ", descricao)
                    print("Quantidade Vendida: ", int(q2[p]))

                    index_prec = cod_prod.index(int(prod_vend2[p]))
                    preco = vl_prod[index_prec]
                    print("Valor Unitário: ", preco)
                    print("Valor Total: ", preco * int(q2[p]))
                    print()

            elif cvend_vend[i] == cod_vend[2]:
                for p in range(len(prod_vend3)):
                    print("Código do Produto: ", int(prod_vend3[p]))
                    index_desc = cod_prod.index(int(prod_vend3[p]))
                    descricao = desc_prod[index_desc]
                    print("Descrição do Produto: ", descricao)
                    print("Quantidade Vendida: ", int(q3[p]))

                    index_prec = cod_prod.index(int(prod_vend3[p]))
                    preco = vl_prod[index_prec]
                    print("Valor Unitário: ", preco)
                    print("Valor Total: ", preco * int(q3[p]))
                    print()

            elif cvend_vend[i] == cod_vend[3]:
                for p in range(len(prod_vend4)):
                    print("Código do Produto: ", int(prod_vend4[p]))
                    index_desc = cod_prod.index(int(prod_vend4[p]))
                    descricao = desc_prod[index_desc]
                    print("Descrição do Produto: ", descricao)
                    print("Quantidade Vendida: ", int(q4[p]))

                    index_prec = cod_prod.index(int(prod_vend4[p]))
                    preco = vl_prod[index_prec]
                    print("Valor Unitário: ", preco)
                    print("Valor Total: ", preco * int(q4[p]))
                    print()

            elif cvend_vend[i] == cod_vend[4]:
                for p in range(len(prod_vend5)):
                    print("Código do Produto: ", int(prod_vend5[p]))
                    index_desc = cod_prod.index(int(prod_vend5[p]))
                    descricao = desc_prod[index_desc]
                    print("Descrição do Produto: ", descricao)
                    print("Quantidade Vendida: ", int(q5[p]))

                    index_prec = cod_prod.index(int(prod_vend5[p]))
                    preco = vl_prod[index_prec]
                    print("Valor Unitário: ", preco)
                    print("Valor Total: ", preco * int(q5[p]))
                    print()

        for i in range(len(cvend_vend)):
            index_nome = cod_vend.index(int(cvend_vend[i]))
            nome = nm_vend[index_nome]
            if cvend_vend[i] == cod_vend[0]:
                total1 = []
                for n in range(len(prod_vend1)):
                    total = prod_vend1[n] * q1[n]
                    total1.append(total)
                print("Valor Total das Vendas - ", nome, ": ", sum(total1))
                print("Valor Total da Comissão: ", sum(total1) * acrescimo)
                print("Salário do mês (fixo + comissão): ", salario + (sum(total1) * acrescimo))

            elif cvend_vend[i] == cod_vend[1]:
                total2 = []
                for n in range(len(prod_vend2)):
                    total = prod_vend2[n] * q2[n]
                    total2.append(total)
                print("Valor Total das Vendas - ", nome, ": ", sum(total2))
                print("Valor Total da Comissão: ", sum(total2) * acrescimo)
                print("Salário do mês (fixo + comissão): ", salario + (sum(total2) * acrescimo))

            elif cvend_vend[i] == cod_vend[2]:
                total3 = []
                for n in range(len(prod_vend3)):
                    total = prod_vend3[n] * q3[n]
                    total3.append(total)
                print("Valor Total das Vendas - ", nome, ": ", sum(total3))
                print("Valor Total da Comissão: ", sum(total3) * acrescimo)
                print("Salário do mês (fixo + comissão): ", salario + (sum(total3)  * acrescimo))

            elif cvend_vend[i] == cod_vend[3]:
                total4 = []
                for n in range(len(prod_vend4)):
                    total = prod_vend4[n] * q4[n]
                    total4.append(total)
                print("Valor Total das Vendas - ", nome, ": ", sum(total4))
                print("Valor Total da Comissão: ", sum(total4) * acrescimo)
                print("Salário do mês (fixo + comissão): ", salario + (sum(total4) * acrescimo))

            elif cvend_vend[i] == cod_vend[4]:
                total5 = []
                for n in range(len(prod_vend5)):
                    total = prod_vend5[n] * q5[n]
                    total5.append(total)
                print("Valor Total das Vendas - ", nome, ": ", sum(total5))
                print("Valor Total da Comissão: ", sum(total5) * acrescimo)
                print("Salário do mês (fixo + comissão): ", salario + (sum(total5) * acrescimo))


while True:
    print("""
    Menu
    [1] Cadastrar vendedores
    [2] Cadastrar produtos
    [3] Vender produtos
    [4] Listar produtos vendidos por vendedor
    [5] Sair
    """)
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        if len(cod_vend) > 0:
            print("Códigos de vendedores já inseridos. Opção inválida.")
        else:
            cadastrar_vendedores()
    elif opcao == 2:
        if len(cod_prod) > 0:
            print("Produtos já cadastrados. Opção inválida.")
        else:
            cadastrar_produtos()
    elif opcao == 3:
        if len(cod_vend) == 0 or len(cod_prod) == 0:
            print("Não há produtos ou vendedores cadastrados. Opção inválida.")
        else:
            vender_produtos()
    elif opcao == 4:
        listar_produtos()
    elif opcao == 5:
        break
    else:
        print("Código inválido.")
