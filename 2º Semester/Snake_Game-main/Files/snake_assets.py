import os, pygame as pg

pg.init()
pg.font.init()
pg.mixer.init()

window = pg.display.set_mode([700, 700])
pg.display.set_caption("Snake Game")

font = pg.font.SysFont("Lucida Console", 30)

background = pg.image.load("background.png")
background_gameOver = pg.image.load("background_gameOver.png")
background_position = (0, 0)

color_white = (255, 255, 255)
color_goldenrod = (218, 165, 32)
color_red = (255, 0, 0)

score = 0

def cleanScreen():
    os.system("cls")

def writeScreen(text):
    print(text)

def userData():
    while True:
        try:
            cleanScreen()
            user = input("Usuário: ").title()
            if len(user) > 1:
                while True:
                    try:
                        cleanScreen()
                        writeScreen(f'Usuário: {user}')
                        email = input("E-mail: ")
                        if "@" in email and len(email) > 1:
                            player_file = (f'Usuário: {user} - E-mail: {email}\n')
                            file = open("snake_users.txt", "a")
                            file.write(player_file)
                            file.close()
                            break
                    except ValueError:
                        writeScreen(ValueError)
            break
        except ValueError:
            writeScreen(ValueError)

def backgroundScreen():
    window.blit(background, background_position)

def background_gameOverScreen():
    window.blit(background_gameOver, background_position)
    pg.mixer.music.load("background_gameOver_sound.mp3")
    pg.mixer.music.play(1)
    pg.mixer.music.set_volume(1)
    
def eatApple():
    pg.mixer.music.load("eat_apple_sound.mp3")
    pg.mixer.music.play(1)
    pg.mixer.music.set_volume(1)

def showScore(score):
    window.blit(font.render("Pontuação:" + str(score), True, color_white), (0, 670))
    window.blit(font.render("ESC para sair", True, color_white), (465, 670))
