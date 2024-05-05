# 3) Batalha de Pomekons

import os

os.system("cls")

vezes = int(input("Informe o número de instâncias: "))
golpe = 0
golpe1 = 0

for i in range(vezes):
    bonus = int(input("Bônus: ")) 
    ataque_dabriel, defesa_dabriel, level_dabriel = map(int, input("Dabriel: ").split())
    ataque_guarte, defesa_guarte, level_guarte = map(int, input("Guarte: ").split())

    if level_dabriel % 2 == 0:
        golpe = ((ataque_dabriel + defesa_dabriel)/ 2) + bonus
 
    else:
        golpe = ((ataque_dabriel + defesa_dabriel) / 2)
   
    if level_guarte % 2 == 0:
        golpe1 = ((ataque_guarte + defesa_guarte) / 2) + bonus 

    else:
        golpe1 = ((ataque_guarte + defesa_guarte) / 2) 
 
    if golpe < golpe1:
        print("Guarte")
 
    elif golpe > golpe1:
        print("Dabriel")
 
    elif golpe1 == golpe:
        print("Empate")
