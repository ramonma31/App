import re


class ColorsApp:
    def __init__(self) -> None:
        self._Light_purple = "#9A2ED9"
        self._Dark_purple = "#511F76"
        self._White = "#FFFFFF"
        self._Dark_orange = "#FF5319"
        self._Light_orange = "#FF8B00"

    @property
    def Light_purple(self):
        return self._Light_purple

    @Light_purple.setter
    def Light_purple(self, value):
        if re.search("#", value):
            self._Light_purple = value
            return

    @property
    def Dark_purple(self):
        return self._Dark_purple

    @Dark_purple.setter
    def Dark_purple(self, value):
        if re.search("#", value):
            self._Dark_purple = value
            return

    @property
    def White(self):
        return self._White

    @White.setter
    def White(self, value):
        if re.search("#", value):
            self._White = value
            return

    @property
    def Light_orange(self):
        return self._Light_orange

    @Light_orange.setter
    def Light_orange(self, value):
        if re.search("#", value):
            self._Light_orange = value
            return

    @property
    def Dark_orange(self):
        return self._Dark_orange

    @Dark_orange.setter
    def Dark_orange(self, value):
        if re.search("#", value):
            self._Dark_orange = value
            return
