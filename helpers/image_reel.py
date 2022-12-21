import providers.movies_provider as movie
from flet import *
import sys
sys.path.insert(0, r'providers')


def fullPosterImag(posterPath):
    if (posterPath != None):
        return 'https://image.tmdb.org/t/p/w500${posterPath}'
    return 'https://i.stack.imgur.com/GNhxO.png'


allmovie = Row(scroll=True)
s = []

for x in s:
    allmovie.controls.append(
        Card(
            elevation=30,
            content=Container(
                width=160,
                height=330,
                padding=10,
                border=border.symmetric(
                    vertical=border.BorderSide(5, "orange")),
                border_radius=border_radius.all(30),
                bgcolor="white",
                content=Column([
                    Image(
                        src=base_url+x["poster_path"],
                        height=200,
                        border_radius=border_radius.all(30),
                        fit="contain"
                    ),
                    Text(x['original_title'],
                         size=18,
                         weight="bold")

                ], alignment="center")
            )
        )
    )


mysection1 = Column([
    Text("Trending", size=20, weight="bold"),

    allmovie,

])


'''OLD
# img = ft.Image(
#     src=f"/icons/icon-512.png",
#     width=100,
#     height=100,
#     fit=ft.ImageFit.CONTAIN,
# )
# images = ft.Row(expand=1, wrap=False, scroll="always")
# for i in range(0, 30):
#     images.controls.append(
#         ft.Image(
#             src='https://i.stack.imgur.com/GNhxO.png',
#             width=200,
#             height=200,
#             fit=ft.ImageFit.NONE,
#             repeat=ft.ImageRepeat.NO_REPEAT,
#             border_radius=ft.border_radius.all(10),
#         )
#     )
'''
