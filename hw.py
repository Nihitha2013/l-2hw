import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")

bg = pygame.transform.scale(
    pygame.image.load("pngtree-cartoon-illustration-of-a-young-gamer-playing-video-games-on-a-picture-image_5581641.jpg").convert(),
    (300, 300)
)

col = pygame.Color("white")

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(col)
    screen.blit(bg, (100, 100)) 
    pygame.draw.rect(screen, "yellow", pygame.Rect(100, 410, 300, 20)) 
    pygame.display.flip()

pygame.quit()