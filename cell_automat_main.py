import pygame
import pygame_gui
##################
import gui

pygame.init()

infoObject = pygame.display.Info()
window_width = infoObject.current_w#1920
window_height = infoObject.current_h#1080
screen = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)

pygame.display.set_caption('cell_automat')

manager = pygame_gui.UIManager((window_width, window_height))

#gui#
button = gui.Button(0, 0, 150, 50, 'text', manager)

clock = pygame.time.Clock()
##
running = True
while running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        ##
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        ##
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == button.button:
                running = False
        manager.process_events(event)

    manager.update(time_delta)
    screen.fill((0, 0, 0))
    manager.draw_ui(screen)

    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(2, 50, 50, 40), 3)
    pygame.display.update()












