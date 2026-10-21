print("=-"*45)
print("Bem-vindo ao programa para saber o quanto de lucro você tem nas vendas dos seus produtos")
print("Desenvolvido por: Diego Henrique Brito de Almeida")
print("=-"*45)
opcao = 0
while opcao !=2:
    print("Opções disponíveis: \n 1) Analise o produto \n 2) Sair")
    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        preco_da_venda = float(input("Digite por quanto você vendeu/está pensando em vender R$: "))
        custo_total = float(input("Digite o custo total (frete, embalagem, imposto) R$: "))
        lucro = preco_da_venda - custo_total 
        margem = (lucro / preco_da_venda) * 100
        print()
        print("A margem do lucro sob a venda do produto é {:.2f} %".format(margem))
        print("=-"*45)

       
    elif opcao == 2:
        print("Obrigado por usar o programa!")
        break

    else:
        print("Opção inválida, tente novamente")
        print()
print("=-"*45)

