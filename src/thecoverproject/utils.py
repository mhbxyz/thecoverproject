import json

from thecoverproject import Platform, PageCategory
from thecoverproject.urls import home, platforms, game_page, cover_page, search_page, index_opt, page_opt


def construct_url(url: str):
    if not url.startswith("http"):
        if url.startswith("/"):
            return home + url
        else:
            return home + "/" + url
    return url


def construct_platform_url(platform: Platform, index: PageCategory, page_index: int = 1) -> str:
    return platforms[platform] + index_opt.format(index.value) + page_opt.format(page_index)


def construct_game_url(game_id: int) -> str:
    return game_page.format(game_id)


def construct_game_cover_url(cover_id: int) -> str:
    return cover_page.format(cover_id)


def construct_search_url(research_topic: str, page_index: int = 1) -> str:

    search_string: str

    search_string = research_topic.replace(" ", "+")
    return search_page.format(search_string) + page_opt.format(page_index)


def ppjson(data: list | dict, indent: int = 4):
    print(json.dumps(data, indent=indent))
