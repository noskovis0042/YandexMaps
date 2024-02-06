import pygame
from Samples.geocoder import get_coordinates, get_ll_span
from Samples.mapapi_PG import return_map

argv = ['Maps API.py', '37.617848, 55.755336']

toponym_to_find = " ".join(argv[1:])

if toponym_to_find:
    ll, spn = get_ll_span(toponym_to_find)
    yandex_map = return_map(f"ll={ll}&spn={spn}", 'map')

    pygame.init()
    screen = pygame.display.set_mode((600, 450))

    screen.blit(yandex_map, (0, 0))
    while pygame.event.wait().type != pygame.QUIT:
        key = pygame.key.get_pressed()
        if key[pygame.K_PAGEUP]:
            spn = ','.join([str(float(i) * 1.5) for i in spn.split(',')])
            yandex_map = return_map(f"ll={ll}&spn={spn}", 'map')
        if key[pygame.K_PAGEDOWN]:
            spn = ','.join([str(float(i) / 1.5) for i in spn.split(',')])
            yandex_map = return_map(f"ll={ll}&spn={spn}", 'map')
        screen.fill('White')
        screen.blit(yandex_map, (0, 0))
        pygame.display.flip()
    pygame.quit()
else:
    print('Данных нет')
