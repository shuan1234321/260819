import sys
import random
import pygame

WIDTH, HEIGHT = 640, 480
FPS = 60

MENU = ["TIMING GAME", "TYPING GAME", "CALCULATOR GAME", "EXIT"]

def print_menu(screen, font, selected):
    for i, item in enumerate(MENU):
        if i == selected:
            text = "> " + item
        else:
            text = "  " + item
        screen.blit(font.render(text, True, (255, 255, 255)), (100, 50 + 50 * i))

def main() -> None:
    pygame.init()
    font = pygame.font.SysFont(None, 36)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("NEW GAME")
    clock = pygame.time.Clock()

    selected = 0
    mode = "menu"
    go_time = 0
    start_time = 0
    result = 0
    exit_time = 0

    running = True
    while running:
        now = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if mode == "menu":
                    if event.key == pygame.K_UP:
                        if selected > 0:
                            selected = selected - 1
                    elif event.key == pygame.K_DOWN:
                        if selected < len(MENU) - 1:
                            selected = selected + 1
                    elif event.key == pygame.K_RETURN:
                        if MENU[selected] == "TIMING GAME":
                            mode = "wait"
                            go_time = now + random.randint(2000, 5000)
                        elif MENU[selected] == "EXIT":
                            mode = "exit"
                            exit_time = now

                elif mode == "wait":
                    if event.key == pygame.K_SPACE:
                        mode = "too_early"

                elif mode == "press":
                    if event.key == pygame.K_SPACE:
                        result = now - start_time
                        mode = "result"

                elif mode == "result" or mode == "too_early":
                    if event.key == pygame.K_r:
                        mode = "wait"
                        go_time = now + random.randint(2000, 5000)
                    elif event.key == pygame.K_e:
                        mode = "exit"
                        exit_time = now

        if mode == "wait" and now >= go_time:
            mode = "press"
            start_time = now

        if mode == "exit" and now - exit_time >= 1500:
            running = False

        screen.fill((30, 32, 40))

        if mode == "menu":
            print_menu(screen, font, selected)
        elif mode == "press":
            screen.blit(font.render("PRESS BUTTON!", True, (255, 255, 255)), (260, 200))
        elif mode == "wait":
            screen.blit(font.render("WAIT!", True, (255, 255, 255)), (260, 200))
        elif mode == "exit":
            screen.blit(font.render("BYE BYE!", True, (255, 255, 255)), (260, 200))
        elif mode == "result":
            screen.blit(font.render(str(result) + " ms", True, (255, 255, 255)), (260, 200))
            screen.blit(font.render("R: restart  /  E: exit", True, (150, 150, 150)), (200, 260))
        elif mode == "too_early":
            screen.blit(font.render("TOO EARLY!", True, (255, 255, 255)), (260, 200))
            screen.blit(font.render("R: restart  /  E: exit", True, (150, 150, 150)), (200, 260))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()