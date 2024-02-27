from typing import Dict, List, Any
import random

from layout.actions_buttons import ActionsMenu
from layout.appMenu import MenuApp
from flet import (Border, BorderSide, ButtonStyle, Card, Column, Container,
                  Control, Divider, Dropdown, ElevatedButton, IconButton,
                  Image, InputBorder, Page, ResponsiveRow, Row, CupertinoAlertDialog,
                  Text, TextButton, TextField, TextStyle, View, border_radius,
                  dropdown, icons, margin, padding)

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


class CreateObjectId:
    def __init__(self) -> None:
        self._cache_ = {}
        self.id_cache = 0

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        caracters = [
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "l", "m", "n", "o", "p", "k", "y", "r", "s", "t",
            "u", "v", "x", "z"
        ]

        for i in range(0, 10):
            cod_id = str(random.choice(
                range(0, 1000))) + random.choice(caracters)
            if cod_id not in self._cache_:
                self.id_cache += 1
                self._cache_[str(self.id_cache)] = cod_id
                return cod_id


class CreateObjectDefalt:
    def __init__(self) -> None:
        pass

    def __call__(self, defaults: List[Control]) -> List[str]:
        return [
            default.data
            for default in defaults
            if isinstance(default.data, str)
        ]


class AddBot(View):

    # CRIA UM CARD COM OS PREREQUISITOS PASSADOS E REDUNTANTES
    # FUNCIONA PARA ABSTRAIR LINHAS DE CODIGO REPEDIDAS
    @staticmethod
    def _create_card_addbots(col: Dict[str, int], content: Control) -> Card:
        return Card(
            col=col,
            content=content,
            color=LIGHT_ORANGE,
            shadow_color=DARK_ORANGE,
            elevation=30,
        )

    # CRIA UM CONTAINER/DIV PARA O CONTEUDO DO CARD
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
    def _create_container_selection_color(
        content=None, bgcolor=None,
        circle=False, data=None,
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

    def __init__(self, page: Page, data):
        super(AddBot, self).__init__(
            route="/addbot",
            vertical_alignment="center",
            scroll="auto",
            spacing=0,
        )

        # VARIAVEIS DE CONTROLE DE ADIÇÃO E DA VIEW
        self._cache: List[Control] = []
        self.trash: List[Any] = []
        self.statistics = {
            "total_reds": 0,
            "total_tips": 0,
            "total_wins": 0,
            "total_wins_gale": 0,
            "total_wins_primary": 0
        }
        self.defaults = {
            "red": [],
            "black": [],
        }

        # CAMINHO PARA AS IMAGENS SRC DOS BOTOES DE ADIÇÂO DE PADRÃO
        self.src_numbers_red = [
            "red-1.png", "red-2.png", "red-3.png", "red-4.png", "red-5.png",
            "red-6.png", "red-7.png"
        ]

        # CAMINHO PARA AS IMAGENS SRC DOS BOTOES DE ADIÇÂO DE PADRÃO
        self.src_numbers_black = [
            "black-8.png", "black-9.png", "black-10.png", "black-11.png",
            "black-12.png", "black-13.png", "black-14.png"
        ]

        self.controls_column_black = []
        self.controls_column_red = []

        self.page = page
        self.data = data

        self.actions = ActionsMenu(self.page)
        self.menuapp = MenuApp(self.page)

        # ENTRADA DE DADOS DO NOME DO BOT
        self.input_name = TextField(
            helper_text="Enter the bot name",
            helper_style=TextStyle(
                size=SUBITITLE_SIZE,
                color="#0F1923",
            ),
            data="Name",
            label="",
            border=InputBorder.UNDERLINE,
            border_color=LIGHT_PURPLE,
            color=DARK_PURPLE,
        )

        # ENTRADA DE DADOS DO TOKEN DO BOT DO TELEGRAM
        self.input_token = TextField(
            helper_text="Enter your Telegram Bot Token",
            helper_style=TextStyle(
                size=SUBITITLE_SIZE,
                color="#0F1923",
            ),
            data="Token",
            label="",
            border=InputBorder.UNDERLINE,
            border_color=LIGHT_PURPLE,
            color=DARK_PURPLE,
        )

        # ENTRADA DE DADOS DO CHAT ID DO CANAL OU GRUPO
        self.input_chat_id = TextField(
            helper_text="Enter your chat channel ID or telegram group",
            helper_style=TextStyle(
                size=SUBITITLE_SIZE,
                color="#0F1923",
            ),
            data="Chat Id",
            label="",
            border=InputBorder.UNDERLINE,
            border_color=LIGHT_PURPLE,
            color=DARK_PURPLE,
        )

        # ENTRADA DE DADOS COM OPÇÕES DE GAMES
        self.input_game = Dropdown(
            helper_text="Choose which game",
            helper_style=TextStyle(
                size=SUBITITLE_SIZE,
                color="#0F1923",
            ),
            data="Game",
            border=InputBorder.UNDERLINE,
            border_color=LIGHT_PURPLE,
            # color=DARK_PURPLE,
            options=[
                dropdown.Option(text="Fortune Double"),
                dropdown.Option(text="Roulett Double"),
            ]
        )

        # CAMPOS DE ENTRADA DE DADOS DO BOT
        self.fields = [
            self.input_name, self.input_token, self.input_chat_id,
            self.input_game
        ]

        # CAMPO DE ENTRADA DE DEFAULT CONTAINER
        self.input_row_display_default = Row(
            controls=[
                Text(
                    value="Click on colors or numbers to define a pattern",
                    size=15,
                    weight="bold",
                )
            ]
        )

        # BOTÃO DE LIMPAR O CAMPO DO PADRÃO EM VIGOR
        self.button_crear_default = IconButton(
            icon=icons.DELETE_ROUNDED,
            icon_size=15,
            icon_color="#F22C4D",
            # bgcolor=DARK_PURPLE,
            on_click=self.clear_input_default
        )

        # BOTÃO DE DESFAZER O CAMPO DO PADRÃO EM VIGOR
        self.button_undo_default = IconButton(
            icon=icons.UNDO_ROUNDED,
            icon_size=15,
            icon_color="#0285c7",
            on_click=self.undo_default
        )

        # BOTÃO DE REFAZER O CAMPO DO PADRÃO EM VIGOR
        self.button_redo_default = IconButton(
            icon=icons.REDO_ROUNDED,
            icon_size=15,
            icon_color="#0285c7",
            on_click=self.redo_default
        )

        # ENTRADA DE DADOS PARA A QUANTIDADE DE GALES INPOSTA NO BOT
        self.input_gales_bot = TextField(
            width=100,
            text_align="center",
            helper_text="Number of guess",
            helper_style=TextStyle(
                size=SUBITITLE_SIZE,
                color="#0F1923",
            ),
            data="Chat Id",
            label="",
            border=InputBorder.UNDERLINE,
            border_color=LIGHT_PURPLE,
            color=DARK_PURPLE,
        )

        # ENTRADA DE DADOS PARA A VITORIA IMPOSTA AO PADRÃO
        self.input_victory_in = Dropdown(
            helper_text="Victory in",
            helper_style=TextStyle(
                size=SUBITITLE_SIZE,
                color="#0F1923",
            ),
            data="victory_in",
            border=InputBorder.UNDERLINE,
            border_color=LIGHT_PURPLE,
            bgcolor=LIGHT_PURPLE,
            options=[
                dropdown.Option(text="Red and Panda"),
                dropdown.Option(text="Black and Panda"),
            ]
        )

        # COLUNAS DO DISPLAY PARA APRESENTAR OS PADROES DO BOT
        self.column_display_black = Column(
            controls=[
                Text("Victory in Black")
            ]
        )
        self.column_display_red = Column(
            controls=[
                Text("Victory in Red")
            ]
        )

        # LINHA RESPONSIVA DE TODOS OS CONTEUDOS DA PAGINA DE ADIÇÃO DE BOTS
        self.responsive_row_display = ResponsiveRow(
            controls=[
                Row(
                    controls=[
                        Text(value="Add Bots", size=30)
                    ],
                    alignment="center"
                ),
                Text(
                    value="Bot data",
                    size=20,
                    weight="bold",
                ),
                # Divider(thickness=1.5)
            ],
        )

        # DIV DO DISPLAY PRINCIPAL CONTENDO UM CONTAINER QUE TEM UMA COLUNA
        self.display_content: Container = Container(
            padding=padding.only(10, 20, 10, 20),
            margin=margin.symmetric(vertical=-30),
            border_radius=border_radius.only(top_left=30, top_right=30),
            bgcolor=LIGHT_ORANGE,
            content=self.responsive_row_display
        )

        # INSERÇÂO DOS CAMPOS NA GRID VIEW DA PAGINA
        self.controls = [
            self.menuapp,
            self.actions,
            self.display_content
        ]

        # INICIANDO A INSERÇÃO DOS CAMPOS DE ENTRADA DE DADOS
        self.insert_dinamic_fields()

        self.insert_dinamic_fields_defaults()

        self.insert_dinamic_fields_by_gales_victory_in()

    # FUNÇÃO RESPONSAVEL POR REALIZAR A INSERÇÂO DINAMICA DOS INPUTS DE ADIÇÃO
    # INSERINDO CARDS EM UMA LINHA RESPONSSIVA
    def insert_dinamic_fields(self):

        for i in self.fields:
            self.responsive_row_display.controls.append(
                AddBot._create_card_addbots(
                    {"xs": 12, "sm": 6, "md": 4, "xl": 3},
                    AddBot._create_container_card(
                        content=Column(
                            controls=[
                                Text(
                                    value=i.data,
                                    color=DARK_PURPLE,
                                    size=15
                                ),
                                i,
                                Row(
                                    controls=[
                                        TextButton(
                                            data=i.data,
                                            text="Clear",
                                            style=ButtonStyle(
                                                color={
                                                    "": LIGHT_PURPLE,
                                                    "hovered": "#F1F1F1",
                                                },
                                                bgcolor={
                                                    "": LIGHT_ORANGE,
                                                    "hovered": DARK_ORANGE
                                                },
                                                animation_duration=300,
                                            ),
                                            on_click=self.clear_field
                                        )
                                    ]
                                )
                            ],
                            horizontal_alignment="center"
                        )
                    )
                )
            )

        self.page.update()

        return

    # FUNÇÃO COMPLEMENTAR PARA REALIZAR A LIMPEZA DOS CAMPOS DINAMICAMENTE
    def clear_field(self, event) -> None:
        for index, control in enumerate(["Name", "Token", "Chat Id", "Game"]):
            if control == str(event.control.data):
                self.fields[index].value = ""
                self.page.update()

# -----------------------------------------------------------------------------------#
    # FUNÇÕES PARA INSERÇÃO DE CAMPOS DINAMICAMENTE DA TELA DE ADIÇÃO DE BOT
    def insert_dinamic_fields_defaults(self):

        # Image do botão panda
        image_panda = Image(
            src="assets/image/panda-1.png",
            width=BUTTONS_SIZE,
            height=BUTTONS_SIZE,
            border_radius=BORDER_RADIUS_DEFAULT
        )

        # Parametros para os botões de cores mais o bohtão do panda
        params_by_color = [
            (
                image_panda, None, False, "yellow",
                self.insert_color_into_display_default
            ),
            (
                None, "#F22C4D", True, "red",
                self.insert_color_into_display_default
            ),
            (
                None, "#6448e0", True, "black",
                self.insert_color_into_display_default
            ),
            (
                None, "#0285c7", True, "all",
                self.insert_color_into_display_default
            )
        ]

        params_by_number_red = [
            (
                Image(
                    src=f"assets/image/{path}",
                    width=BUTTONS_SIZE,
                    height=BUTTONS_SIZE,
                    border_radius=BORDER_RADIUS_DEFAULT
                ),
                None,
                False,
                path,
                self.insert_number_into_display_default
            )
            for path in self.src_numbers_red
        ]

        params_by_number_black = [
            (
                Image(
                    src=f"assets/image/{path}",
                    width=BUTTONS_SIZE,
                    height=BUTTONS_SIZE,
                    border_radius=BORDER_RADIUS_DEFAULT
                ),
                None,
                False,
                path,
                self.insert_number_into_display_default
            )
            for path in self.src_numbers_black
        ]

        controls_edit_by_color = [
            AddBot._create_container_selection_color(*i)
            for i in params_by_color
        ]

        controls_by_number_red = [
            AddBot._create_container_selection_color(*i)
            for i in params_by_number_red
        ]

        controls_by_number_black = [
            AddBot._create_container_selection_color(*i)
            for i in params_by_number_black
        ]

        # INSERE O TITULO DA DIV
        self.responsive_row_display.controls.append(
            Text(
                value="Defaults",
                size=20,
                weight="bold"
            )
        )

        # BOTÃO DE ADIÇÃO DO PADRÃO AO DISPLAY
        button_add_default = Row(
            controls=[
                ElevatedButton(
                    content=Text(
                        value="Add-Default",
                        color="#6448e0"
                    ),
                    style=ButtonStyle(
                        elevation={
                            "": 10,
                            "hovered": 25
                        },
                        side={
                           "": BorderSide(0, LIGHT_ORANGE),
                           "hovered": BorderSide(1, DARK_ORANGE),
                        },
                        shadow_color={
                            "": DARK_ORANGE,
                            "hovered": DARK_ORANGE
                        },
                        bgcolor=LIGHT_ORANGE,
                        padding={
                            "": 5,
                            "hovered": 10
                        }
                    ),
                    on_click=self.insert_default_into_column
                )
            ],
            alignment="end"
        )

        # INSESRE ENTRADA DE DADOS DO PADRÃO
        self.responsive_row_display.controls.append(
            Column(
                col={"xs": 12, "md": 4},
                controls=[
                    # CARD PADRÃO
                    AddBot._create_card_addbots(
                        {"xs": 12, "sm": 6},
                        AddBot._create_container_card(
                            Column(
                                controls=[
                                    Text("padrao"),
                                    self.input_row_display_default,
                                    button_add_default
                                ]
                            )
                        )
                    ),
                    # CARD EDITAR PADRÃO
                    AddBot._create_card_addbots(
                        {"xs": 12, "sm": 6},
                        AddBot._create_container_card(
                            Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Text("Editar"),
                                            Text("By color")
                                        ],
                                        alignment="spaceBetween"
                                    ),
                                    Row(
                                        controls=[
                                            Row(
                                                controls=[
                                                    self.button_crear_default,
                                                    self.button_undo_default,
                                                    self.button_redo_default,
                                                ]
                                            ),
                                            Row(
                                                controls=controls_edit_by_color
                                            )
                                        ],
                                        alignment="spaceBetween"
                                    )
                                ]
                            )
                        )
                    ),
                    AddBot._create_card_addbots(
                        {"xs": 12, "sm": 6},
                        AddBot._create_container_card(
                            Column(
                                controls=[
                                    Text(
                                        "By Number"
                                    ),
                                    Column(
                                        controls=[
                                            Row(
                                                controls_by_number_red
                                            ),
                                            Row(
                                                controls_by_number_black
                                            ),
                                        ]
                                    )
                                ]
                            )
                        )
                    )
                ]
            )
        )
        # INSERINDO O DISPLAY DOS PADROES DE RED A ADICIONAR AO BOT
        self.responsive_row_display.controls.append(
            AddBot._create_card_addbots(
                col={"xs": 12, "sm": 6, "md": 4},
                content=AddBot._create_container_card(
                    self.column_display_red
                )
            )
        )
        # INSERINDO O DISPLAY DOS PADROES DE BLACK A ADICIONAR AO BOT
        self.responsive_row_display.controls.append(
            AddBot._create_card_addbots(
                col={"xs": 12, "sm": 6, "md": 4},
                content=AddBot._create_container_card(
                    self.column_display_black
                )
            )
        )

        self.page.update()

    def insert_number_into_display_default(self, event):
        params_by_number = []
        params_by_number_red = [
            (
                Image(
                    src=f"assets/image/{path}",
                    width=BUTTONS_SIZE,
                    height=BUTTONS_SIZE,
                    border_radius=BORDER_RADIUS_DEFAULT
                ),
                None,
                False,
                path,
                self.insert_number_into_display_default
            )
            for path in self.src_numbers_red
        ]

        params_by_number_black = [
            (
                Image(
                    src=f"assets/image/{path}",
                    width=BUTTONS_SIZE,
                    height=BUTTONS_SIZE,
                    border_radius=BORDER_RADIUS_DEFAULT
                ),
                None,
                False,
                path,
                self.insert_number_into_display_default
            )
            for path in self.src_numbers_black
        ]

        params_by_number.extend(params_by_number_red)
        params_by_number.extend(params_by_number_black)
        params = []
        params.extend(self.src_numbers_red)
        params.extend(self.src_numbers_black)

        for index, field in enumerate(params):
            try:
                if isinstance(
                    self.input_row_display_default.controls[0],
                    Text
                ):
                    self.input_row_display_default.controls.clear()
            except IndexError:
                pass
            if field == event.control.data:
                self.input_row_display_default.controls.append(
                    AddBot._create_container_selection_color(
                        *params_by_number[index]
                    )
                )
                self.page.update()
                break

    def insert_color_into_display_default(self, event):

        image_panda = Image(
            src="assets/image/panda-1.png",
            width=BUTTONS_SIZE,
            height=BUTTONS_SIZE,
            border_radius=BORDER_RADIUS_DEFAULT
        )

        params = [
            (
                image_panda, None, False, "yellow",
                self.insert_color_into_display_default
            ),
            (
                None, "#F22C4D", True, "red",
                self.insert_color_into_display_default
            ),
            (
                None, "#6448e0", True, "black",
                self.insert_color_into_display_default
            ),
            (
                None, "#0285c7", True, "all",
                self.insert_color_into_display_default
            )
        ]

        fields = (
            "yellow", "red", "black", "all"
        )

        for index, field in enumerate(fields):
            try:
                if isinstance(
                    self.input_row_display_default.controls[0],
                    Text
                ):
                    self.input_row_display_default.controls.clear()
            except IndexError:
                pass
            if field == event.control.data:
                self.input_row_display_default.controls.append(
                    AddBot._create_container_selection_color(*params[index])
                )
                self.page.update()
                break

    def insert_dinamic_fields_by_gales_victory_in(self):
        self.responsive_row_display.controls.append(
            AddBot._create_card_addbots(
                {"xs": 12, "sm": 6, "md": 2},
                AddBot._create_container_card(
                    Row(
                        controls=[
                            IconButton(
                                icon=icons.EXPOSURE_MINUS_1,
                                icon_color=DARK_PURPLE,
                                on_click=self.subtract_gale,
                            ),
                            self.input_gales_bot,
                            IconButton(
                                icon=icons.EXPOSURE_PLUS_1_ROUNDED,
                                icon_color=DARK_PURPLE,
                                on_click=self.add_gale
                            ),
                        ],
                        alignment="spaceAround"
                    )
                )
            )
        )
        self.responsive_row_display.controls.append(
            AddBot._create_card_addbots(
                {"xs": 12, "sm": 6, "md": 2},
                AddBot._create_container_card(
                    self.input_victory_in
                )
            )
        )
        self.responsive_row_display.controls.append(
            Row(
                col={"xs": 12, "md": 12},
                controls=[
                    ElevatedButton(
                        content=Text(
                            value="Add-Bot",
                            color="#6448e0"
                        ),
                        style=ButtonStyle(
                            elevation={
                                "": 10,
                                "hovered": 25
                            },
                            side={
                                "": BorderSide(0, LIGHT_ORANGE),
                                "hovered": BorderSide(1, DARK_ORANGE),
                            },
                            shadow_color={
                                "": DARK_ORANGE,
                                "hovered": DARK_ORANGE
                            },
                            bgcolor=LIGHT_ORANGE,
                            padding={
                                "": 10,
                                "hovered": 15
                            }
                        ),
                        on_click=self.insert_bot_into_database
                    )
                ],
                alignment="end"
            )
        )
        self.responsive_row_display.controls.append(
            Divider(thickness=1.5, color="transparent")
        )
        self.page.update()

# ___________________________________________________________________________________#

# -----------------------------------------------------------------------------------#
    # FUNÇÃO RESPONSAVEL POR INSERIR PADRÃO NA COLUNA DA COR CORRETA
    def insert_default_into_column(self, event):
        id_button = CreateObjectId()
        # resolve = CreateObjectDefalt()

        if isinstance(self.input_row_display_default.controls[0], Text):
            return
        if not self.input_victory_in.value:
            self.input_victory_in.error_text = "Please insert victory!"
            self.page.update()
            return
        self.input_victory_in.error_text = ""
        if self.input_victory_in.value == "Red and Panda":
            controls = self.input_row_display_default.controls.copy()
            controls.append(
                IconButton(
                    data=len([i for i in self.column_display_red.controls if isinstance(i, Row)]),
                    icon=icons.DELETE_ROUNDED,
                    icon_color="#6448e0",
                    on_click=self.delete_default_red
                )
            )
            self.column_display_red.controls.append(
                Row(
                    data=id_button(),
                    controls=controls
                )
            )
        if self.input_victory_in.value == "Black and Panda":
            controls = self.input_row_display_default.controls.copy()
            controls.append(
                IconButton(
                    data=len([i for i in self.column_display_black.controls if isinstance(i, Row)]),
                    icon=icons.DELETE_ROUNDED,
                    icon_color="#6448e0",
                    on_click=self.delete_default_black
                )
            )
            self.column_display_black.controls.append(
                Row(
                    data=id_button(),
                    controls=controls
                )
            )
        self.input_row_display_default.controls.clear()
        self.input_row_display_default.controls.append(
            Text(
                value="Click on colors or numbers to define a pattern",
                size=15
            )
        )
        self.page.update()
# ___________________________________________________________________________________#

    # FUNCÃO RESPONSAVEL POR LIMPAR O CAMPO DE PADRÃO
    def clear_input_default(self, event):
        self.input_row_display_default.controls.clear()
        self.input_row_display_default.controls.append(
            Text(
                value="Click on colors or numbers to define a pattern",
                size=15
            )
        )
        self.page.update()

    # FUNÇÃO RESPONSAVEL POR DESFAZER ULTIMA AÇÃO
    def undo_default(self, event):

        if isinstance(self.input_row_display_default.controls[0], Text):
            return

        elif len(self.input_row_display_default.controls) == 1:
            self._cache.append(self.input_row_display_default.controls.pop())
            self.input_row_display_default.controls.append(
                Text(
                    value="Click on colors or numbers to define a pattern",
                    size=15,
                    weight="bold",
                )
            )
            self.page.update()
            return

        self._cache.append(self.input_row_display_default.controls.pop())
        self.page.update()

    # FUNÇÃO RESPONSAVEL POR REFAZER ULTIMA AÇÃO
    def redo_default(self, event):

        if not len(self._cache):
            return

        if isinstance(self.input_row_display_default.controls[0], Text):

            self.input_row_display_default.controls.clear()

            self.input_row_display_default.controls.append(
                self._cache.pop()
            )

            self.page.update()
            return

        self.input_row_display_default.controls.append(
            self._cache.pop()
        )

        self.page.update()
        return

    # FUNÇÃO RESPONSAVEL POR ADICIONAR MAIS UM NO VALOR DO GALE
    def add_gale(self, event):
        now_value = self.input_gales_bot.value
        value = int(now_value) if now_value else 0
        value += 1
        self.input_gales_bot.value = str(value)
        self.page.update()

    # FUNÇÃO RESPONSAVEL POR SUBTRAIR MAIS UM NO VALOR DO GALE
    def subtract_gale(self, event):
        now_value = self.input_gales_bot.value
        value = int(now_value) if now_value else 0
        if value <= 0:
            return
        value -= 1
        self.input_gales_bot.value = str(value)
        self.page.update()

    # FUNÇÃO RESPONSAVEL POR DELETAR O PADRÃO EM VIGENCIA
    def delete_default_red(self, event):
        try:
            self.column_display_red.controls.pop(event.control.data + 1)
        except IndexError:
            self.column_display_red.controls.pop(event.control.data)

        self.page.update()

    # FUNÇÃO RESPONSAVEL POR DELETAR O PADRÃO EM VIGENCIA
    def delete_default_black(self, event):
        try:
            self.column_display_black.controls.pop(event.control.data + 1)
        except IndexError:
            self.column_display_black.controls.pop(event.control.data)

        self.page.update()

    # FUNÇÃO RESPONSAVEL POR INSERIR UM BOT NO BANCO DE DADOS
    def insert_bot_into_database(self, event):
        count = 0

        fields = [
            self.input_name, self.input_token, self.input_chat_id,
            self.input_game
        ]

        for field in fields:
            if not field.value:
                field.error_text = "Field Not Value!"
                count += 1
                self.page.update()
            field.error_text = ""
        if count:
            return

        for row in self.column_display_red.controls:
            if isinstance(row, Row):
                self.defaults["red"].append(
                    [content.data for content in row.controls]
                )
        for row in self.column_display_black.controls:
            if isinstance(row, Row):
                self.defaults["black"].append(
                    [content.data for content in row.controls]
                )
        if len(self.defaults["red"]) == 0 and len(self.defaults["black"]) == 0:
            return

        gales = self.input_gales_bot.value if self.input_gales_bot.value else 1

        bot = {
            "id_user": self.page.client_storage.get("_id"),
            "token": self.input_token.value,
            "chat_id": self.input_chat_id.value,
            "name": self.input_name.value,
            "statistics": self.statistics,
            "game": self.input_game.value,
            "defaults": self.defaults,
            "gales": gales
        }

        for field in fields:
            field.value = ""

        for index, row in enumerate(self.column_display_red.controls):
            if isinstance(row, Row):
                try:
                    self.column_display_red.controls.pop(index)
                except IndexError:
                    pass

        for index, row in enumerate(self.column_display_black.controls):
            if isinstance(row, Row):
                try:
                    self.column_display_black.controls.pop(index)
                except IndexError:
                    pass

        self.page.update()

        def dimiss(event):
            self.page.dialog.open = False
            self.page.update()

        alert_succes = CupertinoAlertDialog(
            title=Text("Sucess", color=DARK_GREEN_BANNER),
            content=Container(
                padding=10,
                content=Column(
                    controls=[
                        Text("Sucess Bot in Acont!", size=20, color=LIGHT_ORANGE),
                        ElevatedButton(
                            content=Text(
                                value="Ok",
                                color="#6448e0"
                            ),
                            style=ButtonStyle(
                                elevation={
                                    "": 10,
                                    "hovered": 25
                                },
                                side={
                                    "": BorderSide(0, LIGHT_ORANGE),
                                    "hovered": BorderSide(1, DARK_ORANGE),
                                },
                                shadow_color={
                                    "": DARK_ORANGE,
                                    "hovered": DARK_ORANGE
                                },
                                bgcolor=LIGHT_ORANGE,
                                padding={
                                    "": 5,
                                    "hovered": 10
                                }
                            ),
                            on_click=dimiss
                        )
                    ]
                )
            )
        )

        try:
            self.data.table("bot").insert(bot).execute()
            self.page.dialog = alert_succes
            self.page.dialog.open = True
            self.page.update()
        except Exception:
            pass
