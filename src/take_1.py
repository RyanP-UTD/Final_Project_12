import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((900, 700))
    pygame.display.set_caption("Bug Swatter")

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
