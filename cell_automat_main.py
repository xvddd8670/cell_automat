import pygame
import pygame_gui
##################
import gui
import cell
#init
pygame.init()

infoObject = pygame.display.Info()
window_width = infoObject.current_w#1920
window_height = infoObject.current_h#1080
screen = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
pygame.display.set_caption('cell_automat')
manager = pygame_gui.UIManager((window_width, window_height))

#gui#
button = gui.Button(0, 0, 150, 50, 'text', manager)

#objects
#create cells list
size_x = 100
size_y = 100
cells_list = []
i_in_while = 0
while i_in_while < size_x:
    j_in_while = 0
    cells_y = []
    while j_in_while < size_y:
        cells_y.append(cell.Cell(i_in_while, j_in_while))
        j_in_while += 1
    cells_list.append(cells_y)
    del(cells_y)
    i_in_while += 1

#main while 
clock = pygame.time.Clock()
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

    #pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(2, 50, 50, 40), 3)
    for cells_block in cells_list:
        for cell_ in cells_block:
            cell_.render(screen)

    pygame.display.update()












