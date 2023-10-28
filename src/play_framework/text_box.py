import pygame


class TextBox(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text="", input=False):
        super().__init__()
        self.image = pygame.Surface((width, height)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.font = pygame.font.Font(None, 32)
        self.input = input
        self._text = text

    def _render_text(self):
        if not self.image:
            raise ValueError("Image is not set")

        self.image.fill((0, 0, 0, 0))
        text_surface = self.font.render(self._text, True, (0, 0, 0))

        text_rect = text_surface.get_rect(center=self.image.get_rect().center)
        self.image.blit(text_surface, text_rect)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self._render_text()

    def update(self, event):
        self._render_text()
