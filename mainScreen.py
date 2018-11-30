import os

def newGame():
    import save
    os.chdir("saves")
    save.criar()


def loadGame():
    import save
    os.chdir("saves")
    save.carregar()
    print('Load')

def options():
    print('Em breve :)')

def credit():
    print('---------')
    print('## Em desenvolvimento ##')
    print("\n\n Por Arthur Egide")

print('-- Bem vindo ao RPG em "textes" --\n')

opt = ['Iniciar novo jogo', 'Carregar Jogo', 'Opcoes', 'Detalhes'],['newGame', 'loadGame', 'options', 'credits']


for ind,i in enumerate(opt[0]):
    print('-'+ str(ind) +'-', i, '--- ')

import main
choice = main.choice()

if opt[1][choice] == opt[1][0]:
    newGame()
elif opt[1][choice] == opt[1][1]:
    loadGame()
elif opt[1][choice] == opt[1][2]:
    options()
elif opt[1][choice] == opt[1][3]:
    credit()