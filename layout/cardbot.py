from typing import Any, Dict, List

from layout.actions_buttons import ActionsMenu
from layout.appMenu import MenuApp
from flet import (BarChart, BarChartGroup, BarChartRod, Border, BorderSide,
                  BoxShadow, Card, ChartAxis, ChartAxisLabel, ChartGridLines,
                  Column, Container, Control, IconButton, Image, Page,
                  PieChart, PieChartEvent, PieChartSection, ResponsiveRow, Row,
                  Text, TextStyle, View, border, border_radius, colors, margin,
                  padding, icons)

DARK_GREEN_BANNER = "greenaccent700"
LIGHT_GREEN_BANNER = "greenaccent200"
DARK_PURPLE = "#511F76"
LIGHT_PURPLE = "#9A2ED9"
LIGHT_ORANGE = "#FF8B00"
DARK_ORANGE = "#FF5319"
BORDER_INPUT = "#fbd80c"
CYAN_BUTTON_STYLE = "#1D223A"
WHITE_BUTTON_STYLE = "#FEFDFC"

SUBITITLE_SIZE = 12
BUTTONS_SIZE = 30
BORDER_RADIUS_DEFAULT = 5


class CardBot(View):

    @staticmethod
    def _create_card_field_bot(col: Dict[str, int], content: Control) -> Card:
        return Card(
            col=col,
            content=content,
            elevation=30,
            color=LIGHT_ORANGE,
            shadow_color=DARK_ORANGE,
        )

    @staticmethod
    def _create_container_card(content: Control) -> Container:
        return Container(
            margin=margin.all(3),
            bgcolor=LIGHT_ORANGE,
            padding=10,
            content=content,
        )

    # CRIA UM CONTAINER BUTTON PARA SELEÇÃO DE CORES/NUMEROS DO PADRÃO
    @staticmethod
    def _create_container_selection_color_or_number(
        content=None,
        bgcolor=None,
        circle=False,
        data=None,
        func=lambda e: print("None")
    ) -> Container:
        if circle:
            content = Container(
                border_radius=border_radius.all(15),
                margin=margin.all(4),
                border=Border(
                    top=BorderSide(2, "#F1F1F1"),
                    right=BorderSide(2, "#F1F1F1"),
                    bottom=BorderSide(2, "#F1F1F1"),
                    left=BorderSide(2, "#F1F1F1"),
                )
            )
        return Container(
            width=BUTTONS_SIZE,
            height=BUTTONS_SIZE,
            border_radius=BORDER_RADIUS_DEFAULT,
            bgcolor=bgcolor,
            content=content,
            data=data,
            on_click=func
        )

    # CONVERTE A LISTA DE DEFAULT PARA O DISPLAY
    @staticmethod
    def _create_params_row_default(
        default: List[str],
        srcs: List[str],
        func: Any
    ) -> List[Control]:

        list_return = []

        for i in default:
            if i in srcs:
                list_return.append(
                    (
                        Image(
                            src=f"assets/image/{i}",
                            width=BUTTONS_SIZE,
                            height=BUTTONS_SIZE,
                            border_radius=BORDER_RADIUS_DEFAULT
                        ),
                        None,
                        False,
                        i,
                        func
                    )
                )
            if i == "yellow":
                list_return.append(
                    (
                        Image(
                            src="assets/image/panda-1.png",
                            width=BUTTONS_SIZE,
                            height=BUTTONS_SIZE,
                            border_radius=BORDER_RADIUS_DEFAULT
                        ),
                        None,
                        False,
                        i,
                        func
                    )
                )
            if i == "red":
                list_return.append(
                    (
                        None,
                        "#F22C4D",
                        True,
                        i,
                        func
                    )
                )
            if i == "black":
                list_return.append(
                    (
                        None,
                        "#6448e0",
                        True,
                        i,
                        func
                    )
                )
            if i == "all":
                list_return.append(
                    (
                        None,
                        "#0285c7",
                        True,
                        i,
                        func
                    )
                )
        return list_return

    def __init__(self, page: Page, data: Dict[str, Any]) -> None:
        super(CardBot, self).__init__(
            route="/cardbot",
            spacing=0,
            padding=0,
            scroll="auto",
            horizontal_alignment="center"
        )

        self.page = page
        self.data: Dict[str, Any] = data
        self.menuapp = MenuApp(self.page)
        self.actions = ActionsMenu(self.page)

        self.bot: Dict = self.page.client_storage.get("bot")

        # CAMINHO PARA AS IMAGENS SRC DOS BOTOES DE ADIÇÂO DE PADRÃO
        self.src_numbers = [
            "red-1.png", "red-2.png", "red-3.png", "red-4.png", "red-5.png",
            "red-6.png", "red-7.png", "black-8.png", "black-9.png",
            "black-10.png", "black-11.png", "black-12.png", "black-13.png",
            "black-14.png"
        ]

        self.defaults_red = [
            i for k, v in self.bot.items()
            if k == "defaults" for ke, va in v.items() if ke == "red"
            for i in va
        ]

        self.defaults_black = [
            i for k, v in self.bot.items()
            if k == "defaults" for ke, va in v.items() if ke == "black"
            for i in va
        ]

        self.normal_title_style = TextStyle(
            size=16, color=colors.WHITE, weight="bold"
        )

        self.hover_title_style = TextStyle(
            size=22,
            color=colors.WHITE,
            weight="bold",
            shadow=BoxShadow(blur_radius=2, color=colors.BLACK54),
        )

        self.normal_radius = 50
        self.hover_radius = 60

        self.column_display_black = Column(
            controls=[
                Text("Victory in black")
            ]
        )
        self.column_display_red = Column(
            controls=[
                Text("Victory in red")
            ]
        )

        self.txt_name = Text(
            value=f"{self.bot["name"]}",
            size=25,
        )

        self.chart = PieChart(
            sections=[
                PieChartSection(
                    40,
                    title="40%",
                    title_style=self.normal_title_style,
                    color=colors.BLUE,
                    radius=self.normal_radius,
                ),
                PieChartSection(
                    30,
                    title="30%",
                    title_style=self.normal_title_style,
                    color=colors.YELLOW,
                    radius=self.normal_radius,
                ),
                PieChartSection(
                    15,
                    title="15%",
                    title_style=self.normal_title_style,
                    color=colors.PURPLE,
                    radius=self.normal_radius,
                ),
                PieChartSection(
                    15,
                    title="15%",
                    title_style=self.normal_title_style,
                    color=colors.GREEN,
                    radius=self.normal_radius,
                ),
            ],
            sections_space=0,
            center_space_radius=40,
            on_chart_event=self.on_chart_event,
            expand=True,
        )

        self.responsive_row_display: ResponsiveRow = ResponsiveRow(
            controls=[
                Row(
                    col={"xs": 12, "md": 12, "md": 12},
                    controls=[
                        self.txt_name
                    ],
                    alignment="center"
                )
            ]
        )

        self.section_bot = Container(
            padding=padding.only(10, 20, 10, 20),
            margin=margin.symmetric(vertical=-30),
            border_radius=border_radius.only(top_left=30, top_right=30),
            bgcolor=LIGHT_ORANGE,
            content=self.responsive_row_display
        )

        self.controls = [
            self.menuapp,
            self.actions,
            self.section_bot
        ]

        self.inser_chats_into_display()

        self.insert_columns_defaults()

        self.insert_dinamic_data_bot()

        self.page.update()

    # INSERÇÃO DE DADOS EM GRAFICOS DE DESEMPENHO DO BOT
    def inser_chats_into_display(self):
        statistics = {}
        for key, field in self.bot.items():
            if key == "statistics":
                statistics = field

        self.responsive_row_display.controls.append(
            CardBot._create_card_field_bot(
                {"xs": 12, "md": 4},
                CardBot._create_container_card(
                    BarChart(
                            bar_groups=[
                                BarChartGroup(
                                    x=0,
                                    bar_rods=[
                                        BarChartRod(
                                            from_y=0,
                                            to_y=statistics["total_tips"],
                                            width=40,
                                            color=colors.AMBER,
                                            tooltip="Total Tips",
                                            border_radius=0,
                                        ),
                                    ],
                                ),
                                BarChartGroup(
                                    x=1,
                                    bar_rods=[
                                        BarChartRod(
                                            from_y=0,
                                            to_y=statistics["total_wins"],
                                            width=40,
                                            color=colors.BLUE,
                                            tooltip="Wins",
                                            border_radius=0,
                                        ),
                                    ],
                                ),
                                BarChartGroup(
                                    x=2,
                                    bar_rods=[
                                        BarChartRod(
                                            from_y=0,
                                            to_y=statistics["total_reds"],
                                            width=40,
                                            color=colors.RED,
                                            tooltip="Loss",
                                            border_radius=0,
                                        ),
                                    ],
                                ),
                                BarChartGroup(
                                    x=3,
                                    bar_rods=[
                                        BarChartRod(
                                            from_y=0,
                                            to_y=60,
                                            width=statistics["total_wins_primary"],
                                            color=colors.ORANGE,
                                            tooltip="Wins Primary",
                                            border_radius=0,
                                        ),
                                    ],
                                ),
                            ],
                            border=border.all(1, colors.GREY_400),
                            left_axis=ChartAxis(
                                labels_size=40,
                                title=Text("Statistics"),
                                title_size=40
                            ),
                            bottom_axis=ChartAxis(
                                labels=[
                                    ChartAxisLabel(
                                        value=0, label=Container(
                                            Text("Total Tips"), padding=10
                                        )
                                    ),
                                    ChartAxisLabel(
                                        value=1, label=Container(
                                            Text("Wins"), padding=10
                                        )
                                    ),
                                    ChartAxisLabel(
                                        value=2, label=Container(
                                            Text("Loss"), padding=10
                                        )
                                    ),
                                    ChartAxisLabel(
                                        value=3, label=Container(
                                            Text("Wins Primary"), padding=10
                                        )
                                    ),
                                ],
                                labels_size=40,
                            ),
                            horizontal_grid_lines=ChartGridLines(
                                color=colors.GREY_300,
                                width=1,
                                dash_pattern=[3, 3]
                            ),
                            tooltip_bgcolor=colors.with_opacity(
                                0.5, colors.GREY_300
                            ),
                            max_y=110,
                            interactive=True,
                            expand=True,
                    )
                )
            )
        )

    def on_chart_event(self, e: PieChartEvent):
        for idx, section in enumerate(self.chart.sections):
            if idx == e.section_index:
                section.radius = self.hover_radius
                section.title_style = self.hover_title_style
            else:
                section.radius = self.normal_radius
                section.title_style = self.normal_title_style
        self.page.update()

    # FUNÇÃO RESPONSAVEL POR INSERIR OS DADOS DINAMICAMENTE NA TELA
    def insert_dinamic_data_bot(self):
        for key, field in self.bot.items():
            if key == "name":
                self.responsive_row_display.controls.append(
                    CardBot._create_card_field_bot(
                        {"xs": 12, "sm": 6, "md": 4, "xl": 3},
                        CardBot._create_container_card(
                            content=Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text(f"{key}".capitalize(), size=20),
                                            IconButton(
                                                data=key,
                                                icon=icons.EDIT_ROUNDED,
                                                icon_size=20,
                                                icon_color="#0285c7",
                                                on_click=self.edit_field_bot
                                            )
                                        ]
                                    ),
                                    Text(f"{field}".capitalize())
                                ]
                            )
                        )
                    )
                )
            if key == "token":
                self.responsive_row_display.controls.append(
                    CardBot._create_card_field_bot(
                        {"xs": 12, "sm": 6, "md": 4, "xl": 3},
                        CardBot._create_container_card(
                            content=Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text("Token", size=20),
                                            IconButton(
                                                data=key,
                                                icon=icons.EDIT_ROUNDED,
                                                icon_size=20,
                                                icon_color="#0285c7",
                                                on_click=self.edit_field_bot
                                            )
                                        ]
                                    ),
                                    Text(
                                        value=f"{field}".capitalize()
                                    )
                                ]
                            )
                        )
                    )
                )
            if key == "chat_id":
                self.responsive_row_display.controls.append(
                    CardBot._create_card_field_bot(
                        {"xs": 12, "sm": 6, "md": 4, "xl": 3},
                        CardBot._create_container_card(
                            content=Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text("Chat Id", size=20),
                                            IconButton(
                                                data=key,
                                                icon=icons.EDIT_ROUNDED,
                                                icon_size=20,
                                                icon_color="#0285c7",
                                                on_click=self.edit_field_bot
                                            )
                                        ]
                                    ),
                                    Text(
                                        value=f"{field}".capitalize()
                                    )
                                ]
                            )
                        )
                    )
                )
            if key == "game":
                self.responsive_row_display.controls.append(
                    CardBot._create_card_field_bot(
                        {"xs": 12, "sm": 6, "md": 4, "xl": 3},
                        CardBot._create_container_card(
                            content=Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text("Game", size=20),
                                            IconButton(
                                                data=key,
                                                icon=icons.EDIT_ROUNDED,
                                                icon_size=20,
                                                icon_color="#0285c7",
                                                on_click=self.edit_field_bot
                                            )
                                        ]
                                    ),
                                    Text(
                                        value=f"{field}".capitalize()
                                    )
                                ]
                            )
                        )
                    )
                )

    # INSERE OS PADROES EM LINHA CORRESPONDENTE AO BOT
    def insert_columns_defaults(self):

        list_params_black = [
            CardBot._create_params_row_default(
                i,
                self.src_numbers,
                self.func_all_teste
            )
            for i in self.defaults_black
        ]

        list_params_red = [
            CardBot._create_params_row_default(
                i,
                self.src_numbers,
                self.func_all_teste
            )
            for i in self.defaults_red
        ]

        list_controls_red = [
            Row(
                controls=[
                    CardBot._create_container_selection_color_or_number(*i)
                    for i in row
                ]
            ) for row in list_params_red
        ]

        list_controls_black = [
            Row(
                controls=[
                    CardBot._create_container_selection_color_or_number(*i)
                    for i in row
                ]
            ) for row in list_params_black
        ]

        for i in list_controls_red:
            i.controls.extend(
                [
                    IconButton(
                        data=len([i for i in self.column_display_black.controls if isinstance(i, Row)]),
                        icon=icons.DELETE_ROUNDED,
                        icon_color="#6448e0",
                        on_click=self.delete_default_red
                    )
                ]
            )

        for i in list_controls_black:
            i.controls.extend(
                [
                    IconButton(
                        data=len([i for i in self.column_display_black.controls if isinstance(i, Row)]),
                        icon=icons.DELETE_ROUNDED,
                        icon_color="#6448e0",
                        on_click=self.delete_default_black
                    )
                ]
            )

        self.column_display_black.controls.extend(list_controls_black)
        self.column_display_red.controls.extend(list_controls_red)

        self.responsive_row_display.controls.append(
            CardBot._create_card_field_bot(
                {"xs": 12, "sm": 4},
                CardBot._create_container_card(
                    self.column_display_red
                )
            )
        )
        self.responsive_row_display.controls.append(
            CardBot._create_card_field_bot(
                {"xs": 12, "sm": 4},
                CardBot._create_container_card(
                    self.column_display_black
                )
            )
        )

    def func_all_teste(self, event):
        print("event")

    def delete_default_black(self, event):
        print("delete")

    def delete_default_red(self, event):
        print("delete")

    def edit_field_bot(self, event):
        print(f"{event.control.data}")
