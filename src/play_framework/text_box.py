import pygame


class TextBox(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text=""):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.font = pygame.font.Font(None, 32)
        self.text = text
        self.render_text()

    def render_text(self):
        text_surface = self.font.render(self.text, True, (0, 0, 0))

        if not self.image:
            raise ValueError("Image is not set")

        text_rect = text_surface.get_rect(center=self.image.get_rect().center)
        self.image.blit(text_surface, text_rect)

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.render_text()
