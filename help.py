def help():
    from os import system
    from time import sleep
    system("cls")
    op = 1; c = 0
    while op != 0:
        if c < 1:
            print("O que você deseja saber\n");sleep(0.6)
            print("1 - Movimentos");sleep(0.5)
            print("2 - Checar itens");sleep(0.5)
            print("3 - Inventário");sleep(0.5)
            print("0 - sair\n");sleep(0.5);c = c + 1

        op = int(input("Opção: "))

        if op == 0:
            break
        if op == 1:
            print("\nMovimentos básicos.\n");sleep(2)
            print("---> Para andar você precisa usar os comandos walk\n")
            input("Ok? pressione qualquer tecla.")

        elif op == 2:
            print("\n---> Para checar itens use o comando check, com ele você checar a área próxima.\n");sleep(2)
            input("Ok? pressione qualquer tecla.")

        elif op == 3:
            print("\n---> Para ver o inventário utilize bag.");sleep(0.5)
            print("---> Para usar um item após o comando bag escreva o número do item utilizável.\n");sleep(0.5)
            input("Ok? pressione qualquer tecla.")
        else:
            print("Escolha uma das opções, a opção " + str(op) + " não existe.");sleep(2)