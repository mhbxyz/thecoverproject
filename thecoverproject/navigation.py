from typing import Any

import requests
from bs4 import BeautifulSoup, Tag
from requests import Response

from thecoverproject import urls, Consoles, Handhelds, Computers, PageIndex
from thecoverproject.urls import index_opt


def get_game_system_page_data(game_system: Consoles | Handhelds | Computers, index: PageIndex) -> list[dict]:

    buffer: Any
    game_system_url: str
    request: Response

    game_system_url = urls.game_systems[game_system] + index_opt.format(index.value)
    request = requests.get(game_system_url)
    buffer = BeautifulSoup(request.text, 'html.parser')
    buffer = buffer.find("table", class_="tblSpecs")
    rows = buffer.find_all("tr")

    def get_data(row: Tag):

        name: str
        nb_of_covers: int
        name_text: str

        name_text = row.td.text.strip()
        if name_text[-1] == ")":
            name_text_table = name_text.rsplit(" ", 1)
            name = name_text_table[0]
            nb_of_covers = int(name_text_table[1].strip("()"))
        else:
            name = name_text
            nb_of_covers = 1

        return {
            "name": name,
            "nb_of_covers": nb_of_covers,
            "url": urls.home + row.td.span.a.get("href")
        }

    return [get_data(row) for row in rows]
