from time import sleep, time
def shop():
    loja1 = [["Informação",1200],["Isqueiro", 250],["Bebida",20]]
    separador = " "
    title_len = len(" === Produto     ====+=$=+====    Preço ===")
    print          (" === Produto     ====+=$=+====    Preço ===")
    for (item) in loja1:
        Letras = len(item[0])
        print(f"{separador *5}{item[0]} {(title_len-16-Letras) * separador} R${item[1]}");sleep(0.9)
    