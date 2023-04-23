import pygame
import sys
import math
from button import Button

pygame.init()
screen = pygame.display.set_mode((640, 640))

black = (0, 0, 0)
purple = (77, 3, 68)
white = (255, 255, 255)
grey = (0, 0, 0)
brown = (210, 125, 45)
TILE_SIZE = 32
floorBG = pygame.image.load('assets/floorBG.png')
playerImg = pygame.image.load('assets/player.png')
ghostyellowImg = pygame.image.load('assets/ghostyellow.png')
ghostblueImg = pygame.image.load('assets/ghostblue.png')
ghostorangeImg = pygame.image.load('assets/ghostorange.png')
ghostpurpleImg = pygame.image.load('assets/ghostpurple.png')
ghostgreenImg = pygame.image.load('assets/ghostgreen.png')
keyImg = pygame.image.load('assets/key.png')
candyImg = pygame.image.load('assets/sugar.png')
giftImg = pygame.image.load('assets/gift-box.png')
pygame.display.set_caption("Menu")
MainBG = pygame.image.load("assets/menuBG.png")
InstBG = pygame.image.load("assets/instBG.png")
LoseBG = pygame.image.load("assets/loseBG.png")
WinBG = pygame.image.load("assets/winBG.png")

fps = 30
fpsClock = pygame.time.Clock()


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font3.otf", size)


maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 0],
    [0, 1, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 5, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 4, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 3, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 4, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 4, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 0],
    [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


class Maze:

    def drawMaze(self):
        for row in range(len(maze)):
            for column in range(len(maze[row])):
                x = column * TILE_SIZE
                y = row * TILE_SIZE

                if maze[row][column] == 1:
                    # Create a rect with the size of the image.
                    pygame.draw.rect(screen, black, (x, y, 32, 32))
                elif maze[row][column] == 2:
                    # door
                    pygame.draw.rect(screen, brown, (x, y, 32, 32))
                elif maze[row][column] == 3:
                    # key
                    screen.blit(keyImg, (x, y))
                elif maze[row][column] == 4:
                    # candy
                    screen.blit(candyImg, (x, y))
                elif maze[row][column] == 5:
                    # gift
                    screen.blit(giftImg, (x, y))

    def wall_left(self, row, col):
        if maze[row][col] == 1:
            return True

    def wall_right(self, row, col):
        if maze[row][col + 1] == 1:
            return True

    def wall_up(self, row, col):
        if maze[row][col] == 1:
            return True

    def wall_down(self, row, col):
        if maze[row + 1][col] == 1:
            return True

    def door(self, row, col):
        if maze[row][col] == 2:
            return True

    def iskey(self, row, col):
        if maze[row][col] == 3:
            return True

    def iscandy(self, row, col):
        if maze[row][col] == 4:
            return True

    def isgift(self, row, col):
        if maze[row][col] == 5:
            return True


class Player:
    x = 90
    y = 590
    step = 4
    havekey = False
    havegift = False
    candyCount = 0

    def newgame(self):
        self.x = 90
        self.y = 590
        self.step = 7
        self.havekey = False
        self.candyCount = 0
        self.havegift = False
        
        maze[10][10] = 3  # for key
        maze[2][2] = 4  # for candy
        maze[2][10] = 4
        maze[3][16] = 4
        maze[8][8] = 4
        maze[17][17] = 4
        maze[14][14] = 4
        maze[5][10] = 4
        maze[10][2] = 4
        maze[5][14] = 5  # for gift

    def draw(self):
        screen.blit(playerImg, (self.x, self.y))

    def move(self, keys):
        pos = self.x, self.y
        if keys[pygame.K_LEFT]:
            if self.x > 0:
                self.x -= self.step
        if keys[pygame.K_RIGHT]:
            if self.x < 590:
                self.x += self.step
        if keys[pygame.K_UP]:
            if self.y > 0:
                self.y -= self.step
        if keys[pygame.K_DOWN]:
            if self.y < 590:
                self.y += self.step

        row = self.y // 32
        column = self.x // 32

        if grid.wall_left(row, column):
            self.x, self.y = pos

        if grid.wall_down(row, column):
            self.x, self.y = pos

        if grid.wall_up(row, column):
            self.x, self.y = pos

        if grid.wall_right(row, column):
            self.x, self.y = pos

        if grid.iskey(row, column):
            self.havekey = True
            drawblank(row, column)

        if grid.iscandy(row, column):
            self.candyCount += 1
            drawblank(row, column)

        if grid.isgift(row, column):
            enemy.ghostBlue()
            player.havegift = True
            drawblank(row, column)

        if grid.iscandy(row + 1, column):
            self.candyCount += 1
            drawblank(row + 1, column)

        if grid.iscandy(row, column + 1):
            self.candyCount += 1
            drawblank(row, column + 1)

        if grid.door(row, column):
            if self.havekey:
                youwin()
            else:
                if grid.door(row, column):
                    self.x, self.y = pos


class Enemy:
    ghostYellowX = 180
    ghostYellowY = 500

    ghostPurpleX = 80
    ghostPurpleY = 200

    ghostGreenX = 300
    ghostGreenY = 320

    ghostOrangeX = 480
    ghostOrangeY = 100

    ghostBlueX = 90
    ghostBlueY = 590

    ghostYellowStep = 6
    ghostPurpleStep = 3
    ghostOrangeStep = 4
    ghostGreenStep = 6
    ghostBlueStep = 2

    def ghostYellow(self):
        screen.blit(ghostyellowImg, (self.ghostYellowX, self.ghostYellowY))
        # movement
        self.ghostYellowY += self.ghostYellowStep
        if self.ghostYellowY <= 50:
            self.ghostYellowStep = 6
        elif self.ghostYellowY >= 550:
            self.ghostYellowStep = -6

    def ghostGreen(self):  # near the keys
        screen.blit(ghostgreenImg, (self.ghostGreenX, self.ghostGreenY))
        # movement
        self.ghostGreenX += self.ghostGreenStep
        if self.ghostGreenX <= 250:
            self.ghostGreenStep = 3
        elif self.ghostGreenX >= 450:
            self.ghostGreenStep = -3

    def ghostOrange(self):  # near the exit
        screen.blit(ghostorangeImg, (self.ghostOrangeX, self.ghostOrangeY))
        # movement
        self.ghostOrangeX += self.ghostOrangeStep
        if self.ghostOrangeX <= 450:
            self.ghostOrangeStep = 3
        elif self.ghostOrangeX >= 600:
            self.ghostOrangeStep = -3

    def ghostPurple(self):
        screen.blit(ghostpurpleImg, (self.ghostPurpleX, self.ghostPurpleY))
        # movement
        self.ghostPurpleY += self.ghostPurpleStep
        if self.ghostPurpleY <= 50:
            self.ghostPurpleStep = 3
        elif self.ghostPurpleY >= 500:
            self.ghostPurpleStep = -3

    def ghostBlue(self):  # chase after the player
        screen.blit(ghostblueImg, (self.ghostBlueX, self.ghostBlueY))
        # movement
        if self.ghostBlueX < player.x:
            self.ghostBlueX += self.ghostBlueStep
        if self.ghostBlueX > player.x:
            self.ghostBlueX -= self.ghostBlueStep
        if self.ghostBlueY < player.y:
            self.ghostBlueY += self.ghostBlueStep
        if self.ghostBlueY > player.y:
            self.ghostBlueY -= self.ghostBlueStep


def drawblank(row, col):
    maze[row][col] = 0
    pygame.display.update()


def isCollision(enemyX, enemyY, Playerx, Playery):
    distance = math.sqrt(math.pow(enemyX - Playerx, 2) + (math.pow(enemyY - Playery, 2)))
    if distance < 25:
        return True
    return False


player = Player()
grid = Maze()
enemy = Enemy()


def play():
    # game loop
    while True:

        screen.fill(grey)
        screen.blit(floorBG, (0, 0))
        pygame.display.set_caption("Game Mode")
        grid.drawMaze()
        player.draw()
        enemy.ghostYellow()
        enemy.ghostGreen()
        enemy.ghostPurple()
        enemy.ghostOrange()

        if player.havegift:
            enemy.ghostBlue()
            pygame.display.update()
            if isCollision(enemy.ghostBlueX, enemy.ghostBlueY, player.x, player.y):
                youlose()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.move(keys)

        if isCollision(enemy.ghostYellowX, enemy.ghostYellowY, player.x, player.y):
            youlose()

        if isCollision(enemy.ghostPurpleX, enemy.ghostPurpleY, player.x, player.y):
            youlose()

        if isCollision(enemy.ghostGreenX, enemy.ghostGreenY, player.x, player.y):
            youlose()

        if isCollision(enemy.ghostOrangeX, enemy.ghostOrangeY, player.x, player.y):
            youlose()

        pygame.display.update()
        fpsClock.tick(fps)


def instructions():
    while True:
        inst_mousepos = pygame.mouse.get_pos()

        screen.fill("white")
        screen.blit(InstBG, (0, 0))

        inst_back = Button(image=None, pos=(100, 600),
                           text_input="Back", font=get_font(40), base_color="White", hovering_color="Green")

        inst_back.changeColor(inst_mousepos)
        inst_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inst_back.checkForInput(inst_mousepos):
                    main_menu()

        pygame.display.update()


def youlose():
    while True:
        lose_mousepos = pygame.mouse.get_pos()

        screen.fill("white")
        screen.blit(LoseBG, (0, 0))

        Lose_PlayAgain = Button(image=None, pos=(500, 500),
                                text_input="Play Again", font=get_font(40), base_color="Yellow", hovering_color="Green")

        Lose_Quit = Button(image=None, pos=(500, 600),
                           text_input="Quit", font=get_font(40), base_color="Yellow", hovering_color="Green")

        Lose_PlayAgain.changeColor(lose_mousepos)
        Lose_PlayAgain.update(screen)
        Lose_Quit.changeColor(lose_mousepos)
        Lose_Quit.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Lose_PlayAgain.checkForInput(lose_mousepos):
                    player.newgame()
                    play()
                if Lose_Quit.checkForInput(lose_mousepos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def youwin():
    while True:
        win_mousepos = pygame.mouse.get_pos()

        screen.fill("white")
        screen.blit(WinBG, (0, 0))

        scoretext = "Candies Collected: " + str(player.candyCount)

        win_CandyScore = Button(image=pygame.image.load("assets/GreyRect.png"), pos=(300, 400),
                                text_input=scoretext, font=get_font(40), base_color="Yellow", hovering_color="White")

        win_PlayAgain = Button(image=None, pos=(150, 500),
                               text_input="Play Again", font=get_font(40), base_color="White", hovering_color="Green")

        win_Quit = Button(image=None, pos=(150, 600),
                          text_input="Quit", font=get_font(40), base_color="White", hovering_color="Green")

        win_CandyScore.changeColor(win_mousepos)
        win_CandyScore.update(screen)
        win_PlayAgain.changeColor(win_mousepos)
        win_PlayAgain.update(screen)
        win_Quit.changeColor(win_mousepos)
        win_Quit.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if win_PlayAgain.checkForInput(win_mousepos):
                    player.newgame()
                    play()
                if win_Quit.checkForInput(win_mousepos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def main_menu():
    while True:
        screen.blit(MainBG, (0, 0))

        menu_mousepos = pygame.mouse.get_pos()

        playButton = Button(image=pygame.image.load("assets/GreyRect.png"), pos=(320, 230),
                            text_input="Play", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        instButton = Button(image=pygame.image.load("assets/GreyRect.png"), pos=(320, 380),
                            text_input="Instructions", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        quitButton = Button(image=pygame.image.load("assets/GreyRect.png"), pos=(320, 530),
                            text_input="Quit", font=get_font(45), base_color="#d7fcd4", hovering_color="White")

        for button in [playButton, instButton, quitButton]:
            button.changeColor(menu_mousepos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(menu_mousepos):
                    play()
                if instButton.checkForInput(menu_mousepos):
                    instructions()
                if quitButton.checkForInput(menu_mousepos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
