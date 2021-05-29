
def shop(x,y):
    #print          (" === Produto     ====+=$=+====    Preço ===")
    from time import sleep
    Listadict = [[x,y]]

    separador = " "
    title_len = len(" === Produto     ====+=$=+====    Preço ===")
    

    for item in Listadict:

        Letras = len(item[0])
        print(f"{separador *5}{item[0]} {(title_len-16-Letras) * separador} R${item[1]}");sleep(0.9)


Pessoa = {
    'Nome':'Samuel',
    'Sobrenome':'Garrido',
    'Age':19
}



print          (" === Produto     ====+=$=+====    Preço ===")
for x, y in Pessoa.items():
    shop(x,y)