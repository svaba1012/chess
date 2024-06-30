import pygame as pg

def mouseClicked(first):
    mP = pg.mouse.get_pressed()[0]
    if mP and first:
        first = False
        return True, first
    elif not mP:
        first = True
        return False, first
    else:
        return False, False

class button:
    def __init__(self, x, y, width, height, color, string, fontSize, textC):
        font = pg.font.Font('freesansbold.ttf', fontSize)
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        text = font.render(string, True, textC, self.color)
        textRect = text.get_rect()
        textRect.center = (x + width // 2, y + height // 2)
        self.text = text
        self.textRect = textRect

    def crtaj(self, surface):
        pg.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        surface.blit(self.text, self.textRect)
        
    def buttonFunc(self, func):
        #clicked, prvi = mouseClicked(prvi)
        clicked = pg.mouse.get_pressed()[0]
        if clicked:
            mPos = pg.mouse.get_pos()
            if mPos[0] > self.x and mPos[0] < self.x + self.width and mPos[1] > self.y and mPos[1] < self.y + self.height:
                r = func()
                return r
        return None


