import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((900, 700))
    pygame.display.set_caption("Bug Swatter")

    # border line
    border_color = ('White')
    border_thickness = 4
    border_rectangle = pygame.Rect(50, 70, 800, 600) # should posit 40 by 70px and the rect by 800 by 600px

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill('Black')
        
        pygame.draw.rect(screen, border_color, border_rectangle, border_thickness)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
