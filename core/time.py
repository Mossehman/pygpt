import pygame
from utility.singleton import Singleton

class Time:

    __clock = pygame.time.Clock()
    __dt = 0
    __elapsed_time = 0

    @staticmethod
    def run():
        Time.__dt = min(Time.__clock.tick(60) / 1000, 0.05)
        Time.__elapsed_time += Time.__dt
    
    @staticmethod
    def get_deltatime():
        return Time.__dt
    @staticmethod
    def get_elapsedtime():
        return Time.__elapsed_time

    

    
    
