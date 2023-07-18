import pygame

pygame.init()

# 音を再生する関数
def play_sound(sound_path):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(sound_path)
    sound.play()

# 使用例
play_sound('bigdice_single.wav')
