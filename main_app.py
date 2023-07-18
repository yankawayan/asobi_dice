"""

"""
import pygame


# 初期化
pygame.init()

# MP3ファイルのパス
mp3_file = 'bigdice_single.mp3'
wav_file = 'bigdice_single.wav'

# 音楽を再生するための準備
pygame.mixer.init()
# pygame.mixer.music.load(mp3_file)
pygame.mixer.music.load(wav_file)

# 音楽再生
pygame.mixer.music.play()

# 音楽再生中はプログラムが終了しないようにする
while pygame.mixer.music.get_busy():
    continue

# 終了処理
pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()
