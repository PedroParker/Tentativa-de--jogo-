class Text:
    def __init__(self, text, pos, settings):
        self.pos = pos
        self.text = text
        self.text_surface = settings.base_font.render(self.text, True, settings.get_color("black"))

# Methods ---------------------------------------------------------------------

    def draw(self, screen):
        screen.blit(self.text_surface, self.pos)
