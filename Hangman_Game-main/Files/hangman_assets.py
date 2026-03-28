import os, time
from termcolor import colored
from string import ascii_letters

valid_letters = ascii_letters + "ÁÉÍÓÚ' 'ÃÕÇ" + "áéíóú' 'ãõç"
valid_letters_try_letter = ascii_letters + "Ç"

players = []
wordtips = []

letter_attempts = []

write_players = colored("INFORME O NOME DOS PARTICIPANTES:\nDICA: OS NOMES NÃO PODEM CONTER NÚMEROS!", "green")
write_wordtips = colored("INFORME A PALAVRA CHAVE + 3 DICAS:\nDICA: A PALAVRA CHAVE E AS DICAS NÃO PODEM CONTER NÚMEROS!", "green")

def cleanScreen():
    os.system("cls")

def timeWait(seconds):
    time.sleep(seconds)

def writeScreen(text):
    print(text)

def playersNames():
    cleanScreen()  
    while True:
        writeScreen(write_players) 
        try:
            challenger = input("Desafiante: ").title()
            cleanScreen()

            if all(c in valid_letters for c in challenger) and len(challenger) > 2:
                players.append(challenger)
                while True:
                    writeScreen(f'{write_players}\nDesafiante: {challenger}')
                    try:
                        competitor = input("Competidor: ").title()
                        cleanScreen()

                        if all(c in valid_letters for c in competitor) and len(competitor) > 2:
                            players.append(competitor)
                            break     
                    except ValueError:
                        writeScreen(ValueError)
                break  
        except ValueError:
            writeScreen(ValueError)

def wordTips():
    while True:
        writeScreen(write_wordtips)                 
        try:
            word = input("Palavra Chave: ").upper()
            cleanScreen()
            
            if all(c in valid_letters for c in word) and len(word) > 2: 
                wordtips.append(word)         
                while True:
                    writeScreen(f'{write_wordtips}\nPalavra Chave: {word}')                            
                    try:
                        tip1 = input("Dica 1: ").upper()
                        cleanScreen()
                        
                        if all(c in valid_letters for c in tip1) and len(tip1) > 1:                           
                            wordtips.append(tip1)
                            while True:
                                writeScreen(f'{write_wordtips}\nPalavra Chave: {word}\nDica 1: {tip1}')                                                  
                                try:
                                    tip2 = input("Dica 2: ").upper()
                                    cleanScreen()
                                    
                                    if all(c in valid_letters for c in tip2) and len(tip2) > 1:
                                        wordtips.append(tip2)
                                        while True:
                                            writeScreen(f'{write_wordtips}\nPalavra Chave: {word}\nDica 1: {tip1}\nDica 2: {tip2}')                          
                                            try:
                                                tip3 = input("Dica 3: ").upper()
                                                cleanScreen()
                                                
                                                if all(c in valid_letters for c in tip3) and len(tip3) > 1:     
                                                    wordtips.append(tip3)
                                                    break
                                            except ValueError:
                                                writeScreen(ValueError)                         
                                        break  
                                except ValueError:
                                    writeScreen(ValueError) 
                            break 
                    except ValueError:
                        writeScreen(ValueError)    
                break                 
        except ValueError:
            writeScreen(ValueError)

def wordParameters(attempts):
    writeScreen(f"Número de Letras: {letter_count}\nErros: {attempts}\n{''.join(hidden_word)}\nChutes: {' '.join(letter_attempts)}")

def history(attempts):
    challenger_win = (f'Palavra: {wordtips[0]} - Vencedor: Desafiante {players[0]}, Perdedor: Competidor {players[1]}\n')
    competitor_win = (f'Palavra: {wordtips[0]} - Vencedor: Competidor {players[1]}, Perdedor: Desafiante {players[0]}\n')
    competitor_give_up = (f'Palavra: {wordtips[0]} - Vencedor: Desafiante {players[0]}, Perdedor: Competidor {players[1]}\n')

    if attempts == 6:
        file = open("historico_partidas.txt", "a")
        file.write(challenger_win)
        file.close()
        
    elif ''.join(hidden_word) == wordtips[0]:
        file = open("historico_partidas.txt", "a")
        file.write(competitor_win)
        file.close()

    else:
        file = open("historico_partidas.txt", "a")
        file.write(competitor_give_up)
        file.close()

def playAgain():
    file = open("historico_partidas.txt", "r")
    lines = file.readlines()
    file.close()

    writeScreen(f'\nHistórico de Partidas: {len(lines)}')
    while True:
        writeScreen("\nSelecione:\n(1) - Jogar Novamente\n(2) - Sair")
        restart_option = input("Opção: ")
        try:

            if restart_option == "1":
                players.clear()
                wordtips.clear()
                letter_attempts.clear()
                playersNames()
                wordTips()
                infoWord()
                options()

            elif restart_option == "2":
                cleanScreen()
                writeScreen(f"{'#' *28}\n{'#' * 4} OBRIGADO POR JOGAR {'#' * 4}\n{'#' * 28}")
                exit()
                
            else:
                cleanScreen()
                writeScreen(f'\nHistórico de Partidas: {len(lines)}\n')
                writeScreen("OPÇÃO INVÁLIDA!")
        except ValueError:
            writeScreen(ValueError)

def endGame(attempts, used_tips):
    if attempts == 6:
        cleanScreen()
        writeScreen(colored(f'{players[0]} ganhou!\nA Palavra era: {wordtips[0]}\nErros: {attempts}\nDicas utilizadas: {used_tips - 1}', "green"))
        history(attempts)
        playAgain()

    elif ''.join(hidden_word) == wordtips[0]:
        cleanScreen()
        writeScreen(colored(f'{players[1]} ganhou!\nA Palavra era: {wordtips[0]}\nErros: {attempts}\nDicas utilizadas: {used_tips - 1}', "green"))
        history(attempts)
        playAgain()

def infoWord():
    global hidden_word, letter_count

    hidden_word = ""
    for letter in wordtips[0]:
        if letter == " ":
            hidden_word = hidden_word + " "
        else:
            hidden_word = hidden_word + "*"
    hidden_word = list(hidden_word)

    letter_count = len(wordtips[0]) - wordtips[0].count(" ")
    cleanScreen()

def option1(attempts, used_tips):
    while True:
        try:
            wordParameters(attempts)
            try_letter = input("Informe uma Letra: ").upper()
            cleanScreen()

            if all(c in valid_letters_try_letter for c in try_letter) and len(try_letter) != ' ' and len(try_letter) < 2 and try_letter not in letter_attempts:
                letter_attempts.append(try_letter)
                
                if try_letter in wordtips[0]:
                    for i in range(len(wordtips[0])):
                        if try_letter == wordtips[0][i]:
                            hidden_word[i] = try_letter
                    break
                else:
                    attempts += 1
                    break

            elif try_letter == wordtips[0]:
                cleanScreen()
                writeScreen(colored(f'{players[1]} ganhou!\nA Palavra era: {wordtips[0]}\nErros: {attempts}\nDicas utilizadas: {used_tips - 1}', "green"))
                history(attempts)
                playAgain()
        except ValueError:
            writeScreen(ValueError)
            
    return attempts

def option2(used_tips, attempts):
    writeScreen(colored(f'Dica: {wordtips[used_tips]}', "green"))

    return option1(attempts, used_tips)

def options():
    attempts = 0
    used_tips = 1

    while True:
        endGame(attempts, used_tips)

        if used_tips == 4:
            writeScreen(colored("VOCÊ NÃO POSSUI MAIS DICAS DISPONÍVEIS!", "red"))
            wordParameters(attempts)
            writeScreen("\nSELECIONE:\n(1) - Jogar\n(3) - Desistir")
        
        else:
            writeScreen(colored("DICA: VOCÊ POSSUI SOMENTE 3 DICAS!", "green"))
            wordParameters(attempts)
            writeScreen("\nSELECIONE:\n(1) - Jogar\n(2) - Solicitar Dica\n(3) - Desistir")
        try:
            option = input("Opção: ")
            cleanScreen()
            
            if option == "1":
                attempts = option1(attempts, used_tips)
            
            elif option == "2" and used_tips < 4:
                attempts = option2(used_tips, attempts)
                used_tips += 1

            elif option == "3":
                cleanScreen()
                writeScreen(colored(f'{players[1]} desistiu!\nA Palavra era: {wordtips[0]}', "red"))
                history(attempts)
                playAgain()
        except ValueError:
            writeScreen(ValueError)
