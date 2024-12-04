import pygame
import os
import random

class Red_box_Mechanics:
    def __init__(self, x, y, width, height, color, screen_width, screen_height):
        self.rectangle = pygame.Rect(x, y, width, height)
        self.color = color
        self.active = True # Makes red box active
        self.click_time = 0 # Time when clicked
        self.reset_time = 500 # Time until reset
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw(self, surface):
        if self.active:
            pygame.draw.rect(surface, self.color, self.rectangle)


    def check_click(self, mouse_pos):
        if self.active and self.rectangle.collidepoint(mouse_pos):
            print("The Red box is clicked")
            self.active = False # once clicked, set to inactive
            self.click_time = pygame.time.get_ticks()
            return True
        return False  

    def update(self):
        if not self.active and (pygame.time.get_ticks() - self.click_time) > self.reset_time:
            self.active = True # Make sure to reactivate the box

class AnimationMechanics:
    def __init__(self, red_box, width, height, screen_width, screen_height):
        self.red_box = red_box
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.fly_timer = 0
        self.fly_interval = 200

    def teleport(self):
        update_x = random.randint(50, self.screen_width - self.width - 50)
        update_y = random.randint(50, self.screen_height - self.height - 50)
        self.red_box.rectangle.topleft = (update_x, update_y)

    def fly(self):
        offset = 25 # the range within the red box

        if self.red_box.active:
            current_time = pygame.time.get_ticks()
            if current_time - self.fly_timer > self.fly_interval:
                fly_within_x = random.randint(-offset, offset)
                fly_within_y = random.randint(-offset, offset)
                self.red_box.rectangle.x += fly_within_x
                self.red_box.rectangle.y += fly_within_y
                self.fly_timer = current_time #reset the timer after the operaion completes. 
                self.red_box.rectangle.x = max(60, min(self.red_box.rectangle.x, self.red_box.screen_width - self.red_box.rectangle.width - 50))
                self.red_box.rectangle.y = max(80, min(self.red_box.rectangle.y, self.red_box.screen_height - self.red_box.rectangle.height - 50))



def main():
    pygame.init()

    screen_width = 900
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Bug Swatter")

    # Title
    pygame.font.init()
    font = pygame.font.Font(None, 48)
    title_text = font.render("Bug Swatter", True, ('White'))
    title_rectangle = title_text.get_rect(center = (450, 40))

    # Score Indicator
    score_count = 0
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(f"Score: {score_count}", True, ('White'))
    score_rectangle = score_text.get_rect(center=(750, 95))

    # border line
    border_color = 'White'
    border_thickness = 4
    border_rectangle = pygame.Rect(50, 70, 800, 600) # should posit 40 by 70px and the rect by 800 by 600px

    # red box
    red_box_color = 'Black'
    red_box_size = (30, 40)
    red_box_x = (900 - red_box_size[0]) // 2
    red_box_y = (700 - red_box_size[1]) // 2
    red_box = Red_box_Mechanics(red_box_x, red_box_y, * red_box_size, red_box_color, screen_width, screen_height)

    # New class function: Animation Mechanics
    animation_mechanics = AnimationMechanics(red_box, red_box.rectangle.width, red_box.rectangle.height, screen_width, screen_height)

    # Pull Image
    image_path = os.path.join('..', 'docs', 'Bug.png')
    image = pygame.image.load(image_path) #Should load an image
    image = pygame.transform.scale(image, red_box_size)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left mouse button
                    mouse_pos = event.pos
                    if red_box.check_click(mouse_pos):
                        score_count += 1
                        score_text = score_font.render(f"Score: {score_count}", True, ('White'))
                        animation_mechanics.teleport()

        red_box.update()
        animation_mechanics.fly()

        screen.fill('Black')

        pygame.draw.rect(screen, border_color, border_rectangle, border_thickness)

        screen.blit(title_text, title_rectangle)

        red_box.draw(screen)

        if red_box.active:
            screen.blit(image, red_box.rectangle.topleft)

        #screen.blit(image, red_box.rectangle.topleft)

        screen.blit(score_text, score_rectangle)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
 