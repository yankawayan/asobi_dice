import pygame

diceroll_sound_path = 'bigdice_single.mp3'
buttonpush_sound_path = 'push_button.mp3'

class SoundController:
    def __init__(self, sound_path):
        self.sound_path = sound_path

    def play(self, channel_num):
        sound = pygame.mixer.Sound(self.sound_path)
        pygame.mixer.Channel(channel_num).play(sound)

    def stop(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

pygame.init()
pygame.mixer.init()

sound1 = SoundController(diceroll_sound_path)
sound2 = SoundController(buttonpush_sound_path)
sound1.play(0)
sound2.play(1)
