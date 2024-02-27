import flet as f
from layout.colors import ColorsApp
from layout.text_style import TextStyleApp

text = TextStyleApp()
colors = ColorsApp()


class ActionsMenu(f.Container):
    def __init__(self, page: f.Page) -> None:
        super(ActionsMenu, self).__init__(
            bgcolor=colors.Dark_purple,
            padding=20,
            margin=0,
            height=100,
        )
        # PAGE
        self.page = page
        # ICONS FOR LAYOUT
        self.icon_home = f.Icon(
            name=f.icons.HOME_ROUNDED,
            color=colors.White,
            size=30
        )
        self.icon_contact = f.Icon(
            name=f.icons.CONTACT_SUPPORT_OUTLINED,
            color=colors.White,
            size=30
        )

        # LABEL BUTON

        self.label_menu = f.Text(
            value="Menu",
            style=15
        )
        self.label_home = f.Text(
            value="Home",
            style=15
        )
        self.label_contact = f.Text(
            value="Contact",
            style=15
        )

        self.container_home = f.Container(
            ink=True,
            tooltip="Show Home",
            content=f.Row(
                controls=[
                    self.icon_home,
                    self.label_home
                ],
                spacing=1
            ),
            on_click=lambda e: self.page.go("/home")
        )
        self.container_contact = f.Container(
            ink=True,
            tooltip="Show Contact",
            content=f.Row(
                controls=[
                    self.icon_contact,
                    self.label_contact
                ],
                spacing=1
            ),
            on_click=lambda e: self.page.go("/contact")
        )

        self.content = f.Column(
            controls=[
                f.Row(
                    controls=[
                        self.container_home,
                        self.container_contact
                    ],
                    spacing=0,
                    alignment=f.MainAxisAlignment.SPACE_EVENLY
                )
            ]
        )

    def actions_responsive(self, larg: str, page: f.Page):
        if not isinstance(larg, str):
            return
        if larg == "low":
            for i in (
                self.icon_manu, self.icon_home, self.icon_contact
            ):
                i.size = 20
            for i in (
                self.label_menu, self.label_home, self.label_contact
            ):
                i.size = 10
        elif larg == "small":
            for i in (
                self.icon_manu, self.icon_home, self.icon_contact
            ):
                i.size = 25
            for i in (
                self.label_menu, self.label_home, self.label_contact
            ):
                i.size = 13
        elif larg == "medium":
            for i in (
                self.icon_manu, self.icon_home, self.icon_contact
            ):
                i.size = 30
            for i in (
                self.label_menu, self.label_home, self.label_contact
            ):
                i.size = 16
        elif larg == "larg":
            for i in (
                self.icon_manu, self.icon_contact, self.icon_home
            ):
                i.size = 35
            for i in (
                self.label_menu, self.label_home, self.label_contact
            ):
                i.size = 20
