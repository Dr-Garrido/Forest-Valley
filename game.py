#########################################
#       Criador:   Каппа                @
#       Data:      21/04/2021           @
#       Versão:    0.0.5                @
#########################################
#\033[34;35m

#Importação das bibliotecas
from posix import sched_param
from time import sleep


#Atualização de variáveis.
import help,shop,os

print("Olá, é a primeira vez que vejo você aqui. Parece que o destino nos uniu.");sleep(0.5)
nome = input("Já que estamos por aqui. Qual é o seu nome? ");sleep(1)
print("Parabéns você será o guerriro" + nome + "de agora em diante você terá o cargo de guerreiro erga sua espada e explore o mundo!")
print("vamor iniciar as explicações normais.");sleep(1)
print("Esse é o seu terminal, conhecido como CCW (comand control world)");sleep(2)
print("Você terá que digitar comandos especiais que serão explicados no decorrer do game, sem mais delongas. Digite help")

while True:
    ordem = input("Digite um comando:").upper().lstrip()
    if ordem == "HELP":
        help.help()
        print("Fim do comando help")
    elif ordem == "EXIT":
        print("Adeus, talvez nos encontraremos novamente, ou não.")
        break
    elif ordem == "SHOP":
        print("Bem-Vindo a loja o que desejas comprar?");sleep(2)
        shop.shop()

    else:
        os.system("cls")
        print("Comando inválido tente novamente, você digitou -> " + ordem)