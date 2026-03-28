import sys, random
from snake_assets import pg, window, color_goldenrod, color_red, score, userData, backgroundScreen, background_gameOverScreen, eatApple, showScore

clock = pg.time.Clock()

snake_position = [340, 340]
snake_size = [10]
snake_speed = 10

apple_position = [random.randrange(1, 70) * 10, random.randrange(10 , 66) * 10] 
apple_spawn = True

direction = ''
change_to = direction

def gameMain(score, snake_size, snake_position, apple_position, apple_spawn, direction, change_to):
    while True:           
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_w or event.key == pg.K_UP:
                    change_to = "UP"
                if event.key == pg.K_s or event.key == pg.K_DOWN:
                    change_to = "DOWN"
                if event.key == pg.K_a or event.key == pg.K_LEFT:
                    change_to = "LEFT"
                if event.key == pg.K_d or event.key == pg.K_RIGHT:
                    change_to = "RIGHT"
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
        
        if change_to == "UP" and direction != "DOWN":
            direction = "UP"
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        
        if direction == "UP":
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10
        
        snake_size.insert(0, list(snake_position))
        if snake_position[0] == apple_position[0] and snake_position[1] == apple_position[1]:
            score += 1
            eatApple()
            apple_spawn = False
        else:
            snake_size.pop()

        if not apple_spawn:
            apple_position = [random.randrange(1, 70) * 10, random.randrange(10, 66) * 10]
            apple_spawn = True
            
        backgroundScreen()

        for pos in snake_size:
            pg.draw.rect(window, color_goldenrod, pg.Rect(pos[0], pos[1], 10, 10))
            
        pg.draw.rect(window, color_red, pg.Rect(apple_position[0], apple_position[1], 10, 10))
            
        if snake_position[0] < 0:
            snake_position[0] = 690
        if snake_position[0] > 690: 
            snake_position[0] = 0
        if snake_position[1] < 0:
            snake_position[1] = 690  
        if snake_position[1] > 690:
            snake_position[1] = 0

        for pixel in snake_size[1:]:
            if snake_position[0] == pixel[0] and snake_position[1] == pixel[1]:
                background_gameOverScreen()
                direction = ''
                change_to = direction
                score = 0
                snake_size = [1]
                snake_position = [340, 340]

        if snake_position[1] < 10 or snake_position[1] > 660:
            background_gameOverScreen()
            direction = ''
            change_to = direction
            score = 0
            snake_size = [1]
            snake_position = [340, 340]

        showScore(score)

        pg.display.update()   
        clock.tick(snake_speed)

userData()
gameMain(score, snake_size, snake_position, apple_position, apple_spawn, direction, change_to)