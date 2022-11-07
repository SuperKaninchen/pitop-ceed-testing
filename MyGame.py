import sys, pygame

size = width, height = 800, 600


class Ball(object):
    def __init__(self):
        self.count = 0
        self.velocity = [100, 86]
        self.rect = pygame.Rect((100, 50), (50, 50))
        self.surface = pygame.Surface((self.rect.width, self.rect.height))

    def move(self, delta):
        self.rect = self.rect.move(int(self.velocity[0]/delta), int(self.velocity[1]/delta))


def update(ball, delta, sound):
    ball.move(delta)
    if ball.rect.left < 0 or ball.rect.right > width:
        ball.velocity[0] = ball.velocity[0]*-1
        sound.play()
        ball.count += 1
    if ball.rect.top < 0 or ball.rect.bottom > height:
        ball.velocity[1] = ball.velocity[1]*-1
        sound.play()
        ball.count += 1


def show(screen, ball, font):
    screen.fill((0, 0, 0))
    screen.blit(ball.surface, ball.rect)
    screen.blit(font, (32, 32))
    pygame.display.flip()

def main():

    pygame.init()
    pygame.display.set_caption("balls lol")

    screen = pygame.display.set_mode((width, height))

    clock = pygame.time.Clock()

    sound = pygame.mixer.Sound("button-6.wav")

    font = pygame.font.Font(None, 32)

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

        font_surface = font.render(f"Hits: {ball.count}", True, (255, 255, 255))
        show(screen, ball, font_surface)


if __name__ == "__main__":
    main()
