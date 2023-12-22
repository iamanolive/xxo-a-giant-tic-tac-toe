import pygame
pygame.init()

screenWidth = 900
screenHeight = 900

# setting primary variables
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("XXO A Giant Tic Tac Toe")
clock = pygame.time.Clock()
screen.fill("#444444")
font = pygame.font.Font(None, 50)

# declaring game variables
xImage = pygame.image.load('x.png')
oImage = pygame.image.load('o.png')
currentChoice = "x"
winnerX = False
winnerO = False

playerOwins = font.render("Player O wins this round!", True, "White")
winnerOrect = playerOwins.get_rect(center = (450, 100))

playerXwins = font.render("Player X wins this round!", True, "White")
winnerXrect = playerXwins.get_rect(center = (450, 100))

startGame = font.render("Welcome to the computerized Tic Tac Toe!", True, "White")
startGameRect = startGame.get_rect(center = (450, 100))

instruction = font.render("Press the spacebar key to start playing", True, "White")
instructionRect = instruction.get_rect(center = (450, 700))

# changing between screens
currentlyPlaying = True

# variables that reflect whether the blocks are filled
block1 = "nil"
block2 = "nil"
block3 = "nil"
block4 = "nil"
block5 = "nil"
block6 = "nil"
block7 = "nil"
block8 = "nil"
block9 = "nil"


# running the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        
        # drawing white line block-seperators on the game board
        pygame.draw.line(screen, "White", (300, 0), (300, 900), 10)
        pygame.draw.line(screen, "White", (600, 0), (600, 900), 10)
        pygame.draw.line(screen, "White", (0, 300), (900, 300), 10)
        pygame.draw.line(screen, "White", (0, 600), (900, 600), 10)



        if currentlyPlaying:
            if event.type == pygame.KEYDOWN:
                # if key 0 is pressed (QUIT GAME, BACK TO HOME SCREEN)
                if event.key == pygame.K_0:
                    currentlyPlaying = False
                # if key 1 is pressed
                if event.key == pygame.K_1 and block1 == "nil":
                    if currentChoice == "x":
                        screen.blit(xImage, (0, 0))
                        block1 = currentChoice
                        currentChoice = "o"
                        break
                    elif currentChoice == "o":
                        screen.blit(oImage, (0, 0))
                        block1 = currentChoice
                        currentChoice = "x"
                        break
                # if key 2 is pressed
                if event.key == pygame.K_2 and block2 == "nil":
                    if currentChoice == "x":
                        screen.blit(xImage, (300, 0))
                        block2 = currentChoice
                        currentChoice = "o"
                        break
                    elif currentChoice == "o":
                        screen.blit(oImage, (300, 0))
                        block2 = currentChoice
                        currentChoice = "x"
                        break
                # if key 3 is pressed
                if event.key == pygame.K_3 and block3 == "nil":
                    if currentChoice == "x":
                        screen.blit(xImage, (600, 0))
                        block3 = currentChoice
                        currentChoice = "o"
                        break
                    elif currentChoice == "o":
                        screen.blit(oImage, (600, 0))
                        block3 = currentChoice
                        currentChoice = "x"
                        break
                # if key 4 is pressed
                if event.key == pygame.K_4 and block4 == "nil":
                    if currentChoice == "x":
                        screen.blit(xImage, (0, 300))
                        block4 = currentChoice
                        currentChoice = "o"
                        break
                    elif currentChoice == "o":
                        screen.blit(oImage, (0, 300))
                        block4 = currentChoice
                        currentChoice = "x"
                        break
                # if key 5 is pressed
                if event.key == pygame.K_5 and block5 == "nil":
                    if currentChoice == "x":
                        screen.blit(xImage, (300, 300))
                        block5 = currentChoice
                        currentChoice = "o"
                        break
                    elif currentChoice == "o":
                        screen.blit(oImage, (300, 300))
                        block5 = currentChoice
                        currentChoice = "x"
                        break
                # if key 6 is pressed
                if event.key == pygame.K_6 and block6 == "nil":
                    if currentChoice == "x":
                        screen.blit(xImage, (600, 300))
                        block6 = currentChoice
                        currentChoice = "o"
                        break
                    elif currentChoice == "o":
                        screen.blit(oImage, (600, 300))
                        block6 = currentChoice
                        currentChoice = "x"
                        break
                # if key 7 is pressed 
                if event.key == pygame.K_7 and block7 == "nil":
                    if currentChoice == "x":
                        screen.blit(xImage, (0, 600))
                        block7 = currentChoice
                        currentChoice = "o"
                        break
                    elif currentChoice == "o":
                        screen.blit(oImage, (0, 600))
                        block7 = currentChoice
                        currentChoice = "x"
                        break
                # if key 8 is pressed
                if event.key == pygame.K_8 and block8 == "nil":
                    if currentChoice == "x":
                        screen.blit(xImage, (300, 600))
                        block8 = currentChoice
                        currentChoice = "o"
                        break
                    elif currentChoice == "o":
                        screen.blit(oImage, (300, 600))
                        block8 = currentChoice
                        currentChoice = "x"
                        break
                # if key 9 is pressed
                if event.key == pygame.K_9 and block9 == "nil":
                    if currentChoice == "x":
                        screen.blit(xImage, (600, 600))
                        block9 = currentChoice
                        currentChoice = "o"
                        break
                    elif currentChoice == "o":
                        screen.blit(oImage, (600, 600))
                        block9 = currentChoice
                        currentChoice = "x"
                        break
                
            if currentlyPlaying:
                # checking for winning condition
                # X X X first row
                if block1 == block2 == block3 == "x":
                    winnerX = True
                    currentlyPlaying = False
                # O O O first row
                elif block1 == block2 == block3 == "o":
                    winnerO = True
                    currentlyPlaying = False
                # X X X second row
                elif block4 == block5 == block6 == "x":
                    winnerX = True
                    currentlyPlaying = False
                # O O O second row
                elif block4 == block5 == block6 == "o":
                    winnerO = True
                    currentlyPlaying = False
                # X X X third row
                elif block7 == block8 == block9 == "x":
                    winnerX = True
                    currentlyPlaying = False
                # O O O third row
                elif block7 == block8 == block9 == "o":
                    winnerO = True
                    currentlyPlaying = False
                # X X X first column
                elif block1 == block4 == block7 == "x":
                    winnerX = True
                    currentlyPlaying = False
                # O O O first column
                elif block1 == block4 == block7 == "o":
                    winnerO = True
                    currentlyPlaying = False
                # X X X second column
                elif block2 == block5 == block8 == "x":
                    winnerX = True
                    currentlyPlaying = False
                # O O O second column
                elif block2 == block5 == block8 == "o":
                    winnerO = True
                    currentlyPlaying = False
                # X X X third column
                elif block3 == block6 == block9 == "x":
                    winnerX = True
                    currentlyPlaying = False
                # O O O third column
                elif block3 == block6 == block9 == "o":
                    winnerO = True
                    currentlyPlaying = False
                # X X X left to right slanting
                elif block1 == block5 == block9 == "x":
                    winnerX = True
                    currentlyPlaying = False
                # O O O left to right slanting
                elif block1 == block5 == block9 == "o":
                    winnerO = True
                    currentlyPlaying = False
                # X X X right to left slanting
                elif block3 == block5 == block7 == "x":
                    winnerX = True
                    currentlyPlaying = False
                # O O O right to left slanting
                elif block3 == block5 == block7 == "o":
                    winnerO = True
                    currentlyPlaying = False
            
        else:
            screen.fill("#444444")
            if winnerO == True:
                screen.blit(winnerOrect)
                screen.blit(oImage, (300, 300))
                screen.blit(instructionRect)
            elif winnerX == True:
                screen.blit(winnerXrect)
                screen.blit(xImage, (300, 300))
                screen.blit(instructionRect)
            else:
                screen.blit(startGameRect)
                screen.blit(xImage, (175, 300))
                screen.blit(oImage, (300, 200))
                screen.blit(instructionRect)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                currentlyPlaying = True



    pygame.display.update()
    clock.tick(600)
    

pygame.quit()