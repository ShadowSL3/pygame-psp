__author__ = "Francesco aulicino, <outfrancesco51@gmail.com>"


import pygame, sys, time, threading


pygame.init() 
pygame.display.set_caption("PSP-Pygame")
pygame.key.set_repeat(1, 1)


def Color(*args):
    # TODO:  this should be a class w/ rw attrs red, gree, blue, alpha 
    return args 


class Controller: 
    """ Mapping Controller PSP
    
    TRIANGLE: keypad x
    Square: keypad x
    TRIANGLE: keypad x
    """

    def __init__(self, grab=False):
        if grab:
            pygame.event.set_grab(True)
            pygame.mouse.set_visible(True)
        else:
            pygame.event.set_grab(False)
            pygame.mouse.set_visible(False)
        self._key = [0] * 323
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._key = pygame.key.get_pressed()
            if self._key[pygame.K_F4]:
                sys.exit()
    @property
    def circle(self):
        return self._key[pygame.K_x]
    @property
    def xcross(self):
        return self._key[pygame.K_z]
    
    @property
    def triangle(self):
        return self._key[pygame.K_s]
    
    @property
    def square(self):
        return self._key[pygame.K_a]
    
    @property
    def l(self):
        return self._key[pygame.K_q]
    
    @property
    def r(self):
        return self._key[pygame.K_w]
    
    @property
    def start(self):
        return self._key[pygame.K_v]
    
    @property
    def select(self):
        return self._key[pygame.K_c]
    
    @property
    def left(self):
        return self._key[pygame.K_LEFT]
    
    @property
    def right(self):
        return self._key[pygame.K_RIGHT]
    @property
    def up(self):
        return self._key[pygame.K_UP]
    
    @property
    def down(self):
        return self._key[pygame.K_DOWN]
    @property
    def triangle(self):
        return self._key[pygame.K_x]
    
    @property
    def AnalogicX(self):
        x_pos = pygame.mouse.get_pos[0] * 256 / 480 - 127
        return 0
    @property
    def AnalogicY(self):
        y_pos = pygame.mouse.get_pos[1] * 256 / 272 - 127
        return 1
    
class Image (pygame.Surface):
    def __init__(self, *args):
        if len(args) == 2:
            pygame.Surface.__init__(self, (args[1], pygame.SRCALPHA, 32))
            self.set_alpha(255)
        else:
            if type(args[0]) is Image:
                surf = args[0]
            else:
                surf = pygame.image.load(args[0])
                pygame.Surface.__init__(self, (surf.get_width(), surf.get_height()), pygame.SRCALPHA, 32)
                self.blit(surf, surf.get_rect())

        def clear(self, color):
            self.fill(color)

        def blit_to_screen(self,  src, sx=0, sy = 0, w=-1, h = -1,  dx= 0, dy = 0, blend = False):
            # TODO: Implement Alpha
            if type(dx) is float:
                print ("dx is float, should be integer")
            if type(dy) is float:
                print ("dx is float, should be integer")
            
            if type(sx) is tuple:
                pygame.Surface.blit(self, src, sx)
                return 
            if dx == -1:
                dx = src.get_rect()[0]

            if dy == -1:
                dy = src.get_rect()[1]

            if type(sx) is int:
                if w == -1: w = src.width
                if h == -1: h = src.height
                tmp = src.subsurface(sx, sy, w, h)
                pygame.Surface.blit(self, tmp, (dx, dy))
                return 
            pygame.Surface.blit(self, src, (dx, dy))

        def fillRect(self, x, y, w, h, color):
            pass
    def saveToFile(self, filename):
        pygame.image.save(self, filename)

    @property
    def width(self):
        rect = self.get_rect()
        return rect[2] - rect[0]
    @property
    def height(self):
        rect = self.get_rect()
        return rect[3] - rect[1]
    
class Screen:
    def __init__(self, width=482, height=272):
        self._screen = pygame.display.set_mode((width, height))
def blit (self, img, sx=0, sy=0, sw=-1, sh=-1, dx=-1, dy=-1, blend=False, dw=-1, dh=-1):
            dx, dy = sx
            rect = img.get_rect()
            h = rect[3] - rect[1]
            w = rect[2] - rect[0]
            if sw == -1: sw = w
            if sh == -1: sh = h
            if dx == -1: dx = rect[0]
            if dy == -1: dy = rect[1]
            if dw == -1: dw = w
            if dh == -1: dh = h
            tmp = img.subsurface(sx, sy, sw, sh)
            if dw != w or dh != h:
             tmp = pygame.transform.scale(tmp, (dw, dh))
            self._screen.blit(tmp, (dx, dy))
def swap(self):
    pygame.display.flip()
    pygame.event.pump()

def clear_screen(self, color):
    self._screen.fill(color)

def fillRect(self, x, y, w, h, color): 
    self._screen.fill((x, y, w, h), color) 

def saveToFile(self, filename):
    surf = pygame.display.get_surface()
    pygame.image.save(surf, filename)

@property
def width(self):
    rect = self._screen.get_rect()
    return rect[2] - rect[0]
@property
def height(self):
    rect = self._screen.get_rect()
    return rect[3] - rect[0]


class Transform:
    T_Plus = TR_MULT = range(0, 2)

    def __init__(self, type, praram=None):
        pass

    def apply():
        pass
