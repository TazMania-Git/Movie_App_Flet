import helpers.image_reel as reel
import NavigationRail as nr
import appmenu
from flet import *
from flet import icons, colors
import sys
sys.path.insert(0, r'helpers')


def main(page: Page):
    page.scroll = True
    page.theme_mode = ThemeMode.DARK
    page.title = "Movie App"
    page.add(
        # appmenu.appmenu,
        Row(
            [
                nr.rail,
                VerticalDivider(width=1),
                Column([Text("Body!")],
                       alignment=MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )


flet.app(target=main)
