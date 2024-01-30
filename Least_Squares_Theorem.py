import pygame
import sys
import numpy as np
from sklearn.linear_model import LinearRegression

# Pygame'ı başlat
pygame.init()

# Ekran boyutu (16:9 formatında)
WIDTH, HEIGHT = 1200, 675  # 16:9 için genişlik: yükseklik = 16:9
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("En Küçük Kareler Teoremi Animasyonu")

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Veri noktaları ve regresyon çizgisi için veri yapısı
data_points = []
regression_line = None

# Kullanıcının gireceği koordinat değerleri
user_x = 0
user_y = 0

# Ana oyun döngüsü
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Fare tıklamasını yakala
            x, y = pygame.mouse.get_pos()
            data_points.append((x, y))

            # En küçük kareler regresyonunu güncelle
            if len(data_points) >= 2:
                X = np.array([point[0] for point in data_points]).reshape(-1, 1)
                y = np.array([point[1] for point in data_points])
                model = LinearRegression().fit(X, y)
                regression_line = [(0, int(model.intercept_)), (WIDTH, int(model.predict([[WIDTH]])[0]))]

        if event.type == pygame.KEYDOWN:
            # Kullanıcının koordinatları girmesi için klavye girişini yakala
            if event.key == pygame.K_RETURN:
                data_points.append((user_x, user_y))

                # En küçük kareler regresyonunu güncelle
                if len(data_points) >= 2:
                    X = np.array([point[0] for point in data_points]).reshape(-1, 1)
                    y = np.array([point[1] for point in data_points])
                    model = LinearRegression().fit(X, y)
                    regression_line = [(0, int(model.intercept_)), (WIDTH, int(model.predict([[WIDTH]])[0]))]

            elif event.key == pygame.K_UP:
                user_y -= 10
            elif event.key == pygame.K_DOWN:
                user_y += 10
            elif event.key == pygame.K_LEFT:
                user_x -= 10
            elif event.key == pygame.K_RIGHT:
                user_x += 10

    # Ekranı temizle
    screen.fill(WHITE)

    # Koordinat düzlemini çiz
    pygame.draw.line(screen, BLACK, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 2)  # x eksenini çiz
    pygame.draw.line(screen, BLACK, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)  # y eksenini çiz

    # Gridleri çiz
    for i in range(-WIDTH // 2, WIDTH // 2 + 1, 50):
        pygame.draw.line(screen, BLACK, (WIDTH // 2 + i, 0), (WIDTH // 2 + i, HEIGHT), 1)
        pygame.draw.line(screen, BLACK, (0, HEIGHT // 2 + i), (WIDTH, HEIGHT // 2 + i), 1)

    # Sayıları mavi renkte ve küçük boyutta çiz
    font = pygame.font.SysFont("timesnewroman", 18)
    for i in range(-WIDTH // 2, WIDTH // 2 + 1, 50):
        text = font.render(str(i), True, BLUE)
        screen.blit(text, (WIDTH // 2 + i + 5, HEIGHT // 2 - 20))
        text = font.render(str(-i), True, BLUE)
        screen.blit(text, (WIDTH // 2 - 20, HEIGHT // 2 + i + 5))

    # Noktaları çiz
    for point in data_points:
        pygame.draw.circle(screen, RED, point, 5)

    # Regresyon çizgisini çiz
    if regression_line:
        pygame.draw.line(screen, RED, regression_line[0], regression_line[1], 2)

    # Kullanıcının noktasını çiz
    pygame.draw.circle(screen, BLACK, (WIDTH // 2 + user_x, HEIGHT // 2 - user_y), 8)

    # Ekranı güncelle
    pygame.display.flip()

    # Oyun hızını sınırla
    clock.tick(60)
