import sys, pygame

size = width, height = 800, 600


class Ball(object):
    def __init__(self):
        self.velocity = [1, 1]
        self.rect = pygame.Rect((100, 50), (50, 50))
        self.surface = pygame.Surface((self.rect.width, self.rect.height))

    def move(self, delta):
        self.rect = self.rect.move(self.velocity[0]*delta, self.velocity[1]*delta)


def update(ball, delta, sound):
    ball.move(delta)
    if ball.rect.left < 0 or ball.rect.right > width:
        ball.velocity[0] = ball.velocity[0]*-1
        sound.play()
    if ball.rect.top < 0 or ball.rect.bottom > height:
        ball.velocity[1] = ball.velocity[1]*-1
        sound.play()


def show(screen, ball):
    screen.fill((0, 0, 50))
    screen.blit(ball.surface, ball.rect)
    pygame.display.flip()

def main():

    pygame.init()
    pygame.display.set_caption("balls lol")

    screen = pygame.display.set_mode((width, height))

    clock = pygame.time.Clock()

    sound = pygame.mixer.Sound("OBAMNA.mp3")

    ball = Ball()
    pygame.draw.circle(ball.surface, (255, 255, 255), (25, 25), 25)

    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        delta = clock.get_time()
        update(ball, delta, sound)
        show(screen, ball)


if __name__ == "__main__":
    main()
