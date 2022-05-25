from thecoverproject import urls


def construct_url(url: str):
    if not url.startswith("http"):
        if url.startswith("/"):
            return urls.home + url
        else:
            return urls.home + "/" + url
    return url
