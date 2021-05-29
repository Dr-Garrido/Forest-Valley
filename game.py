########################################$
#       Criador:   Каппа                $
#       Data:      21/04/2021           X
#       Versão:    0.2.2                $
########################################$

#Importação das bibliotecas
from time import sleep
from animations import organizar
import help , os

# 1 = checar
# 2 = pegar
# 3 = utilizável

#Atualização de variáveis.
char = "1x1"
bag = {
    'paper':1
}
mission1 = {
    'body':False,'body2':False, 'mesa':False,
    'all':False
}
area1x1 = {
    'body':'Canivete', 'body2':'Faca', 'mesa':None
}

while True:
    ordem = input("Digite um comando:").upper().lstrip()
    if ordem == "HELP":
        help.help()
        print("Fim do comando help")

    elif ordem == "EXIT":
        print("Adeus, talvez nos encontraremos novamente, ou não.")
        break

    elif ordem == "LIMPAR":
        os.system("cls")
    






    elif ordem == "CHECK":
        print("Checando área...");sleep(0.9)
        achados = 0
        if char == "1x1":

            print("_____Objeto______====+=@=+====______Item____")
            for x, y in area1x1.items():
                organizar(x,y)
                ###############
                #op = input(f"Deseja checar o {x} (S/N)?")
                #if op in "sS":
                #    elementodeletar = x
                #    del area1x1[elementodeletar]
                #else:
                #    print("ok")
                ###################
                
                achados += 1

            if achados == 0:
                print("Não foi encontrado nada.")






    elif ordem == "BAG":
        print("Os itens da sua mochila são:")
        for x in bag:
            print(x)




    elif ordem == "USE":
        print("Qual item deseja utilizar?")
        item = str(input("Nome do item: "))


    else:
        print("Comando inválido tente novamente, você digitou -> " + ordem)
