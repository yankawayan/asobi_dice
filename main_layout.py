import pygame
import numpy as np
import sys
from main_sound_controller import SoundController

# ウィンドウのサイズ
WIDTH = 800
HEIGHT = 600

# 色の定義
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

# 初期化
pygame.init()

# ウィンドウの作成
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My App")

clock = pygame.time.Clock()

dice_sound = SoundController('bigdice_single.wav') 
button_sound = SoundController('push_button.wav')

# 正六面体の頂点の座標（正規化された立方体の座標）
cube_vertices = np.array([
    [-0.5, -0.5, -0.5],
    [0.5, -0.5, -0.5],
    [0.5, 0.5, -0.5],
    [-0.5, 0.5, -0.5],
    [-0.5, -0.5, 0.5],
    [0.5, -0.5, 0.5],
    [0.5, 0.5, 0.5],
    [-0.5, 0.5, 0.5]
])

# 正六面体の辺を表すインデックス
cube_edges = [(0, 1), (1, 2), (2, 3), (3, 0),
              (0, 4), (1, 5), (2, 6), (3, 7),
              (4, 5), (5, 6), (6, 7), (7, 4)]

# 正六面体の面を表すインデックス
cube_faces = [(0, 1, 2, 3),  # 下面（青）
              (4, 5, 6, 7),  # 上面（緑）
              (0, 1, 5, 4),  # 側面1（赤）
              (1, 2, 6, 5),  # 側面2（黄）
              (2, 3, 7, 6),  # 側面3（オレンジ）
              (0, 3, 7, 4)]  # 側面4（紫）

dice_markers_coordinate = [[()],                   #1
                           [(),()],                #2
                           [(),(),()],             #3
                           [(),(),(),()],          #4
                           [(),(),(),(),()],       #5
                           [(),(),(),(),(),()]]    #6

# 各面の色を指定
colors = [(0, 0, 255),  # 青
          (0, 255, 0),  # 緑
          (255, 0, 0),  # 赤
          (255, 255, 0),  # 黄
          (255, 165, 0),  # オレンジ
          (128, 0, 128)]  # 紫

# 回転行列を計算する関数
def rotate_3d_point(point, angle_x, angle_y, angle_z):
    rotation_x = np.array([[1, 0, 0],
                           [0, np.cos(angle_x), -np.sin(angle_x)],
                           [0, np.sin(angle_x), np.cos(angle_x)]])
    rotation_y = np.array([[np.cos(angle_y), 0, np.sin(angle_y)],
                           [0, 1, 0],
                           [-np.sin(angle_y), 0, np.cos(angle_y)]])
    rotation_z = np.array([[np.cos(angle_z), -np.sin(angle_z), 0],
                           [np.sin(angle_z), np.cos(angle_z), 0],
                           [0, 0, 1]])
    return rotation_z @ rotation_y @ rotation_x @ point

angle_x = 0
angle_y = 0
angle_z = 0

# メインループ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONUP:
            #左クリック
            if event.button == 1: 
                button_sound.play(1)
                dice_sound.play(0)

    # 背景を描画
    window.fill(WHITE)

    # ヘッダーを描画
    header_rect = pygame.Rect(0, 0, WIDTH, 80)
    pygame.draw.rect(window, GRAY, header_rect)

    # ボディーを描画
    body_rect = pygame.Rect(0, 80, WIDTH, HEIGHT - 200)
    pygame.draw.rect(window, WHITE, body_rect)

    # テキストボックスを描画
    textbox_rect = pygame.Rect(50, 150, 200, 30)
    pygame.draw.rect(window, WHITE, textbox_rect)
    pygame.draw.rect(window, BLACK, textbox_rect, 2)

    # ボタンを描画
    button_rect = pygame.Rect(300, 150, 100, 30)
    pygame.draw.rect(window, GRAY, button_rect)
    pygame.draw.rect(window, BLACK, button_rect, 2)

    # フッダーを描画
    footer_rect = pygame.Rect(0, HEIGHT - 120, WIDTH, 120)
    pygame.draw.rect(window, GRAY, footer_rect)

    # テキストを描画
    font = pygame.font.Font(None, 24)
    text = font.render("Welcome to My App", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, 40))
    window.blit(text, text_rect)

    # 正六面体を回転させる
    angle_x += 0.05
    angle_y += 0.05
    angle_z += 0.05

    rotated_vertices = [rotate_3d_point(vertex, angle_x, angle_y, angle_z) for vertex in cube_vertices]
    
    # # 正六面体を描画
    # for edge in cube_edges:
    #     point1 = (rotated_vertices[edge[0]][0] * 100 + WIDTH // 2, rotated_vertices[edge[0]][1] * 100 + HEIGHT // 2)
    #     point2 = (rotated_vertices[edge[1]][0] * 100 + WIDTH // 2, rotated_vertices[edge[1]][1] * 100 + HEIGHT // 2)
    #     pygame.draw.line(window, (0, 0, 0), point1, point2, 3)

    # 正六面体の各面を描画
    for face_index, face in enumerate(cube_faces):
        points = [(rotated_vertices[i][0] * 100 + WIDTH // 2, rotated_vertices[i][1] * 100 + HEIGHT // 2) for i in face]
        pygame.draw.polygon(window, colors[face_index], points)

    pygame.display.update()
    clock.tick(60)