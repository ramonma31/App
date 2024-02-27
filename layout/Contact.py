import flet as f
from layout.colors import ColorsApp
from supabase import Client
from layout.appMenu import MenuApp
from layout.actions_buttons import ActionsMenu

colors = ColorsApp()


class Contact(f.View):
    def __init__(self, page: f.Page, data: Client) -> None:
        super(Contact, self).__init__(
            route="/contact",
            spacing=0,
            horizontal_alignment="center",
            auto_scroll=True
        )

        self.page = page

        self.data = data

        self.menuapp = MenuApp(self.page)
        self.actions = ActionsMenu(self.page)

        self.body_contact = f.ResponsiveRow(
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
                            f.Text("Contact")
                        ],
                    )
                )
            ]
        )

        self.controls = [
            self.menuapp,
            self.actions,
            self.body_contact
        ]
