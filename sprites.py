import pygame
from config import *
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.hit_rect = CAR_HIT_BOX
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.rot = 90

    def get_keys(self):
        self.rot_speed = 0
        self.vel = vec(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rot_speed = CAR_ROTATION_SPEED
        if keys[pygame.K_RIGHT]:
            self.rot_speed = -CAR_ROTATION_SPEED
        if keys[pygame.K_UP]:
            self.vel = vec(CAR_SPEED, 0).rotate(-self.rot)
        if keys[pygame.K_DOWN]:
            self.vel = vec(-CAR_SPEED / 2, 0).rotate(-self.rot)


    def update(self):
        self.get_keys()
        self.pos += self.vel
        self.rot = (self.rot + self.rot_speed) % 360
        self.image = pygame.transform.rotate(self.game.player_img, self.rot+270)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.hit_rect.centerx = self.pos.x
        self.hit_rect.centery = self.pos.y
