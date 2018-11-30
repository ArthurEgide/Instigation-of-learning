def carregar():
    with open('personagens.txt') as txt:
        ler = txt.readline()
        cont = 1
        while ler != '':
            print(cont,'-',ler, end = '')
            ler = txt.readline()
            cont += 1
        choice = int(input('\n-- Escolha seu personagem --\n\n\n'))
        cont = 0
        txt.seek(0)
        while cont < choice:
            ler = txt.readline()
            cont += 1

        print('\n-- Escolhido --\n\n',ler)
        return ler

