import pygame
import sys
import random
import time

class TreasureMazeGame:
   import pygame
import sys
import random
import time

class TreasureMazeGame:
    def __init__(self):
        # Khởi tạo pygame
        pygame.init()

        # Set kích thước cửa sổ game
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Khởi tạo tiêu đề cửa sổ
        pygame.display.set_caption("Treasure Maze")

        # Khởi tạo màu
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)

        # Khởi tạo font
        self.font = pygame.font.Font(None, 36)

        # Set khung menu và khung game
        self.menu_width, self.menu_height = 800, 150
        self.maze_width, self.maze_height = 800, 450

        # Set kích cỡ ô vuông, số dòng, số cột của ma trận
        self.square_size = 25
        self.maze_cols = self.maze_width // self.square_size
        self.maze_rows = self.maze_height // self.square_size
        # => ma trận có 32 cột, 18 dòng
        # Set ô người dùng
        self.player_size = self.square_size
        self.target_size = self.square_size

        # Khai báo ma trận (0 - đường đi, 1 - tường)
        self.maze = self.get_defined_maze()

        # Người chơi và mục tiêu
        self.player_pos = [0, 0]
        self.target_pos = [self.maze_rows - 1, self.maze_cols - 1]

        # Điểm và thời gian
        self.start_time = time.time()
        self.initial_score = 600
        self.score = self.initial_score
        self.game_over = False

    def get_defined_maze(self):
        # Define your maze here as a 2D list of 0s and 1s
        # For example, a 3x3 maze with walls on the edges:
        defined_maze = [
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

        return defined_maze

    def draw_maze(self):
        for i in range(self.maze_rows):
            for j in range(self.maze_cols):
                if 0 <= i < len(self.maze) and 0 <= j < len(self.maze[i]) and self.maze[i][j] == 1:
                    pygame.draw.rect(self.screen, self.black, (j * self.square_size, i * self.square_size + self.menu_height, self.square_size, self.square_size))
                else:
                    pygame.draw.rect(self.screen, self.white, (j * self.square_size, i * self.square_size + self.menu_height, self.square_size, self.square_size))

    def draw_entities(self):
        pygame.draw.rect(self.screen, self.red, (self.player_pos[1] * self.square_size, self.player_pos[0] * self.square_size + self.menu_height, self.player_size, self.player_size))
        pygame.draw.rect(self.screen, self.red, (self.target_pos[1] * self.square_size, self.target_pos[0] * self.square_size + self.menu_height, self.target_size, self.target_size))

    def draw_score_frame(self):
        pygame.draw.rect(self.screen, self.black, (0, 0, self.width, self.menu_height))

        elapsed_time = int(time.time() - self.start_time)
        remaining_time = max(60 - elapsed_time, 0)  # Đếm ngược thời gian từ 60 giây và giữ cho giá trị không nhỏ hơn 0

        # Tính toán điểm dựa trên thời gian
        elapsed_seconds = time.time() - self.start_time
        score_loss = int(elapsed_seconds / 1) * 10
        self.score = max(self.initial_score - score_loss, 0)

        text = f"Time: {remaining_time} sec  Score: {self.score}"
        text_surface = self.font.render(text, True, self.white)
        self.screen.blit(text_surface, (10, 10))

        exit_button = pygame.Rect(self.width - 100, 10, 80, 30)
        pygame.draw.rect(self.screen, self.red, exit_button)
        exit_text = self.font.render("Exit", True, self.white)
        self.screen.blit(exit_text, exit_button.topleft)

        # Kiểm tra nút Exit có được nhấn hay không
        if exit_button.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:  # Kiểm tra xem có phải là nút trái chuột không
                self.game_over = True  # Đặt trạng thái trò chơi thành kết thúc

    def reset_game(self):
        # Reset the game when the player presses the "Play" button
        self.player_pos = [0, 0]
        self.target_pos = [self.maze_rows - 1, self.maze_cols - 1]
        self.start_time = time.time()
        self.score = self.initial_score
        self.game_over = False  # Đặt lại trạng thái trò chơi khi bắt đầu lại

    def run_game(self):
        # Vòng lặp chạy game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()

            # Cập nhật ô người chơi dựa trên nút 4 hướng
            if keys[pygame.K_UP] and self.player_pos[0] > 0 and self.maze[self.player_pos[0] - 1][self.player_pos[1]] == 0:
                self.player_pos[0] -= 1
            if keys[pygame.K_DOWN] and self.player_pos[0] < self.maze_rows - 1 and self.maze[self.player_pos[0] + 1][self.player_pos[1]] == 0:
                self.player_pos[0] += 1
            if keys[pygame.K_LEFT] and self.player_pos[1] > 0 and self.maze[self.player_pos[0]][self.player_pos[1] - 1] == 0:
                self.player_pos[1] -= 1
            if keys[pygame.K_RIGHT] and self.player_pos[1] < self.maze_cols - 1 and self.maze[self.player_pos[0]][self.player_pos[1] + 1] == 0:
                self.player_pos[1] += 1

            # Kiểm tra người chơi có đi tới mục đích
            if self.player_pos == self.target_pos:
                self.score += 100
                self.player_pos = [0, 0]
                self.target_pos = [self.maze_rows - 1, self.maze_cols - 1]

            # Vẽ màn hình
            self.screen.fill(self.black)
            pygame.draw.rect(self.screen, self.white, (0, 0, self.width, self.menu_height))
            pygame.draw.rect(self.screen, self.white, (0, self.menu_height, self.width, self.maze_height))
            self.draw_maze()
            self.draw_entities()
            self.draw_score_frame()

            pygame.display.flip()
            pygame.time.Clock().tick(30)

            if self.game_over:
                return  # Kết thúc vòng lặp nếu trò chơi đã kết thúc