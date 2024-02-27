import flet as f
from layout.colors import ColorsApp
from layout.text_style import TextStyleApp
from layout.appMenu import MenuApp
from layout.actions_buttons import ActionsMenu
from supabase import Client

colors = ColorsApp()
text = TextStyleApp()


class Menu(f.View):
    def __init__(self, page: f.Page, data: Client) -> None:
        super(Menu, self).__init__(
            route="/menu",
            spacing=0,
            horizontal_alignment="center"
        )

        self.page = page
        self.data = data

        self.menuapp = MenuApp(page=self.page)
        self.actions = ActionsMenu(page=self.page)

        self.card_menu = f.Card(
            elevation=30,
        )

        self.body_menu = f.ResponsiveRow(
            controls=[
                f.Container(
                    alignment=f.alignment.center,
                    bgcolor=colors.Light_orange,
                    border_radius=f.border_radius.only(
                        top_left=30,
                        top_right=30
                    ),
                    padding=0,
                    margin=f.margin.symmetric(vertical=-30),
                    content=f.Column(
                        col={"xs": 12, "sm": 12, "md": 12, "lg": 12},
                        controls=[
                            self.card_menu
                        ],
                    )
                )
            ]
        )

        self.controls = [
            self.menuapp,
            self.actions,
            self.body_menu
        ]

    def create_cards_games_menu(self, event):
        fields = ("Fortune APP")
