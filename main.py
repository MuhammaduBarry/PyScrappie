import pprint

from bs4 import BeautifulSoup

from src.scrape import html_page_one_parser, html_page_two_parser, create_custom_hn, sort_stories_by_vote

def main() -> None:
    soup: BeautifulSoup = html_page_one_parser()
    links: list = soup.select(".titleline > a")
    subtext: list = soup.select(".subtext")

    soup_two: BeautifulSoup = html_page_two_parser()
    links_two: list = soup_two.select(".titleline > a")
    subtext_two: list = soup_two.select(".subtext")

    both_pages: list = create_custom_hn(links, subtext) + create_custom_hn(links_two, subtext_two)
    both_pages: list = sort_stories_by_vote(both_pages)
    pprint.pprint(both_pages)


if __name__ == '__main__':
    main()