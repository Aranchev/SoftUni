# https://judge.softuni.org/Contests/Compete/Index/2417#2
n = int(input())

for i in range(0, n + 1 , 2): #! първото - долна граница; второто - горна граница; третото - през колко 
    print(2 ** i)

#! Когато input-неш 10 става следното: range става (0, 11, 2), което означава, че range e ot 0 до 10 през 2.
#! 'print(2 ** i)' прави така, щото когато въведеш input 10 степента на 2 се вдига с 2, докато стигне до 10:
#! 2 ** 0 = 1; 2 ** 2 = 4; 2 ** 4 = 16; 2 ** 6 = 64...