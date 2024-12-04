import pygame
import os

class Red_box_Mechanics:
    def __init__(self, x, y, width, height, color):
        self.rectangle = pygame.Rect(x, y, width, height)
        self.color = color
        self.active = True # Makes red box active

    def draw(self, surface):
        if self.active:
            pygame.draw.rect(surface, self.color, self.rectangle)

    def check_click(self, mouse_pos):
        if self.active and self.rectangle.collidepoint(mouse_pos):
            print("The Red box is clicked")
            self.active = False # once clicked, set to inactive
            return True
        return False

def main():
    pygame.init()

    screen = pygame.display.set_mode((900, 700))
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
    red_box_color = 'Red'
    red_box_size = (50, 60)
    red_box_x = (900 - red_box_size[0]) // 2
    red_box_y = (700 - red_box_size[1]) // 2
    red_box = Red_box_Mechanics(red_box_x, red_box_y, * red_box_size, red_box_color)

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
 