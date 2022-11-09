import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    ''' Реагирует на нажатие клавиш'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        
def fire_bullet(ai_settings, screen, ship, bullets):
    '''Выпускает пулю, если максимум ещё не достигнут'''
    if len(bullets) < ai_settings.bullets_allowed:
        # Создание новой пули и включение ее в группу bullets
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def chek_keyup_events(event, ship):
    ''' Реагирует на отпускание клавиш'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    '''Обрабатывает нажатия клавиш и события мыши'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            chek_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    '''Обновляет изображения на экране и отображает новый экран'''
    # При каждом проходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    # Все пули выводятся позади изображений корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # Отображение последнего прорисованного экрана
    pygame.display.flip()

def update_bullets(bullets):
    ''' Обновляет позиции пуль и уничтожает старые пули'''
    # Обновление позиции пуль
    bullets.update()

     # Удаление пуль, вышедших за пределы экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
