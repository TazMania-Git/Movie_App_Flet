import providers.movies_provider as mp
import helpers.image_reel as reel
import NavigationRail as nr
import appmenu
from flet import *
from flet import icons, colors
import sys
sys.path.insert(0, r'helpers')
# sys.path.insert(1, r'providers')
# sys.path.append(r'.../providers')


class App(UserControl):
    def build(build):

        return Column(controls=[
            ])

        # ACA MANDO EL RAIL PARA EL COSTADO IZQ
        # return Column(height=500,width=100,controls=[nr.rail])
        ###


def main(page: Page):
    page.scroll = True
    page.theme_mode = ThemeMode.DARK
    page.title = "Movies App"
    page.update()
    app = App()
    page.add(
        app,
        appmenu.appbar
        # Row(
        #     [
        #         nr.rail,
        #         VerticalDivider(width=1),
        #         Column([Text("Body!")],
        #                alignment=MainAxisAlignment.START, expand=True),
        #     ],
        #     expand=True,
        # )
    )


if __name__ == "__main__":
    # hola = mp.result  # CON ESTO LLAMO Y TRAIGO EL RESULTADO DE LA API
    movie_provider = mp.Movie_provider()
    movie_provider.get_all_now_playing()
    app(target=main)
