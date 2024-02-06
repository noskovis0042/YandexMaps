from Samples.geocoder import get_coordinates, get_ll_span
from Samples.mapapi_PG import show_map

argv = ['Maps API.py', '37.617848, 55.755336']

toponym_to_find = " ".join(argv[1:])

if toponym_to_find:
    ll, spn = get_ll_span(toponym_to_find)
    ll_spn = f"ll={ll}&spn={spn}"
    show_map(ll_spn, 'map')
else:
    print('Данных нет')
