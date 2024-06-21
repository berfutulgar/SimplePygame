import pygame 
import sys #pygame'den çıkarken python'un düzgün kapanmasını sağlar

pygame.init()

size = (400, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Simple Pygame Example")

# Define initial position and size of the rectangle
rect_x = 150
rect_y = 100
rect_width = 100
rect_height = 50
rect_speed = 0.01  # Speed of the rectangle

#main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Get pressed keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    if rect_x < 0 or rect_x + rect_width > size[0] or rect_y < 0 or rect_y + rect_height > size[1]:
        running = False  # End the game if the rectangle hits the boundary


    screen.fill((157, 36, 253))
    
    pygame.draw.rect(screen, (157, 227, 253), (rect_x, rect_y, rect_width, rect_height)) 
    pygame.display.flip()

pygame.quit()
sys.exit()