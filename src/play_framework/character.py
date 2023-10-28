import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, states: dict[str, pygame.Surface]):
        super().__init__()

        self.states = states
        self._current_state = [*states][0]
        self.image = states[self._current_state]
        self.rect = self.image.get_rect()

    def _update_image(self, state: str):
        self.image = self.states[state]
        self.rect = self.image.get_rect()

    def get_state(self):
        """
        Get the current state of the character.
        """
        return self._current_state

    def set_state(self, state: str):
        """
        Set the current state of the character.
        """

        if state not in self.states:
            raise ValueError(f"State {repr(state)} does not exist")

        self._current_state = state
        self._update_image(state)
