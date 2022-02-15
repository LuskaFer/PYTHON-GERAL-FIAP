vendedores = {}
proddesc = {}
prodqtd = {}
prodpreco = {}
vendasporvendedor = {}
j = 0

def cadastrarvend ():
    i = 1
    if vendedores == {}:
        while i <= 2:
            while i != 0:
                codigo = int(input("Digite o código do vendedor(a): "))
                if codigo > 0:
                    vendedor = str(input("Digite o nome do(a) vendedor(a)"))
                    if codigo not in vendedores:
                        vendedores[codigo] = vendedor
                        i += 1
                    else:
                        print("Este vendedor(a) já foi cadastrado. Digite outro vendedor(a): ")
                    break
                else:
                    print("Digite um código maior que 0.")
    else:
        print("Vendedores já cadastrados")

def cadastrarprod ():
    i = 1
    if proddesc == {}:
        while i <= 2:
            while i != 0:
                codigo = int(input("Digite o código do produto: "))
                if codigo >= 0:
                    descricao = str(input("Digite a descrição do produto: "))
                    qtd = int(input("Digite a quantidade em estoque: "))
                    preco = float(input("Digite o preço unitário do produto: "))
                    if descricao not in proddesc and codigo not in proddesc:
                        proddesc[codigo] = descricao
                        prodqtd[codigo] = qtd
                        prodpreco[codigo] = preco
                    else:
                        print("Este produto já foi cadastrado. Digite outro produto: ")
                    i += 1
                    break
                else:
                    print("Digite um código maior que 0.")
    else:
        print("Produtos já cadastrados")

def vender (codvend, codprod, qtd):
    print(codvend)
    print(vendedores)
    print(codprod in proddesc)
    print(codvend in vendedores)
    print(qtd > 0)
    if codvend in vendedores and codprod in proddesc and qtd > 0:
        prodqtd[codprod] -= qtd
        if codvend in vendasporvendedor:
            if codprod in vendasporvendedor[codvend]:
                vendasporvendedor[codvend, ['Quantidade']] += qtd
            else:
                vendasporvendedor[codvend, ['Codigo']] = codprod
                vendasporvendedor[codvend, ['Quantidade']] = qtd
        else:
            vendasporvendedor[codvend] = {'Codigo': codprod, 'Quantidade': qtd}
        return True
    else:
        print("Vendedor ou produto não cadastrado ou quantidade menor ou igual a 0. ")
        return False

def listarprodutos ():
    for i, j in vendasporvendedor.items():
        print("Vendedor: ", i, " - ", vendedores[i],".")
        print("Código do produto:     |Descrição do produto     |Quantidade     |Valor unitário     |Valor total")

        text = (j['Codigo'],"|", proddesc[j['Codigo']], "|",  j['Quantidade'], "|", prodpreco[j['Codigo']], "|", prodpreco[j['Codigo']]*j['Quantidade'])
        print(len(text))
        print(text)


def mostrarmenu ():
    print("1. Cadastrar vendedores")
    print("2. Cadastrar produtos")
    print("3. Vender produtos")
    print("4. Listar produtos vendidos por vendedor")
    print("5. Sair")


print("Bem vindo ao gerenciador da empresa.")
while j == 0:
    mostrarmenu()
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        cadastrarvend()

    elif opcao == 2:
        cadastrarprod()

    elif opcao == 3:
        vendedor = int(input("Digite o código do vendedor(a): "))
        produto = int(input("Digite o código do produto: "))
        qtd = int(input("Digite a quantidade a ser vendida: "))
        if vender(vendedor, produto, qtd):
            print("Venda realizada.")
        else:
            print("Venda não realizada.")

    elif opcao == 4:
        listarprodutos()

    elif opcao == 5:
        break

    else:
        print("Opção inválida.")
