import pygame
import random

class Oyuncu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.saglik = 100
        self.parasi = 100
        self.silahlar = []

    def saldir(self, dusman):
        zar_atisi = random.randint(1, 10)
        hasar = sum([silah.hasar for silah in self.silahlar]) + zar_atisi
        dusman.saglik -= hasar
        return hasar

# Düşman sınıfı
class Dusman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, 750), random.randint(50, 550))
        self.saglik = 50
        self.saldiri = 8

    def saldir(self, oyuncu):
        zar_atisi = random.randint(1, 6)
        hasar = self.saldiri + zar_atisi
        oyuncu.saglik -= hasar
        return hasar

# Silah sınıfı
class Silah(pygame.sprite.Sprite):
    def __init__(self, adi, fiyat, hasar):
        super().__init__()
        self.adi = adi
        self.fiyat = fiyat
        self.hasar = hasar

# Demirci sınıfı
class Demirci(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.silahlar = [
            Silah("Kılıç", 20, 10),
            Silah("Ok", 15, 7),
            Silah("Mızrak", 18, 9)
        ]

# Pygame başlat
pygame.init()

# Ekran boyutu
ekran_genislik = 800
ekran_yukseklik = 600
ekran = pygame.display.set_mode((ekran_genislik, ekran_yukseklik))
pygame.display.set_caption("RPG Oyunu")

# Renkler
siyah = (0, 0, 0)
beyaz = (255, 255, 255)

# Zaman tanımları
saat = pygame.time.Clock()
FPS = 60

# Sprite grupları
oyuncu_grup = pygame.sprite.Group()
dusman_grup = pygame.sprite.Group()
demirci_grup = pygame.sprite.Group()

# Oyuncu oluştur
oyuncu = Oyuncu()
oyuncu_grup.add(oyuncu)

# Düşman oluştur
for _ in range(10):
    dusman = Dusman()
    dusman_grup.add(dusman)

# Demirci oluştur
demirci = Demirci()
demirci_grup.add(demirci)

# Ana oyun döngüsü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Oyuncu hareket
    keys = pygame.key.get_pressed()
    oyuncu_hiz = 5
    if keys[pygame.K_LEFT]:
        oyuncu.rect.x -= oyuncu_hiz
    if keys[pygame.K_RIGHT]:
        oyuncu.rect.x += oyuncu_hiz
    if keys[pygame.K_UP]:
        oyuncu.rect.y -= oyuncu_hiz
    if keys[pygame.K_DOWN]:
        oyuncu.rect.y += oyuncu_hiz

    # Düşman hareket
    for dusman in dusman_grup:
        dusman_hiz = 2
        if dusman.rect.x < oyuncu.rect.x:
            dusman.rect.x += dusman_hiz
        elif dusman.rect.x > oyuncu.rect.x:
            dusman.rect.x -= dusman_hiz
        if dusman.rect.y < oyuncu.rect.y:
            dusman.rect.y += dusman_hiz
        elif dusman.rect.y > oyuncu.rect.y:
            dusman.rect.y -= dusman_hiz

    # Çarpışmaları kontrol et
    dusman_saldiri_hizasi = 1
    for dusman in dusman_grup:
        if pygame.sprite.collide_rect(oyuncu, dusman):
            oyuncu.saglik -= dusman.saldir(oyuncu)
            if oyuncu.saglik <= 0:
                running = False
            dusman.rect.x += dusman_saldiri_hizasi  # Düşmanlar oyuncuya doğru ilerler

    # Ekranı temizle
    ekran.fill(siyah)

    # Sprite gruplarını çiz
    oyuncu_grup.draw(ekran)
    dusman_grup.draw(ekran)
    demirci_grup.draw(ekran)

    # Ekranı güncelle
    pygame.display.flip()

    # FPS sınırlama
    saat.tick(FPS)

    # Oyunun sürekli çalışmasını sağlamak için bekleme
    pygame.time.delay(10)

# Pygame'i kapat
pygame.quit()
