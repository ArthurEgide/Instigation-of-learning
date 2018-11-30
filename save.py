import main, glob, os

def criar():
    confirma = False
    while not confirma:
        nome = input("Digite um nome pro personagem")
        print("Deseja se chamar '",nome,"'? (0 - Não/1 - Sim)")
        if main.choice() == 1:
            confirma = True
            if nome + ".rpsave" in glob.glob("*.rpsave"):
                print("Já tens um personagem com este nome.")
                confirma = False

    presets = ["Guerreiro", "Assassino", "Mago"], ["Força", "Agilidade", "Inteligencia"], [[5, 3, 2], [2, 5, 3], [2, 3, 5]]
    confirma = False
    while not confirma:
        print("-- Escolha sua classe--\n")
        for i in range(len(presets)):
            print('#['+ str(i) +']#-',presets[0][i],'-#['+ str(i) +']#')



        classe = main.choice()
        for i in range(len(presets)):
            print(presets[1][i],":",presets[2][classe][i])

        print("Deseja mesmo ser um '",presets[0][classe],"'? (0 - Não/1 - Sim)")
        if main.choice() == 1:
            confirma = True

    with open(nome+".rpsave", "w") as sv:
        sv.write("name:" + nome)
        sv.write("\ncls:" + str(presets[0][classe]))
        sv.write("\nstr:" + str(presets[2][classe][0]))
        sv.write("\nagi:" + str(presets[2][classe][1]))
        sv.write("\nint:" + str(presets[2][classe][2]))
        sv.write("\nhp:" + "20")
    print("Personagem criado com sucesso!!!")



def carregar():
    saves = []
    for ind,file in enumerate(glob.glob("*.rpsave")):
        print(ind, '--', file.split(".rpsave")[0])
        saves.append(file)

    if len(saves) == 0:
        print("Não há personagens salvos")
    else:
        choice = main.choice()
        player = open(saves[choice])
        return player

