import flet as ft
import sys
sys.path.insert(0, r'providers')
import movies_provider as movie


def fullPosterImag(posterPath):
    if (posterPath != null):
        return 'https://image.tmdb.org/t/p/w500${posterPath}'
    return 'https://i.stack.imgur.com/GNhxO.png'


img = ft.Image(
    src=f"/icons/icon-512.png",
    width=100,
    height=100,
    fit=ft.ImageFit.CONTAIN,
)
images = ft.Row(expand=1, wrap=False, scroll="always")
for i in range(0, 30):
    images.controls.append(
        ft.Image(
            src='https://i.stack.imgur.com/GNhxO.png',
            width=200,
            height=200,
            fit=ft.ImageFit.NONE,
            repeat=ft.ImageRepeat.NO_REPEAT,
            border_radius=ft.border_radius.all(10),
        )
    )
