import pygame

from config import Config
from snake import Snake
from apple import Apple

class Game():

    def __init__(self):
        pygame.init()
        
        self.direction = 'RIGHT'
        self.direction_change = self.direction

        self.clock = pygame.time.Clock()

        pygame.display.set_caption(Config['game']['caption'])
        self.screen = pygame.display.set_mode((Config['game']['width'], Config['game']['height']))

        self.snake_body = Snake().get_snake_body()
        self.snake_position = Snake().get_snake_position()

        self.apple_spawn = Apple().get_apple_spawn
        self.apple_position = Apple().get_apple_position()

        self.score = 0
        self.high_score = 0
        self.scores = []

        self.not_playing = True
        self.in_menu = True
        self.in_instructions = False
        self.run = False 
        self.in_credits = False
        self.in_difficulty_selection = False

        self.font = pygame.font.Font(Config['game']['font'], Config['game']['font_size'])

    def main_menu(self):

        for self.event in pygame.event.get():

            self.screen.fill(Config['colors']['white'])
    
            self.play_button_text = self.font.render("Click to Play", True, Config['colors']['white'])
            self.instructions_button_text = self.font.render("Instructions", True, Config['colors']['white'])
            self.credits_button_text = self.font.render("Credits", True, Config['colors']['white'])
    
            self.play_button_rect = self.play_button_text.get_rect(center = (Config['game']['width'] / 2, Config['game']['height'] / 2))
            self.instructions_button_rect = self.instructions_button_text.get_rect(center = (200, Config['game']['height'] / 2))
            self.credits_button_rect = self.credits_button_text.get_rect(center = (600, Config['game']['height'] / 2))
    
            pygame.draw.rect(self.screen, Config['colors']['black'], self.play_button_rect)
            pygame.draw.rect(self.screen, Config['colors']['black'], self.instructions_button_rect)
            pygame.draw.rect(self.screen, Config['colors']['black'], self.credits_button_rect)
    
            self.screen.blit(self.play_button_text, self.play_button_rect)
            self.screen.blit(self.instructions_button_text, self.instructions_button_rect)
            self.screen.blit(self.credits_button_text, self.credits_button_rect)

            if self.event.type == pygame.QUIT:
                self.running = False
                self.in_menu = False
                self.run = False
                self.in_instructions = False
                self.in_credits = False
                self.in_difficulty_selection = False
                self.not_playing = False

            if self.event.type == pygame.MOUSEBUTTONDOWN:
                self.position = pygame.mouse.get_pos()
                if self.play_button_rect.collidepoint(self.position):
                    self.in_menu = False
                    self.in_instructions = False
                    self.in_credits = False
                    self.run = False
                    self.in_difficulty_selection = True

                if self.instructions_button_rect.collidepoint(self.position):
                    self.in_menu = False
                    self.run = False
                    self.in_credits = False
                    self.in_difficulty_selection = False
                    self.in_instructions = True

                if self.credits_button_rect.collidepoint(self.position):
                    self.in_menu = False
                    self.run = False
                    self.in_instructions = False
                    self.in_difficulty_selection = False
                    self.in_credits = True

        pygame.display.update()

    def difficulty_selection(self):

        for self.event in pygame.event.get():

            self.screen.fill(Config['colors']['white'])
    
            self.easy_button_text = self.font.render("Easy", True, Config['colors']['white'])
            self.normal_button_text = self.font.render("Normal", True, Config['colors']['white'])
            self.hard_button_text = self.font.render("Hard", True, Config['colors']['white'])
            
            self.easy_button_rect = self.easy_button_text.get_rect(center = (200, Config['game']['height'] / 2))
            self.normal_button_rect = self.normal_button_text.get_rect(center = (Config['game']['width'] / 2, Config['game']['height'] / 2))
            self.hard_button_rect = self.hard_button_text.get_rect(center = (600, Config['game']['height'] / 2))
    
            pygame.draw.rect(self.screen, Config['colors']['black'], self.easy_button_rect)
            pygame.draw.rect(self.screen, Config['colors']['black'], self.normal_button_rect)
            pygame.draw.rect(self.screen, Config['colors']['black'], self.hard_button_rect)
    
            self.screen.blit(self.easy_button_text, self.easy_button_rect)
            self.screen.blit(self.normal_button_text, self.normal_button_rect)
            self.screen.blit(self.hard_button_text, self.hard_button_rect)

            if self.event.type == pygame.QUIT:
                self.running = False
                self.in_menu = False
                self.run = False
                self.in_instructions = False
                self.in_credits = False
                self.in_difficulty_selection = False
                self.not_playing = False

            if self.event.type == pygame.MOUSEBUTTONDOWN:
                self.position = pygame.mouse.get_pos()
                if self.easy_button_rect.collidepoint(self.position):
                    self.difficulty_choice = 'easy'
                    self.run = True
                    self.not_playing = False
                    self.in_difficulty_selection = False

                if self.normal_button_rect.collidepoint(self.position):
                    self.difficulty_choice = 'normal'
                    self.run = True
                    self.not_playing = False
                    self.in_difficulty_selection = False

                if self.hard_button_rect.collidepoint(self.position):
                    self.difficulty_choice = 'hard'
                    self.run = True
                    self.not_playing = False
                    self.in_difficulty_selection = False

        pygame.display.update()

    def instructions(self):

        for self.event in pygame.event.get():

            if self.event.type == pygame.QUIT:
                self.running = False
                self.in_menu = False
                self.run = False
                self.in_instructions = False
                self.in_credits = False
                self.in_difficulty_selection = False
                self.not_playing = False

        self.screen.fill(Config['colors']['black'])
        self.instructions_text = self.font.render("Welcome to Snake!\nUse the arrow keys to move the snake around the open space and eat the apple!\nThere are only two rules you must follow when playing: don’t hit a wall and don’t bite your own tail.\nCrashing into a wall or your tail will end the game immediately. Your high score is calculated based on the number of apples you at.\nYou win the game when there is no more room for your snake to grow. Remember to have fun!", True, Config['colors']['white'])
        self.instructions_text_rect = self.instructions_text.get_rect(center = (Config['game']['width'] / 2, Config['game']['height'] / 2))
        self.screen.blit(self.instructions_text, self.instructions_text_rect)

        pygame.display.update()

    def credits(self):

        self.credit_list = ["Credits - The Snake Game"," ","Logic - Arnav Mehra","Colouring - Arnav Mehra", "Programming - Arnav Mehra", "Configuration File - Aloo Ji", "My Sanity - Gone"]

        self.texts = []

        for i, line in enumerate(self.credit_list):

            self.text = self.font.render(line, 1, (10, 10, 10))
            self.text_rectangle = self.text.get_rect(centerx = self.screen.get_rect().centerx, y=self.screen.get_rect().bottom + i * 45)
            self.texts.append((self.text_rectangle, self.text))

        self.running = True

        while self.running:

            self.screen.fill(Config['colors']['white'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.in_menu = False
                    self.run = False
                    self.in_instructions = False
                    self.in_credits = False
                    self.in_difficulty_selection = False
                    self.not_playing = False

            for self.text_rectangle, self.text in self.texts:
                self.text_rectangle.move_ip(0, -10)
                self.screen.blit(self.text, self.text_rectangle)

            if not self.screen.get_rect().collidelistall([text_rectangle for (text_rectangle, text) in self.texts]):
                self.in_menu = True
                self.not_playing = True
                self.running = False
                self.in_credits = False
            
            pygame.display.update()
            self.clock.tick(30)    

    def find_high_score(self):

        self.file = open("high_score.txt", "r")

        self.current_line = self.file.readline().rstrip("\n")
        self.current_line = int(self.current_line)
        self.high_score = self.current_line

    def add_high_score(self):
        self.file = open("high_score.txt", "w")
        self.file.write(str(self.high_score))

    def snake_movement_change(self):

        if self.event.type == pygame.KEYDOWN:

            if self.event.key == pygame.K_UP or self.event.key == pygame.K_w:
                self.direction_change = "UP"
            if self.event.key == pygame.K_DOWN or self.event.key == pygame.K_s:
                self.direction_change = "DOWN"
            if self.event.key == pygame.K_LEFT or self.event.key == pygame.K_a:
                self.direction_change = "LEFT"
            if self.event.key == pygame.K_RIGHT or self.event.key == pygame.K_d:
                self.direction_change = "RIGHT"
            
        if self.direction_change == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.direction_change == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.direction_change == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.direction_change == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def snake_movement(self):
            
            if self.direction == "UP":
                self.snake_position[1] -= Config['snake']['height']
            if self.direction == "DOWN":
                self.snake_position[1] += Config['snake']['height']
            if self.direction == "LEFT":
                self.snake_position[0] -= Config['snake']['width']
            if self.direction == "RIGHT":
                self.snake_position[0] += Config['snake']['width']

    def snake_apple_collision(self):

        self.snake_body.insert(0, list(self.snake_position))
        self.apple = pygame.Rect(self.apple_position[0], self.apple_position[1], Config['apple']['width'], Config['apple']['height'])
        self.snake_head = pygame.Rect(self.snake_body[0][0], self.snake_body[0][1], Config['snake']['width'], Config['snake']['height'])

        if self.snake_head.colliderect(self.apple):
            self.apple_spawn = False
            self.score += 1
        else:
            self.snake_body.pop()

        if not self.apple_spawn:
            self.apple_position = Apple().get_apple_position()
            self.apple_spawn = True
    
    def show_text(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score_text = self.font.render(f"Score: {self.score} | High Score: {self.high_score}", True, Config['colors']['white'])
        self.screen.blit(self.score_text, self.score_text.get_rect(midbottom = (Config['game']['width'] / 2, Config['game']['height'] + 3)))

    def game_over():
        pass

    def start(self):
        
        self.find_high_score()

        while self.not_playing:

            while self.in_menu:

                self.main_menu()

            while self.in_difficulty_selection:

                self.difficulty_selection()

            while self.in_instructions:

                self.instructions()

            while self.in_credits:

                self.credits()

        while self.run:

            for self.event in pygame.event.get():

                if self.event.type == pygame.QUIT:
                    self.run = False

                self.snake_movement_change()
            self.snake_movement()
            self.snake_apple_collision()

            self.screen.fill(Config['colors']['blue'])
            self.window = pygame.Rect(Config['game']['bumper_size'], Config['game']['bumper_size'], Config['game']['width'] - Config['game']['bumper_size'] * 2, Config['game']['height'] - Config['game']['bumper_size'] * 2)

            pygame.draw.rect(self.screen, Config['colors']['black'], self.window)

            self.show_text()

            for position in self.snake_body:
                pygame.draw.rect(self.screen, Config['colors']['green'], pygame.Rect(position[0], position[1], Config['snake']['width'], Config['snake']['height']))
                pygame.draw.rect(self.screen, Config['colors']['apple-red'], pygame.Rect(self.apple_position[0], self.apple_position[1], Config['apple']['width'], Config['apple']['height']))

            if (self.snake_position[0] < 20 or self.snake_position[0] + Config['snake']['width'] > Config['game']['width'] - Config['game']['bumper_size']) or (self.snake_position[1] < 20 or self.snake_position[1] + Config['snake']['height'] > Config['game']['height'] - Config['game']['bumper_size']):
                self.run = False

            for block in self.snake_body[1:]:
                if self.snake_position[0] == block[0] and self.snake_position[1] == block[1]:
                    self.run = False

            pygame.display.update()
            self.clock.tick(Config['difficulty'][self.difficulty_choice])

        
        self.add_high_score()
        pygame.quit()
