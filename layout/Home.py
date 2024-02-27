from typing import Any, Dict, List

import flet as f
# import pendulum as dtp
from layout.actions_buttons import ActionsMenu
# from login import User
from layout.api.api import GetResult
from layout.appMenu import MenuApp
# from colors import ColorsApp
from flet import (AlertDialog, BoxShadow, ButtonStyle, Card, Column, Container,
                  CrossAxisAlignment, FontWeight, IconButton, Image, ImageFit,
                  MainAxisAlignment, Page, PieChart, PieChartEvent,
                  PieChartSection, ResponsiveRow, Row, Text, TextButton,
                  TextField, TextStyle, View, alignment, border, border_radius,
                  colors, icons, margin, padding)
from supabase import Client

# colors to app
RED_PIE_CHART: Dict[str, str] = {
    "red": "#f12c4c",
    "black": "#862b8c",
    "white": "#f3c318",
}
DARK_GREEN_BANNER = "greenaccent700"
LIGHT_GREEN_BANNER = "greenaccent200"
DARK_PURPLE = "#511F76"
LIGHT_PURPLE = "#9A2ED9"
LIGHT_ORANGE = "#FF8B00"
DARK_ORANGE = "#FF5319"
BORDER_INPUT = "#fbd80c"
CYAN_BUTTON_STYLE = "#1D223A"
WHITE_BUTTON_STYLE = "#FEFDFC"


class Home(View):
    def __init__(self, page: Page, data: Client) -> None:
        super(Home, self).__init__(
            route="/home",
            spacing=0,
            horizontal_alignment="center",
            scroll="auto"
        )

        self.normal_radius = 30
        self.hover_radius = 40
        self.normal_title_style = TextStyle(
            size=10, color=f.colors.WHITE, weight=FontWeight.BOLD
        )
        self.hover_title_style = TextStyle(
            size=15,
            color=f.colors.WHITE,
            weight=FontWeight.BOLD,
            shadow=BoxShadow(blur_radius=2, color=f.colors.BLACK54),
        )

        self.bots = {}
        self.data = data
        self.page = page
        self.page.scroll = "auto"
        self.menubar = MenuApp(page=self.page)
        self.actions = ActionsMenu(page=self.page)
        self.blaze = GetResult()

        # USER IN ACTION
        user = self.data.table("user").select("*, bot(*)").eq(
            "id_user", self.page.client_storage.get("_id")
        ).execute()

        self._user = user.data[0]

        # BOTOES E INPUTS PARA BUSCA DE BOTS NO APP
# -------------------------------------------------------------------------#

        # ENTRADA DE DADOS PARA BUSCA POR NOME|QUALQUER PARAMETRO
        self.input_search = TextField(
            border="none",
            label="Search bots ? ",
            label_style=TextStyle(
                color=DARK_PURPLE,
                size=15,
            ),
            color=DARK_PURPLE,
            prefix_icon=icons.SEARCH_ROUNDED,
        )

        # BOTÃO DE BUSCA
        self.button_search = TextButton(
            text="Search...",
            style=ButtonStyle(color=DARK_PURPLE),
            on_click=self.search_bots,
        )

        # SESSÃO PARA OS CARDS DEPENDENDO DA QUANTIDADE
# -------------------------------------------------------------------------#

        # FIELDS SÂO CAMPOS PARA AS BADGES CRIADAS DINAMICAMENTE
        self.fields_badge_bots = (
            ("Add bot", self.add_bots),
            ("Play bot", self.play_bot),
            ("Donation", self.donation),
            ("contact", self.contact)
        )

        # LINHA OU ROW DE CARDS BOTS CRIADOS DINAMICAMENTE
        self.row_card_bots = ResponsiveRow()

        # COLUNA GRID DO CONTEUDO
        self.column_bots_grid: Column = Column(
            controls=[
                ResponsiveRow(
                    controls=[
                        Column(
                            col={"sm": 6},
                            controls=[
                                self.input_search,
                            ],
                            alignment="start"
                        ),
                        Column(
                            col={"sm": 6},
                            controls=[
                                self.button_search,
                            ],
                            alignment="start"
                        ),
                    ],
                    # width=350,
                    alignment="center",
                ),
                Row(
                    controls=[
                        Text(
                            "Top Bots for you",
                            size=30,
                            weight="bold",
                        ),
                    ],
                    alignment="center"
                ),
                Row(
                    controls=[
                        self.create_container_badge(*i)
                        for i in self.fields_badge_bots
                    ],
                    alignment="spaceAround",
                    scroll="aways"
                ),
                Container(
                    margin=margin.only(bottom=40),
                    content=self.row_card_bots
                )
            ],
            alignment="center"
        )

        # SESSÃO DOS CARDS DOS BOTS COMTEM A COLUNA COM AS OPTIONS E CARDSBOTS
        self.section_bots = Container(
            margin=margin.symmetric(vertical=-30),
            padding=padding.only(20, 20, 20, 100),
            border_radius=border_radius.only(top_right=30, top_left=30),
            bgcolor=LIGHT_ORANGE,
            content=self.column_bots_grid
        )

        self.create_row_cards_content()

        # SESSÃO DO RODAPÉ ONDE TEM QUEM CRIOU O APP
# ------------------------------------------------------------------------------#

        # CONTAINER DE RODAPÉ
        self.footer_app = Container(
            padding=20,
            bgcolor="cyan"
        )

        self.controls = [
            self.menubar,
            self.actions,
            self.section_bots,
            self.footer_app
        ]

        self.page.update()

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    def create_column_results(self) -> Column:
        percent = self.blaze.percent_by_color()
        return Column(
            spacing=20,
            run_spacing=20,
            alignment="center",
            controls=[
                Row(
                    controls=[
                        Container(
                            width=25,
                            height=25,
                            # bgcolor=DARK_ORANGE,
                            shadow=f.BoxShadow(
                                spread_radius=1.8,
                                blur_radius=1.8,
                                color=DARK_ORANGE,
                            ),
                            border_radius=5,
                            on_click=lambda e: print("Modal statistic"),
                            content=Image(
                                src="assets/image/statistics-svgrepo-com.svg",
                                width=20,
                                height=20,
                                fit="contain"
                            )
                        ),
                        Text(
                            value="Percent results",
                            size=15,
                            weight="bold",
                            color=DARK_PURPLE
                        ),
                    ],
                    alignment="start"
                ),
                Row(
                    controls=[
                        self.create_pie_charts_sections(percent=percent),
                    ],
                    alignment="center"
                ),
            ],
            expand=True,
            height=120
        )

    def create_container_responsive(self, content, padding) -> Container:
        if padding == "only":
            padding = f.padding.only(left=10, right=10)

        return Container(
            padding=padding,
            content=Row(
                controls=content,
                alignment="center",
                scroll="aways"
            )
        )

    def create_card_bots(self, bot) -> Card:
        return Card(
            col={"xs": 12, "sm": 6, "md": 4},
            # width=400,
            # height=400,
            elevation=30,
            shadow_color=DARK_ORANGE,
            content=Container(
                data=bot,
                bgcolor=LIGHT_ORANGE,
                padding=10,
                on_click=self.open_card_bot,
                content=Column(
                    controls=[
                        Image(
                            src="assets/image/ChatBot.jpg",
                            fit="contain",
                            border_radius=100,
                            width=300,
                            height=220,
                        ),
                        Text(
                            value=f"Name: {bot["name"]}",
                            size=20,
                            weight="bold",
                        ),
                        Text(
                            value=str(bot["game"]).replace(
                                "_", " "
                            ).capitalize(),
                            size=15,
                            color="gray"
                        )
                    ]
                )
            )
        )

    def select_bot(self, event) -> None:
        print(event.control.data)
        bot: List[Any] = event.control.data
        bots_dialog = AlertDialog(
            title=Text(
                value="Name Bot: None"
            ),
            content=Container(
                content=Column(
                    controls=[
                        TextField(
                            label="",
                            value=f"{bot}"
                        )
                    ]
                )
            )
        )
        self.page.dialog = bots_dialog
        self.page.dialog.open = True
        self.page.update()

    def create_container_badge(self, text: str, func=None):
        # CREATE CONTAINER BADGE SECTION BOTS :)
        def create_func(e):
            print("Badge Action!")

        if not func:
            func = create_func

        return Container(
            margin=margin.only(top=10),
            border_radius=30,
            padding=10,
            bgcolor=LIGHT_PURPLE,
            # ink=True,
            on_click=func,
            border=border.all(2, "#E1E1E1"),
            content=Text(value=text, size=13, color="White"),
        )

    def create_row_cards_content(self):
        data = self.data.table("bot").select("*").eq(
            "id_user", self.page.client_storage.get("_id")
        ).execute()

        if data.data:
            self.row_card_bots.controls.clear()
            for i in data.data:
                self.row_card_bots.controls.append(
                    self.create_card_bots(i)
                )
                self.page.update()
            return
        self.row_card_bots.controls.clear()
        self.row_card_bots.controls.append(
            self.create_card_bots({"name": "Not Bot", "game": "Not Game"})
        )
        self.page.update()

    def search_bots(self, event):
        print("Search bots")

    def add_bots(self, event):
        self.page.go("/addbot")

    def play_bot(self, event):
        print("Play bot")

    def donation(self, event):
        print("Donation")

    def contact(self, event):
        print("contact")

    def open_card_bot(self, event):
        self.page.client_storage.set("bot", event.control.data)
        self.page.go("/cardbot")
