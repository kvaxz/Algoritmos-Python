import random
import os
import time

contador = 1

while True:

    print("""  
========== QUALQUER TECLA E APERTE ENTER =============
============== PARA SAIR INSIRA "0"  =================
    """)
    acao = input()

    if acao == "0":
        print("LOGO AGORA QUE EU IA SOLTAR A CARTA!")
        break
    else:
        os.system('cls')
        slot = ['🍒', '🍋', '🍊', '🍇', '🔔', '⭐', '🍀', '💎', '🪙', '🃏']
        random.shuffle(slot)

        slot1=random.choice(slot)
        slot2=random.choice(slot)
        slot3=random.choice(slot)

        print("\n\n\n|||================|||")
        print(f"|  {slot1}  |  {slot2}  |  {slot3}  |")
        print("|||================|||\n\n")
        contador+=1

        if slot1 == slot2 == slot3:
            print("PARABÉNS KRAIO, FINALMENTE VOCE GANHOU FI")
            print(f"PRECISOU SÓ DE {contador} TENTATIVAS\n\n\n")
            break