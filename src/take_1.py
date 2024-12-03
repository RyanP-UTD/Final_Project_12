import pygame
import os

def main():
    pygame.init()

    screen = pygame.display.set_mode((900, 700))
    pygame.display.set_caption("Bug Swatter")

    # Title
    pygame.font.init()
    font = pygame.font.Font(None, 48)
    title_text = font.render("Bug Swatter", True, ('White'))
    title_rectangle = title_text.get_rect(center = (450, 40))

    # border line
    border_color = 'White'
    border_thickness = 4
    border_rectangle = pygame.Rect(50, 70, 800, 600) # should posit 40 by 70px and the rect by 800 by 600px

    # red box
    red_box_color = 'Red'
    red_box_size = (50, 60)
    red_box_x = (900 - red_box_size[0]) // 2
    red_box_y = (700 - red_box_size[0]) // 2
    red_box = pygame.Rect(red_box_x, red_box_y, * red_box_size)

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

        screen.fill('Black')

        pygame.draw.rect(screen, border_color, border_rectangle, border_thickness)

        screen.blit(title_text, title_rectangle)

        pygame.draw.rect(screen, red_box_color, red_box)

        screen.blit(image, red_box.topleft)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
