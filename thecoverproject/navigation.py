from re import Match, match
from typing import Any, List

import requests
from bs4 import BeautifulSoup, Tag, PageElement, ResultSet
from requests import Response

from thecoverproject import urls, Console, Handheld, Computer, PageIndex, Region
from thecoverproject.exceptions import UnknownRegionError
from thecoverproject.urls import index_opt
from thecoverproject.utils import construct_url


def _get_description_data(description: Tag) -> dict:

    thumbnail_url: str = construct_url(description.img.get("src"))
    cover_url: str = construct_url(description.a.get("href"))

    description.h2.extract()
    description.h3.extract()

    img: Tag
    for img in description.select('img'):
        img.extract()

    description_content: List[PageElement]
    description_content = description.contents

    # get the text of the last page element, split it using spaces
    # and get the nb of downloads in the fith cell of the splitted string
    nb_of_downloads = int(description_content[-1].text.strip().split(" ")[5])

    description_content = [tag for tag in description_content[0:-1] if tag.name != "br"]

    return {
        "description": description_content[0].split(":")[1].strip(),
        "format": description_content[1].split(":")[1].strip(),
        "created_by": description_content[2].split(":")[1].strip(),
        "region": description_content[3].split(":")[1].strip(),
        "case_type": description_content[4].split(":")[1].strip(),
        "nb_of_downloads": nb_of_downloads,
        "urls": {
            "thumbnail": thumbnail_url,
            "download": cover_url,
        },
    }


def _get_other_covers_data(other_covers: Tag, current_cover_thumbnail_url: str) -> list:

    others_covers_table: ResultSet

    other_covers.find("li", class_="tabHeader").extract()  # removes useless table header
    others_covers_table = other_covers.find_all("li")  # Splits the covers table into a list

    li: PageElement
    related_covers = list()
    for li in others_covers_table:

        thumbnail_url: str
        content: List[Tag]
        span_content: List[PageElement]
        regex: Match
        region_code: str

        if not li.attrs == {} and "tabSelected" in li.attrs["class"]:  # Checks if we are on the current selected cover
            thumbnail_url = current_cover_thumbnail_url
        else:
            regex = match(r"showThumb\('[0-9]+', '(?P<url>[\w./_:]+)'\)", li.a.get("onmouseover"))
            thumbnail_url = construct_url(regex.group("url"))

        content = [tag for tag in li.a.contents if tag.name != "br"]  # Removes br tag at pos 1
        span_content = content[1].contents

        # Gets a region code from the flag icon url using a regex
        regex = match(r"\/images\/flags\/(?P<region>[a-z]+)\.png", span_content[-1].get("src"))
        region_code = regex.group("region")

        if region_code not in list(Region.__members__.keys()):
            raise UnknownRegionError(region_code)

        related_covers.append({
            "description": content[0].text.strip(),
            "format": span_content[0].text.split(" ")[-1],  # Gets span tag content then split text before br tag
            "region": {k: v for k, v in Region.__members__.items()}[region_code].value,
            "urls": {
                "thumbnail": thumbnail_url,
                "cover": construct_url(li.a.get("href")),
            },
        })

    return related_covers


def _get_description_and_covers_data_cells(game_id: int) -> tuple[Tag, Tag]:

    game_url: str
    request: Response
    buffer: Any
    others_covers: Tag
    description: Tag
    related_covers: list
    data_cells: list[Tag, Tag]

    game_url = urls.game_page.format(game_id)
    request = requests.get(game_url)
    buffer = BeautifulSoup(request.text, 'html.parser')
    buffer = buffer.find("td", class_="pageBody")
    data_cells = buffer.find_all("td", class_="pageBody")  # Gets the data cells with cover details and others covers

    return data_cells[0], data_cells[1]


def get_game_covers_data(game_id: int) -> list[dict]:
    covers, description = _get_description_and_covers_data_cells(game_id)
    thumbnail_url: str = construct_url(description.img.get("src"))
    return _get_other_covers_data(covers, thumbnail_url)


def get_game_page_data(game_id: int, with_images: bool = False) -> dict:

    covers, description = _get_description_and_covers_data_cells(game_id)
    data = _get_description_data(description)
    data["other_covers"] = _get_other_covers_data(covers, data["urls"]["thumbnail"])

    if with_images:
        data["images"] = {
            "thumbnail": requests.get(data["urls"]["thumbnail"]).content,
            "cover": requests.get(data["urls"]["download"]).content,
        }

    return data


def get_game_system_page_data(game_system: Console | Handheld | Computer, index: PageIndex) -> list[dict]:

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
            "url": construct_url(row.td.span.a.get("href"))
        }

    return [get_data(row) for row in rows]
