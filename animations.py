from time import sleep
#Organizar tudo
def organizar(x,y):
    Listadict = [[x,y]]
    separador = " "
    for item in Listadict:
        Letras = len(item[0])
        print(f"{separador *5}{item[0]} {(28-Letras) * separador} {item[1]}");sleep(0.9) #28