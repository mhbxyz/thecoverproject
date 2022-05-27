from thecoverproject import urls, GameSystem, PageIndex
from urls import index_opt


def construct_url(url: str):
    if not url.startswith("http"):
        if url.startswith("/"):
            return urls.home + url
        else:
            return urls.home + "/" + url
    return url


def construct_game_system_url(game_system: GameSystem, index: PageIndex) -> str:
    return urls.game_systems[game_system] + index_opt.format(index.value)


def construct_game_page_url(game_id: int) -> str:
    return urls.game_page.format(game_id)


def construct_game_cover_url(cover_id: int) -> str:
    return urls.cover_page.format(cover_id)
