import pygame as pg

from pygame.transform import *
from AnimationSprite import Explosions

class Settings():
	"""A class to store all settings for game"""
	def __init__(self):
		"""Initialize the class"""
		self.windowCaption = 'PROMETA INVADER'
		self.screenWidth = 1280
		self.screenHeight = 720
		self.bgColor = (20, 20, 20)
		img = pg.image.load('gfx/background.png')
		img = scale(img, (1280, 720))
		self.bg = img

		#Image
		self.shipImage1 = pg.image.load('gfx/ship2.png')
		self.shipImage2 = rotate(self.shipImage1, -10)
		self.shipImage3 = rotate(self.shipImage1, 10)

		self.alienImage1 = pg.image.load('gfx/mob.png')

		self.explosionEffect = Explosions

		#Sound
		self.menuMusic = pg.mixer.music.load('res/Test.mp3')

		self.backgroundMusic = pg.mixer.music.load('res/Test.mp3')
		self.bulletSound = pg.mixer.Sound('res/ThrowingFireball.wav')
		self.enemyExplodeSound = pg.mixer.Sound('res/Coin.wav')

		#Ships speed
		self.shipLimit = 3

		#Bullet settings
		self.bulletWidth = 3
		self.bulletHeight = 15
		self.bulletColor = (60, 60, 60)

		#Alien settings

		#How quickly the game speeds up
		self.speedUp = 2
		self.scoreSpeedUp = 1.5

		self.initDynamicSettings()

	def initDynamicSettings(self):
		self.shipSpeed = 10
		self.bulletSpeed = 10
		self.alienSpeed = 5
		self.fleetDropSpeed = 3
		self.fleetDir = 1
		self.alienPoints = 50

	def increaseSpeed(self):
		"""Increase the speed settings"""
		#self.shipSpeed *= self.speedUp
		#self.bulletSpeed *= self.speedUp
		if self.alienSpeed <= 1.5:
			self.alienSpeed *= self.speedUp
			self.fleetDropSpeed *= self.speedUp
		self.alienPoints = int(self.alienPoints * self.scoreSpeedUp)