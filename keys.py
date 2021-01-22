import pygame

# Клавиши для игрока
player_keys = {
               pygame.K_w: 'UP',
               pygame.K_s: 'DOWN',
               pygame.K_a: 'LEFT',
               pygame.K_d: 'RIGHT'
               }
player_keys_list = player_keys.keys()

# клавиши для игры
game_keys = {
             pygame.K_ESCAPE: 'PAUSE'
             } | player_keys  # Новая фича, не робит на старых версиях
game_keys_list = game_keys.keys()
