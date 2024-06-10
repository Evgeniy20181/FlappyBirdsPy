import pygame
import sys
import random
from typing import List, Tuple
#import time
class Bird:
    def __init__(self) -> None:
        # Load bird images
        self.bird_up = pygame.image.load("./imgs/img_47.png")
        self.bird_down = pygame.image.load("./imgs/img_48.png")
        self.bird_mid = pygame.image.load("./imgs/img_49.png")
        self.birds = [self.bird_up, self.bird_mid, self.bird_down]
        self.bird_index = 0
        self.bird_flap = pygame.USEREVENT
        pygame.time.set_timer(self.bird_flap, 200)
        self.bird_img = self.birds[self.bird_index]
        self.bird_rect = self.bird_img.get_rect(center=(67, 622 // 2))
        self.bird_movement = 0
        self.gravity = 0.17

    def update(self) -> None:
        # Apply gravity to bird's movement
        self.bird_movement += self.gravity
        self.bird_rect.centery += self.bird_movement

    def flap(self) -> None:
        # Make the bird flap (move up)
        self.bird_movement = 0
        self.bird_movement = -7

    def rotate(self) -> pygame.Surface:
        # Rotate bird image based on its movement
        return pygame.transform.rotozoom(self.bird_img, self.bird_movement * -6, 1)

    def animate(self) -> None:
        # Cycle through bird images for flapping animation
        self.bird_index += 1
        if self.bird_index > 2:
            self.bird_index = 0
        self.bird_img = self.birds[self.bird_index]
        self.bird_rect = self.bird_up.get_rect(center=self.bird_rect.center)

    def reset(self) -> None:
        # Reset bird's position and movement
        self.bird_movement = 0
        self.bird_rect = self.bird_img.get_rect(center=(67, 622 // 2))

    def draw(self, screen: pygame.Surface) -> None:
        # Draw the rotated bird on the screen
        screen.blit(self.rotate(), self.bird_rect)

class Pipes:
    def __init__(self) -> None:
        # Load pipe image and set heights
        self.pipe_img = pygame.image.load("./imgs/greenpipe.png")
        self.pipe_height = [400, 350, 533, 490]
        self.pipes: List[pygame.Rect] = []
        self.create_pipe = pygame.USEREVENT + 1
        pygame.time.set_timer(self.create_pipe, 1200)

    def create_pipes(self) -> Tuple[pygame.Rect, pygame.Rect]:
        # Create top and bottom pipes at random heights
        pipe_y = random.choice(self.pipe_height)
        top_pipe = self.pipe_img.get_rect(midbottom=(467, pipe_y - 300))
        bottom_pipe = self.pipe_img.get_rect(midtop=(467, pipe_y))
        return top_pipe, bottom_pipe

    def update(self, bird_rect: pygame.Rect) -> bool:
        # Move pipes to the left and check for collisions
        game_over = False
        for pipe in self.pipes:
            pipe.centerx -= 3
            if pipe.right < 0:
                self.pipes.remove(pipe)
            if bird_rect.colliderect(pipe):
                game_over = True
        return game_over

    def draw(self, screen: pygame.Surface) -> None:
        # Draw pipes on the screen
        for pipe in self.pipes:
            if pipe.top < 0:
                flipped_pipe = pygame.transform.flip(self.pipe_img, False, True)
                screen.blit(flipped_pipe, pipe)
            else:
                screen.blit(self.pipe_img, pipe)

    def add_pipe(self) -> None:
        # Add a new set of pipes to the list
        self.pipes.extend(self.create_pipes())

class Game:
    def __init__(self) -> None:
        # Initialize game window and assets
        pygame.init()
        pygame.mixer.init() #music engine

        self.width, self.height = 350, 622
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Flappy Bird")

        self.back_img = pygame.image.load("./imgs/img_46.png")
        self.floor_img = pygame.image.load("./imgs/img_50.png")
        self.floor_x = 0

        self.bird = Bird()
        self.pipes = Pipes()

        self.game_over = True
        self.over_img = pygame.image.load("./imgs/img_45.png").convert_alpha()
        self.over_rect = self.over_img.get_rect(center=(self.width // 2, self.height // 2))

        self.score = 0
        self.high_score = 0
        self.score_time = True
        self.score_font = pygame.font.Font("FreeSansBold.ttf", 27)

        #music
        self.background_music = pygame.mixer.Sound('./sounds/Flappy Bird Theme Song.mp3')
        self.score_sound = pygame.mixer.Sound('./sounds/score.wav')
        self.game_over_sound = pygame.mixer.Sound('./sounds/gameOver.mp3')

        # Set volume to 85%
        self.background_music.set_volume(0.25)
        self.score_sound.set_volume(0.3)
        self.game_over_sound.set_volume(0.85)

        # Start playing background music
        self.background_music.play(loops=-1)

    def draw_floor(self) -> None:
        # Draw the floor (moving ground)
        self.screen.blit(self.floor_img, (self.floor_x, 520))
        self.screen.blit(self.floor_img, (self.floor_x + 448, 520))

    def draw_score(self, game_state: str) -> None:
        # Draw the score on the screen
        if game_state == "game_on":
            score_text = self.score_font.render(str(self.score), True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(self.width // 2, 66))
            self.screen.blit(score_text, score_rect)
        elif game_state == "game_over":
            score_text = self.score_font.render(f" Score: {self.score}", True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(self.width // 2, 66))
            self.screen.blit(score_text, score_rect)

            high_score_text = self.score_font.render(f"High Score: {self.high_score}", True, (255, 255, 255))
            high_score_rect = high_score_text.get_rect(center=(self.width // 2, 506))
            self.screen.blit(high_score_text, high_score_rect)

    def score_update(self) -> None:
        # Update the score if the bird passes through pipes
        if self.pipes.pipes:
            for pipe in self.pipes.pipes:
                if 65 < pipe.centerx < 69 and self.score_time:
                    self.score += 1
                    self.score_time = False
                    self.score_sound.play()  # Play score sound
                if pipe.left <= 0:
                    self.score_time = True

        if self.score > self.high_score:
            self.high_score = self.score

    def run(self) -> None:
        # Main game loop
        running = True
        while running:
            self.clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.game_over:
                        self.bird.flap()

                    if event.key == pygame.K_SPACE and self.game_over:
                        self.game_over = False
                        self.pipes.pipes = []
                        self.bird.reset()
                        self.score_time = True
                        self.score = 0
                        

                if event.type == self.bird.bird_flap:
                    self.bird.animate()

                if event.type == self.pipes.create_pipe:
                    self.pipes.add_pipe()

            self.screen.blit(self.back_img, (0, 0))
            self.screen.blit(self.floor_img, (self.floor_x, 550))

            if not self.game_over:
                if self.bird.bird_rect.top <= 0 or self.bird.bird_rect.bottom >= 550:
                    self.game_over = True
                    self.background_music.stop()   # Pause background music
                    self.game_over_sound.play()  # Play game over sound
                    
                    pygame.time.wait(int(self.game_over_sound.get_length())*1000)
                    self.background_music.play(loops=-1)
                    continue
                self.bird.update()
                self.bird.draw(self.screen)
                self.pipes.draw(self.screen)
                self.game_over = self.pipes.update(self.bird.bird_rect)

                if self.game_over:
                    self.background_music.stop()   # Pause background music
                    self.game_over_sound.play()  # Play game over sound
                    pygame.time.wait(int(self.game_over_sound.get_length())*1000)
                    self.background_music.play(loops=-1)
                self.score_update()
                self.draw_score("game_on")
            else:
                self.screen.blit(self.over_img, self.over_rect)
                self.draw_score("game_over")
                #print("game over")

            self.floor_x -= 1
            if self.floor_x < -448:
                self.floor_x = 0

            self.draw_floor()
            pygame.display.update()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
