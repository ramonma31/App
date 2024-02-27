import re
from typing import List
# from user import User
# import pendulum as dtp
# from flet_core.client_storage import ClientStorage
import flet as f
from supabase import Client

# colors to app
DARK_GREEN_BANNER = "greenaccent700"
LIGHT_GREEN_BANNER = "greenaccent200"
DARK_PURPLE = "#511F76"
LIGHT_PURPLE = "#9A2ED9"
LIGHT_ORANGE = "#FF8B00"
DARK_ORANGE = "#FF5319"
BORDER_INPUT = "#fbd80c"
CYAN_BUTTON_STYLE = "#1D223A"
WHITE_BUTTON_STYLE = "#FEFDFC"

# alignments to app
NONE = None
START = "start"
END = "end"
CENTER = "center"
SPACE_BETWEEN = "spaceBetween"
SPACE_AROUND = "spaceAround"
SPACE_EVENLY = "spaceEvenly"

metrics = """\
💻 Metricas

Quantidade de sinais: {}

Wins: {}
Wins de primeira: {}
Wins no gale: {}
Reds: {}
🎯 Acertos {}
Estamos a {} wins seguidos!"""

signal = """\
🎲 ENTRADA CONFIRMADA!

🎰 Apostar no {}
🎰 Após o {} {}
⚪️ Proteger no Branco
🔁 Fazer até {} gales

📱 Fortune Double"""


class Login(f.View):
    @staticmethod
    def _validate_email(email):
        patterns = ("@gmail.com", "@yahoo.com", "@outlook.com")
        for i in patterns:
            if re.search(i, email):
                return True
        return False

    def __init__(self, page: f.Page, data: Client) -> None:
        super(Login, self).__init__(
            route="/",
            spacing=5,
            horizontal_alignment=f.CrossAxisAlignment.CENTER,
            vertical_alignment=f.MainAxisAlignment.START,
            padding=15,
            bgcolor=DARK_PURPLE,
            scroll=True,
        )

        self.data = data

        self.page = page

        self.image_app_bar_layout = f.Container(
            content=f.Image(
                src="assets/image/PandaFundo.png",
                fit=f.ImageFit.CONTAIN,
                width=500
            )
        )

        self.text_input_style = f.TextStyle(
            size=15,
            weight=f.FontWeight.W_500,
        )

        self.buttons_style = f.ButtonStyle(
            color={
                "": WHITE_BUTTON_STYLE,
                "hovered": LIGHT_PURPLE,
            },
            bgcolor={
                "": CYAN_BUTTON_STYLE,
                "hovered": LIGHT_ORANGE
            },
            elevation={"hovered": 10},
            animation_duration=350
        )

        self.input_email = f.TextField(
            border_radius=f.border_radius.all(30),
            border_width=1,
            hint_text="example@email.com",
            text_style=self.text_input_style,
            width=320,
            tooltip="E-mail accont",
            border_color=LIGHT_PURPLE,
            focused_border_width=3,
            focused_border_color=BORDER_INPUT
        )

        self.input_password = f.TextField(
            hint_text="password",
            border_radius=f.border_radius.all(30),
            border_width=1,
            text_style=self.text_input_style,
            width=320,
            tooltip="Passoword accont",
            password=True,
            can_reveal_password=True,
            border_color=LIGHT_PURPLE,
            focused_border_width=3,
            focused_border_color=BORDER_INPUT
        )

        self.button_enter = f.ElevatedButton(
            text="Enter",
            style=self.buttons_style,
            on_click=self.login_in_app
        )

        self.button_sign_up = f.ElevatedButton(
            data="Signup",
            text="sign up",
            style=self.buttons_style,
            on_click=self.sign_up_change
        )

        self.button_cancel = f.ElevatedButton(
            "Cancel",
            style=self.buttons_style
        )

        self.controls = [
                self.create_column_display_login()
        ]

    # DEFINE TO TABLE FOR DISPLAY LOGIN INPUT FIELDS
    def create_column_display_login(
        self,
        width=340,
        fields=("User Name", "Password")
    ) -> f.Column:

        column_return = f.Column(
            controls=[
                self.image_app_bar_layout
            ],
            width=width,
            alignment=CENTER
        )

        input_fields: List[f.Control] = [
            self.input_email, self.input_password
        ]

        for index, field in enumerate(input_fields):
            # ADD LABEL FOR INPUTS FIELDS
            column_return.controls.append(
                f.Row(
                    controls=[
                        f.Text(
                            value=f"{fields[index]}",
                            size=20,
                            weight="bold",
                            color=LIGHT_ORANGE,
                        )
                    ],
                    alignment=CENTER
                )
            )
            # ADD INPUT FIELDS FOR LOGIN
            column_return.controls.append(
                f.Row(
                    controls=[
                        field
                    ],
                    alignment=CENTER
                )
            )

        # ADD BUTTONS ACTIONS TO LOGIN/REGISTER
        column_return.controls.append(
            f.Row(
                controls=[
                    self.button_enter,
                    self.button_sign_up,
                    self.button_cancel
                ],
                alignment=SPACE_BETWEEN
            )
        )
        return column_return

    def login_in_app(self, e):
        def close_banner(e):
            self.page.banner.open = False
            self.page.update()
        count = 0
        for field in (self.input_email, self.input_password):
            if not field.value:
                count += 1
                field.error_text = "Empity field!"
            else:
                field.error_text = ""
            self.page.update()
        if count:
            return

        if not Login._validate_email(self.input_email.value):
            self.input_email.error_text = "E-mail invalid!"
            self.page.update()
            return

        # CROUD IN DATABASE
        data = self.data.table("user").select("*").eq(
            "password", self.input_password.value
        ).eq("email", self.input_email.value).execute()

        # BLOCK DEFINE YOU REGISTRED ACCONT IF NOT REGISTER OPEN BANNER ALERT
        try:
            if data.data[0]["signature"]:
                # CONVERT YOU DATE FOR USER
                self.page.client_storage.set("_id", data.data[0]["id_user"])
                bots = self.data.table("templates").select("*").eq(
                    "id_user", data.data[0]["id_user"]
                ).execute()
                if not bots.data:
                    self.create_templates_initiais(data)
                try:
                    self.page.banner.open = False
                    self.page.update()
                except AttributeError:
                    pass
                self.page.go("/home")
                return

            banner = f.Banner(
                bgcolor="amber100",
                leading=f.Icon(
                    name="warning_amber_rounded",
                    color="amber"
                ),
                content=f.Text(
                    "Suspended subscription contact your administrator!",
                    color=f.colors.BLACK
                ),
                actions=[
                    f.TextButton("Ok!", on_click=close_banner),
                ],
            )
            self.page.banner = banner
            self.page.banner.open = True
            self.page.update()
            return
        except IndexError:
            banner = f.Banner(
                bgcolor="amber100",
                leading=f.Icon(
                    name="warning_amber_rounded",
                    color="amber",
                    size=40
                ),
                content=f.Text(
                    value="Accont not registred! Please register in app",
                    color="black"
                ),
                actions=[
                    f.TextButton("Ok!", on_click=close_banner),
                ],
            )
            self.page.banner = banner
            self.page.banner.open = True
            self.page.update()
            return

    def sign_up_change(self, event):
        try:
            self.page.banner.open = False
        except AttributeError:
            pass
        self.page.go("/signup")
        return

    def create_templates_initiais(self, data):
        templates = [
            {
                "name": "gren",
                "template": "✅✅✅Win✅✅✅",
                "id_user": data.data[0]["id_user"],
            },
            {
                "name": "red",
                "template": "❌❌❌Loss❌❌❌",
                "id_user": data.data[0]["id_user"],
            },
            {
                "name": "signal",
                "template": signal,
                "id_user": data.data[0]["id_user"],
            },
            {
                "name": "metrics",
                "template": metrics,
                "id_user": data.data[0]["id_user"],
            },
            {
                "name": "gales",
                "template": "Vamos para o gale {}",
                "id_user": data.data[0]["id_user"],
            },
            {
                "name": "white",
                "template": "🟡🟡🟡WIN {}x🟡🟡🟡",
                "id_user": data.data[0]["id_user"],
            },
        ]
        for template in templates:
            self.data.table("templates").insert(template).execute()
