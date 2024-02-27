import os
import flet as f
# from actions_buttons import ActionsMenu
# from appMenu import MenuApp
from layout.addbot import AddBot
from layout.colors import ColorsApp
from layout.Contact import Contact
from layout.Home import Home
from layout.Menu import Menu
from layout.login import Login
from layout.signup import Signup
from layout.cardbot import CardBot
from supabase import Client, create_client


SUPABASE_URL = "https://houmarmlwjtrwgewztor.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJp"\
    "c3MiOiJzdXBhYmFzZSIsInJlZiI6ImhvdW1hcm1sd2p0cndnZXd6"\
    "dG9yIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDczNjgzODQsImV4"\
    "cCI6MjAyMjk0NDM4NH0.R_soji7iWXEZDne04EEa4NSkOa8pHP8A9pid5QsOnJg"

os.environ["SUPABASE_URL"] = SUPABASE_URL
os.environ["SUPABASE_KEY"] = SUPABASE_KEY

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
base: Client = create_client(url, key)


def main(page: f.Page):

    def route_change(route):
        page.views.clear()

        if page.route == "/":
            login = Login(page=page, data=base)
            page.views.append(login)
            page.update()

        elif page.route == "/signup":
            signup = Signup(page=page, data=base)
            page.views.append(signup)
            page.update()

        elif page.route == "/home":
            home = Home(page=page, data=base)
            page.views.append(home)
            page.update()

        elif page.route == "/menu":
            menu = Menu(page=page, data=base)
            page.views.append(menu)
            page.update()

        elif page.route == "/contact":
            contact = Contact(page=page, data=base)
            page.views.append(contact)
            page.update()

        elif page.route == "/cardbot":
            container = CardBot(
                page=page,
                data=page.client_storage.get("bot")
            )
            page.views.append(container)
            page.update()

        elif page.route == "/addbot":
            addbot = AddBot(page=page, data=base)
            page.views.append(addbot)
            page.update()

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.padding = 0
    page.spacing = 0
    page.scroll = "auto"
    page.fonts = {
        "protest_strike": "/fonts/ProtestStrike-Regular.ttf"
    }
    page.theme = f.Theme(font_family="protest_strike")
    page.bgcolor = ColorsApp().Dark_orange
    page.update()


if __name__ == "__main__":
    f.app(target=main)
