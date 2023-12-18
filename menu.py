import pygame
import sys
from game import TreasureMazeGame

# Khởi tạo Pygame
pygame.init()

# Cài đặt cửa sổ
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Tải background
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (width, height))

# Tải font mới
font = pygame.font.Font("Roboto-Medium.ttf", 38)
title_font = pygame.font.Font("FzHalloweenMorning.ttf", 72)

# Cài đặt tiêu đề của cửa sổ
pygame.display.set_caption("Treasure Maze")

# Cài đặt màu sắc
white = (255, 255, 255)
red = (255, 0, 0)

# Hàm vẽ nút
def draw_button(x, y, width, height, color, text):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

# Hàm vẽ tiêu đề
def draw_title():
    title_surface = title_font.render("Treasure Maze", True, red)
    title_rect = title_surface.get_rect(center=(width // 2, 100))
    screen.blit(title_surface, title_rect)

# Biến để kiểm soát màn hình
in_menu = True

# Khai báo biến buttons ở đây
buttons = [
    {"rect": pygame.Rect(width // 2 - 100, height // 2 - 150, 200, 50), "text": "Chơi"},
    {"rect": pygame.Rect(width // 2 - 100, height // 2 - 50, 200, 50), "text": "Hướng dẫn"},
    {"rect": pygame.Rect(width // 2 - 100, height // 2 + 50, 200, 50), "text": "Thoát"},
]

# Tạo đối tượng game từ lớp TreasureMazeGame
game = TreasureMazeGame()

# Vòng lặp chính
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if in_menu:
                # Kiểm tra xem người chơi có nhấn vào nút nào không
                for button in buttons:
                    if button["rect"].collidepoint(pygame.mouse.get_pos()):
                        if button["text"] == "Chơi":
                            in_menu = False
                            game.reset_game()  # Thêm hàm reset_game để khởi tạo lại trò chơi
            else:
                # Kiểm tra xem người chơi có nhấn vào nút "Exit" trong trò chơi hay không
                if game.game_over:
                    in_menu = True
                    game.game_over = False  # Đặt lại trạng thái game_over khi quay lại menu

    # Hiển thị background
    screen.blit(background, (0, 0))

    # Vẽ tiêu đề
    draw_title()

    if in_menu:
        # Vẽ các nút trên màn hình menu
        for button in buttons:
            draw_button(button["rect"].x, button["rect"].y, button["rect"].width, button["rect"].height, red, button["text"])
    else:
        # Màn hình chơi game (ở đây chỉ là màn hình trắng)
        pygame.draw.rect(screen, red, (100, 100, 600, 400))
        
        # Gọi phương thức run_game() từ đối tượng game để bắt đầu trò chơi
        game.run_game()

        # Kiểm tra xem trò chơi đã kết thúc hay chưa
        if game.game_over:
            # Chuyển biến in_menu về True để quay lại màn hình menu
            in_menu = True

    pygame.display.flip()
    pygame.time.Clock().tick(30)
