########################################$
#       Criador:   Каппа                $
#       Data:      21/04/2021           X
#       Versão:    0.2.2                $
########################################$

#Importação das bibliotecas
from time import sleep
# 1 = checar
# 2 = pegar
# 3 = utilizável

#Atualização de variáveis.
import help,os
char = "1x1"

bag = {
    'paper':'3'
}

mission1 = {
    'body':False,'body2':False, 'mesa':False,
    'all':False
}
area1x1 = {
    'body':1, 'body2':1, 'mesa':1
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
            for x in area1x1:
                print("Achado -> " + x)
                op = input(f"Deseja checar o {x} ?")
                if op in "sS":
                    del area1x1[x]
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
