from flet import TextStyle


class TextStyleApp:
    def __init__(self):
        super().__init__()

    def Title_style(self):
        return TextStyle(
            size=20,
            color="black",
            weight="bold"
        )

    def Button_Action_Style(self):
        return TextStyle(
            size=10,
            color="white",
            weight="bold"
        )
