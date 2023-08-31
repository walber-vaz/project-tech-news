# Requisito 1
import time

import requests
from parsel import Selector


def fetch(url: str) -> str or None:
    """
    Fetches the content of a given URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str or None: The content of the URL if the request is successful,
        None otherwise.
    """
    try:
        response = requests.get(
            url, timeout=3, headers={"User-Agent": "Fake user-agent"}
        )
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None  # type: ignore
    except requests.exceptions.Timeout:
        return None  # type: ignore


# Requisito 2
def scrape_updates(html_content: str) -> list:
    """
    Scrape the updates from the given HTML content.

    Parameters:
        html_content (str): The HTML content to scrape.

    Returns:
        list: A list of links scraped from the HTML content.
    """
    selector = Selector(html_content)
    links = selector.css(".entry-title a::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content: str) -> str:
    """
    Extracts the next page link from the HTML content.

    Args:
        html_content (str): The HTML content of the page.

    Returns:
        str: The next page link.

    Raises:
        None.

    Examples:
        >>> html_content = "
            <html><body><a class='next' href='/page2'>Next</a></body></html>
        "
        >>> scrape_next_page_link(html_content)
        '/page2'
    """
    selector = Selector(html_content)
    next_page = selector.css(".nav-links a.next::attr(href)").get()
    return next_page  # type: ignore


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
