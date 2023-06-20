import pygame
import sys

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

# メインループ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

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

    pygame.display.update()
    clock.tick(60)
