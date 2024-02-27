from typing import Any

import httpx
import pendulum


class ApiBlaze:

    URLS = [
        "https://blaze-7.com/api/singleplayer-originals/originals/fortune_double_games/history/analytics/1?page=",
        "http://blaze-7.com/api/roulette_games/history?page="
    ]

    @classmethod
    def _create_url_change(cls, page, game):
        return f"{cls.URLS[game]}{page}"

    def __init__(self, page, game) -> None:
        self._url = ApiBlaze._create_url_change(
        ) if page is None else ApiBlaze._create_url_change(page, game)
        self._page = page if page is not None else 1
        self._game = game if game is not None else 0

    @property
    def url(self):
        return self._url

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value if value in range(1, 289) else 1
        self._url = ApiBlaze._create_url_change(self.page, self.game)

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, value):
        self._game = value if value in (0, 1) else 0
        self._url = ApiBlaze._create_url_change(self.page, self.game)


class SearchResult(ApiBlaze):
    def __init__(self, page, game) -> None:
        super().__init__(page, game)

    def search(self, pages=None) -> Any:
        list_results = []
        if pages:
            for i in range(pages[0], pages[1]):
                self.page = i
                get_api = httpx.get(self.url)
                if get_api.status_code == 200:
                    list_results.extend(
                        get_api.json()["records"]
                    )
            self.page = 1
            return list_results
        get_api = httpx.get(self.url)
        if get_api.status_code == 200:
            return get_api.json()["records"]
        return list_results


class GetResult(SearchResult):
    def __init__(self, page=1, game=0) -> None:
        super().__init__(page, game)

    def get_last_result(self):
        return self.search()[0]

    def get_results_by_color(self, color: str):
        return [i for i in self.search((1, 3)) if i["color"] == color]

    def get_results_by_roll(self, roll: str):
        return [i for i in self.search((1, 3)) if i["roll"] == roll]

    def get_results_by_time(self, hour: str):
        return [
            i for i in self.search((1, 3))
            if pendulum.parse(i["created_at"]).subtract(
                hours=3
            ).format("HH:mm") == hour
        ]

    def get_results_by_index(self, index):
        if isinstance(index, tuple):
            return self.search()[index[0]:index[1]]
        return self.search()[index]

    def percent_by_color(self):
        results = self.search(pages=(1, 3))
        qtd_red = len([i["color"] for i in results if i["color"] == "red"])
        qtd_black = len([i["color"] for i in results if i["color"] == "black"])
        qtd_white = len([i["color"] for i in results if i["color"] == "white"])
        total = qtd_red + qtd_black + qtd_white
        percent_red = qtd_red / total * 100
        percent_black = qtd_black / total * 100
        percent_white = qtd_white / total * 100
        return {
            "red": percent_red,
            "black": percent_black,
            "white": percent_white,
        }
