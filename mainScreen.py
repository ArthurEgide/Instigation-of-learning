import main
import save

def newGame():
    print('Em breve :)')

def loadGame():
    save.carregar()

def options():
    print('Em breve :)')

def credit():
    print('Em breve :)')

print('-- Bem vindo ao RPG em "textes" --\n')

opt = ['Iniciar novo jogo', 'Carregar Jogo', 'Opcoes', 'Detalhes'],['newGame', 'loadGame', 'optionsm', 'credits']


for ind,i in enumerate(opt[0]):
    print('-'+ str(ind) +'-', i, '--- ')

choice = main.choice()

if opt[1][choice] == opt[1][0]:
    newGame()
elif opt[1][choice] == opt[1][1]:
    loadGame()
elif opt[1][choice] == opt[1][2]:
    options()
elif opt[1][choice] == opt[1][3]:
    credit()
