import os
os.system("clear")

print("Qual será a forma de passeio?")
print("1 - A pé")
print("2 - De carro")
print("3 - De de bicicleta")

opcao = int(input("Qual a sua opção? "))
if opcao == 1:
    print("Você escolheu a opção 1 - A pé")
elif opcao == 2:
    print("Você escolheu a opção 2 - De carro")
elif opcao == 3:
    print("Você escolheu a opção 3 - De bicicleta")
elif opcao == 4:
    #return opcao anterior
    print() 
else:
    print("Opção inválida!")

print ("fazer um passeio \n Como você quer seguir sua rota?")

print("1 - Rota definida")
print("2 - Rota personalizada")

opcao1 = int(input("Qual a sua opção? "))

if opcao1 == 1:
    print("1 - Rota Manguebeat\n 2 - Rota Artesanato\n 3 - Rota dos Poetas\n 4 - Rota do Carnaval\n 5 - Rota do Praieira\n 6 - Rota da Lama ao Caos")
    sair = input("Sair")
    if sair == "sair":
        print()
        #return opcao anterior

buscar = []

if opcao1 == 2:
    while True:
        concluir = input("Concluir")
        if concluir == "concluir":
            buscando = int(input("Buscar"))
            buscando.append(buscar)
            print("Localização Salva", buscar)
            tirar = input("Tirar localização")
            if tirar == "sim" or "Sim":
                palavra = buscando
                buscando.remove(palavra)
            else:
                print()
        elif concluir == "sair":
            print("saindo")
            #return opcao anterior or BREAK!!! 
        Localização = input("Sua localização")
        if Localização == True:
            print()
            #return opcao anterior (ESSE LOCALIZAÇÃO SERVE COMO GPS DO GOOGLE PARA FACILITAR A LOCALIZAÇÃO ATUAL // SEM FUÇÃO ATUAL)
        cont = input('concluir Seleção?')
        if cont == 'sim':
            print()
            break
        else:
            print('continuando a adicionar...')





        

