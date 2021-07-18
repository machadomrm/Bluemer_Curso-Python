# print('Hello word!!')
# print('Criei meu primeiro código. Eba!!!')

import os
import pygame

pygame.init()
if os.path.exists('./theraven.mp3'):
    pygame.mixer.music.load('./theraven.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)

    clock = pygame.time.Clock()
    clock.tick(10)

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
else:
    print('O arquivo musica.mp3 não está no diretório do script Python')