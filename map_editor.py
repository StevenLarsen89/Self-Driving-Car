import pygame
from config import *

pygame.init()
file = open('level.txt', 'w')
size = WIDTH, HEIGHT
window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption( "Race-AI map editor" )

clock = pygame.time.Clock()
fps = 60
to_draw = []
current_color = 0


draw_start = False


font = pygame.font.Font(None, 36)
def show_text(msg ,color, x, y):
    text = font.render(msg, True, color)
    textpos = (x, y)
    window.blit(text, textpos)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = mouse_pos
            draw_start = True

        if event.type == pygame.MOUSEBUTTONUP:
            final_pos = mouse_pos
            draw_start = False

            #rect = pygame.Rect(pos,(final_pos[0]- pos[0], final_pos[1]-pos[1]))
            #rect.normalize()
            to_draw += [(pos, final_pos)]

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_RETURN:
                for i in range(0, len(to_draw)):
                    print("[" + str(to_draw[i]) + ", BLACK],")
                    file.write("[" + str(to_draw[i]) + ", BLACK]\n")

            if event.key == pygame.K_BACKSPACE:
                to_draw.pop()

    window.fill(WHITE)
    pygame.draw.rect(window, GREEN, pygame.Rect(WIDTH * 0.1 - CAR_WIDTH, HEIGHT / 2 - CAR_HEIGHT, 100, 100))

    # show line when mouse button down
    if draw_start:
        pygame.draw.line(window, BLACK, pos, mouse_pos, 4)

    # draws all saved lines permanently
    for i in range(0, len(to_draw)):
            pygame.draw.line(window, BLACK, to_draw[i][0], to_draw[i][1], 4)



    # show_text("x:", BLACK, 1070, 0)
    # show_text(str(mouse_x), BLACK, 1100, 0)
    # show_text("y:", BLACK, 1170, 0)
    # show_text(str(mouse_y), BLACK, 1200, 0)

    pygame.display.update()
    clock.tick(fps)

file.close()
pygame.quit()