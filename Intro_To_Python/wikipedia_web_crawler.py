# This script is designed to search Wikipedia from an article
# and determine if it can trace its way to the Philosophy
# article using the first link on each article page it visits
# This script was created while following a course on Udacity

# import standard libraries
import time
import urllib

# import third party libraries
from bs4 import BeautifulSoup
import requests

def continue_crawl(search_history, target_url, max_steps=25):
    """
    This function will determine whether it is possible
    to continue searching for the target_url. It will return
    false if the last item in search_history is target_url,
    if list is more than 25 urls and target_url not found,
    or if list has a cycle in it. It will return true otherwise.
    :param search_history: list of article urls that have already been reached (list of str)
    :param target_url: destination url attempting to reach (str)
    :param max_steps: number of article urls allowed before stopping search
    :return: true or false whether it can continue on
    """
    if search_history[-1] == target_url:
        print("Target found. We got to Philosophy")
        return False
    elif len(search_history) > max_steps:
        print("Too many steps taken. Go to jail, do not collect $200")
        return False
    elif search_history[-1] in search_history[0:-1]:
        print("Oops! Have we been here before?")
        return False
    elif search_history[-1] is None:
        print("Nothing to see here. No really, there is nothing to see here.")
        return False
    else:
        return True


def find_first_link(url):
    # get the HTML from the url using requests library
    response = requests.get(url)
    html = response.text
    # feed the HTML into Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # find first link in article using Beautiful soup
    article_link = ""
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return

    first_relative_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_relative_link


def web_crawl(article_chain, target_url):
    while continue_crawl(article_chain, target_url):
        print(article_chain[-1])
        # download the HTML for the last article in article_chain
        # find the first link in the last article's HTML
        first_link = find_first_link(article_chain[-1])
        # add the first link to the article_chain
        article_chain.append(first_link)
        # pause for a couple seconds so we don't flood Wikipedia w/ requests
        time.sleep(2)


start_url = ["https://en.wikipedia.org/wiki/Special:Random"]
tar_url = "https://en.wikipedia.org/wiki/Philosophy"

web_crawl(start_url, tar_url)
