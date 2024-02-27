import flet as f
from layout.colors import ColorsApp
from layout.text_style import TextStyleApp

text = TextStyleApp()
colors = ColorsApp()


class MenuApp(f.ResponsiveRow):
    def __init__(self, page: f.Page) -> None:
        super(MenuApp, self).__init__()
        self.page = page

        self.popup_manu_login = f.PopupMenuItem(content=f.Text("Login"))

        self.popup_manu_logout = f.PopupMenuItem(
            content=f.Text("Logout"),
            on_click=self.change_login
        )

        self.popup_manu_register = f.PopupMenuItem(
            content=f.Text("Registrar")
        )

        self.popup_manu_add_bot = f.PopupMenuItem(
            content=f.Text("Add Bot")
        )

        self.popup_manu_divider = f.PopupMenuItem()

        self.dialog_login = f.AlertDialog(
            title=f.Text(
                value="Login",
                style=f.TextStyle(
                    size=20,
                    weight="bold",
                    shadow=f.BoxShadow(spread_radius=2, blur_radius=2)
                )
            )
        )

        self.popup_menu_button = f.PopupMenuButton(
            icon=f.icons.LIST_OUTLINED,
            items=[
                self.popup_manu_login,
                self.popup_manu_divider,
                self.popup_manu_register,
                self.popup_manu_divider,
                self.popup_manu_add_bot,
                self.popup_manu_divider,
                self.popup_manu_logout,
            ]
        )

        self.image_app_layout = f.Image(
            src="assets/image/LogoApp.png",
            fit="contain",
            width=160,
            height=50
        )
        self.controls = [
            f.Column(
                col={"xs": 12, "sm": 12, "md": 12, "lg": 12},
                controls=[
                    f.Container(
                        padding=f.padding.only(left=3, right=3),
                        margin=0,
                        bgcolor=colors.Dark_purple,
                        content=f.Container(
                            padding=f.padding.only(left=30, right=30),
                            alignment=f.alignment.center,
                            bgcolor=colors.Light_orange,
                            border_radius=f.border_radius.only(
                                40, 40, 40, 40
                            ),
                            content=f.Row(
                                controls=[
                                    self.image_app_layout,
                                    self.popup_menu_button
                                ],
                                alignment=f.MainAxisAlignment.SPACE_BETWEEN
                            )
                        )
                    )
                ]
            )
        ]

    def change_login(self, e):
        try:
            self.page.client_storage.clear()
        except Exception:
            print("não ocorreu com sucesso")
        self.page.go("/")
