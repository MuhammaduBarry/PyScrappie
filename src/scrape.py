import requests
from bs4 import BeautifulSoup


def html_page_one_parser() -> BeautifulSoup:
    # Return Response Code
    r: requests.Response = requests.get("https://news.ycombinator.com/news")
    # Parse text in html form
    soup: BeautifulSoup = BeautifulSoup(r.text, "html.parser")

    return soup

def html_page_two_parser() -> BeautifulSoup:
    r: requests.Response = requests.get("https://news.ycombinator.com/news?p=2")
    soup: BeautifulSoup = BeautifulSoup(r.text, 'html.parser')

    return soup

def sort_stories_by_vote(hnlist: list) -> list:
    return sorted(hnlist, key=lambda k:k["Vote"], reverse=True)

def create_custom_hn(links: list, subtext: list) -> list:
    hn: list = []

    for i, item in enumerate(links):
        title: str = links[i].getText()
        href: str = links[i].get("href", None)
        vote: list = subtext[i].select(".score")

        if len(vote):
            points: int = int(vote[0].getText().replace(" points", ""))
            if points > 100:
                hn.append({"Title": title, "Link": href, "Vote": points})

    return sort_stories_by_vote(hn)