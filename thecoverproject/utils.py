from thecoverproject import urls, Platform, PageCategory
from urls import index_opt, page_opt


def construct_url(url: str):
    if not url.startswith("http"):
        if url.startswith("/"):
            return urls.home + url
        else:
            return urls.home + "/" + url
    return url


def construct_platform_url(platform: Platform, index: PageCategory, page_index: int = 1) -> str:
    return urls.platforms[platform] + index_opt.format(index.value) + page_opt.format(page_index)


def construct_game_url(game_id: int) -> str:
    return urls.game_page.format(game_id)


def construct_game_cover_url(cover_id: int) -> str:
    return urls.cover_page.format(cover_id)


def construct_search_url(research_topic: str, page_index: int = 1) -> str:

    search_string: str

    search_string = research_topic.replace(" ", "+")
    return urls.search_page.format(search_string) + page_opt.format(page_index)
