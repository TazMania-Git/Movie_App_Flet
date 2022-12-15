from flet import *
from flet import icons, colors
import NavigationRail as nr

appmenu = AppBar(bgcolor="black",
                 center_title=True,
                 leading=IconButton(
                     icon=icons.MENU,
                     icon_color="white",
                     icon_size=30,
                     on_click=nr
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

                 ])
