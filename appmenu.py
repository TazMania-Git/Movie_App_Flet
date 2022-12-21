from flet import *
from flet import icons, colors


def check_item_clicked(e):
    e.control.checked = not e.control.checked


appbar = AppBar(
    leading=Icon(icons.MOVIE),
    leading_width=40,
    title=Text("Movies app"),
    center_title=False,
    bgcolor=colors.SURFACE_VARIANT,
    actions=[
        IconButton(icons.WB_SUNNY_OUTLINED),
        IconButton(icons.FILTER_3),
        PopupMenuButton(
            items=[
                PopupMenuItem(text="Item 1"),
                PopupMenuItem(),  # divider
                PopupMenuItem(
                    text="Checked item", checked=False, on_click=check_item_clicked
                ),
                PopupMenuItem(text="Item 2"),
                PopupMenuItem(),  # divider
                PopupMenuItem(
                    text="Checked item", checked=False, on_click=check_item_clicked
                ),

            ]
        ),
    ],
)

'''COSA ANTIGUA
appmenu = AppBar(bgcolor="black",
                 center_title=True,
                 leading=IconButton(
                     icon=icons.MENU,
                     icon_color="white",
                     icon_size=30,
                 ),
                 title=Text("Movie App",
                            size=30,
                            color="white",
                            weight="bold"
                            ),
                 actions=[
                     IconButton(
                         icon=icons.SEARCH,
                         icon_color="white",
                         icon_size=30

                     ),

                 ])'''
