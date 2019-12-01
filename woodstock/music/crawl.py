"""Web crawling and scraping
"""

import requests
from bs4 import BeautifulSoup

from woodstock.util import utility

BASE_URL = 'https://www.imdb.com/'


def get_soup(url: str) -> BeautifulSoup:
    """Returns BeautifulSoup object from the corresponding URL, passed as a string.
    Creates Response object from HTTP GET request, using requests.get(<url string>, allow_redirects=False),
    and then uses the text field of the Response object and the 'html.parser' to create the BeautifulSoup object.
    """

    # Create Response object from HTTP GET request; assume that no redirection is allowed
    response = requests.get(url, allow_redirects=False)
    # Get text from the Response object
    response_text = response.text
    # Create and return the corresponding BeautifulSoup object from the response text; use 'html.parser'
    soup = BeautifulSoup(response_text, 'html.parser')
    return soup


def get_specific_page(start_url: str, page=1):
    """Returns a specific page from a Website where long lists of items are split in multiple pages.
    """

    if '&page=1' in start_url:
        url_chunks = start_url.split('&page=1')
        return ''.join(url_chunks) + '&page=' + str(page)
    else:
        return start_url


def get_next_soup(start_url: str, page=1):
    """Returns the BeautifulSoup object corresponding to a specific page
    in case there are multiple pages that list objects of interest.
    Parameters:
    - start_url: the starting page/url of a multi-page list of objects
    - page: the page number of a specific page of a multi-page list of objects
    """

    return get_soup(get_specific_page(start_url, page))


def crawl(url: str, max_pages=1):
    """Web crawler that collects info about movies from IMDb,
    implemented as a Python generator that yields BeautifulSoup objects (get_next_soup()) from multi-page movie lists.
    Parameters: the url of the starting IMDb page and the max number of pages to crawl in case of multi-page lists.
    """

    page = 1
    while page <= max_pages:
        yield get_next_soup(url, page)
        page += 1


def get_m_info(start_url: str, max_pages=1):
    """
    Returns structured information about movies from a multi-page IMDb movie list.
    :param start_url: the url of the starting page of a multi-page IMDb movie list
    :param max_pages: the max number of pages to crawl
    :return: a list of tuples of info-items about the movies from a multi-page IMDb movie list
    Creates and uses the following data:
    - h3_list - a list of all 'h3' tags from multiple IMDb pages
                (each 'h3' tag contains: movie title, year of release, and (relative) link to the movie's IMDb page)
    - poster_list - a list of all relevant 'div' tags from multiple IMDb pages
                    (each such a 'div' tag contains the link to the poster of the corresponding movie)
    - info_list - a list of 3-tuples of information about each movie from h3_list
    - poster_link_list - a list of links to the posters of the movies from poster_list
    - complete_list - a list of 4-tuples of information about each movie from h3_list and poster_list
    """

    h3_list = []
    poster_list = []
    next_soup = crawl(start_url, max_pages)
    while True:
        try:
            # h3_list.extend(next(next_soup).find_all('h3'))
            s = next(next_soup)
            h3_list.extend(s.find_all('h3'))
            h3_list.pop(len(h3_list) - 1)
            poster_list.extend(s.find_all('div', {'class': "lister-item-image ribbonize"}))
        except StopIteration:
            break

    info_list = []
    for h3 in h3_list:
        title = h3.a.text
        link = BASE_URL + h3.a['href'].lstrip('/')
        year = h3.a.find_next_sibling().string.lstrip('(').rstrip(')')
        t = title, year, link
        info_list.append(t)

    poster_link_list = []
    for poster in poster_list:
        poster_link_list.append(poster.a.img['loadlate'])

    complete_list = []
    for t, poster_link in zip(info_list, poster_link_list):
        title, year, link = t
        extended_t = title, year, link, poster_link
        complete_list.append(extended_t)
    # return h3_list
    # return info_list
    return complete_list


if __name__ == "__main__":

    # # Just experimenting
    # start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key&' \
    #             'mode=detail&page=1&sort=moviemeter,asc'
    # response = requests.get(start_url, allow_redirects=False)  # create Response object from GET request
    # response_text = response.text  # get text from the Response object
    # # print(type(response))
    # # print(type(response_text))
    # # print(response_text)
    # print()
    #
    # soup = BeautifulSoup(response_text, 'html.parser')
    #
    # # print(type(soup))
    # # print(soup)
    # # soup_file = utility.get_data_dir() / 'soup.html'
    # # soup_file.write_text(str(soup), encoding='utf-8', errors='replace')
    #
    # # for h3 in soup.find_all('h3'):
    # #     print(h3)
    #
    # # movie_items = soup.find_all('div', {'class': "lister-list"})
    # # print(type(movie_items))
    # # print(len(movie_items))
    # # print(movie_items)
    #
    # # movie_items_soup = BeautifulSoup(str(movie_items[0]), 'html.parser')
    # # print(type(movie_items_soup))
    #
    # movie_items_h3 = soup.find_all('h3')
    # # print(movie_items_h3)
    # # print(len(movie_items_h3))
    # movie_items_h3.pop(50)
    # # print(len(movie_items_h3))
    # # print(movie_items_h3)
    #
    # for h3 in movie_items_h3:
    #     # print(h3)
    #     # print(type(h3))
    #
    #     # print(h3.text)
    #
    #     # print(h3.text.split('.\n')[1])
    #     print(h3.text.split('.\n')[1].split('\n(')[0])

    # Test get_soup(start_url)
    start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&' \
                'ref_=kw_ref_key&mode=detail&page=1&sort=moviemeter,asc'
    soup = get_soup(start_url)
    # print(soup)
    # print(type(soup))
    # print(soup.text)
    # print()

    # Demonstrate <soup>.find_all('<tag_name>') for 'div' (filter ResultSet with <{'class': "<class name>"}), 'h3',...
    # # movie_items = soup.find_all('div')
    # movie_items = soup.find_all('div', {'class': "lister-list"})
    # print(type(movie_items))
    # print(len(movie_items))
    # print(movie_items)
    # print()

    # Demonstrate <soup>.find_all('<tag_name>') for 'h3' - attribute h3.text
    movie_items_h3 = soup.find_all('h3')
    # for h3 in movie_items_h3:
    #     print(h3)
    movie_items_h3.pop(50)

    # # Demonstrate attribute h3.text
    # for h3 in movie_items_h3:
    #     print(h3)
    #     print(type(h3))
    #     print(h3.text)
    #     print(str(h3))
    #     print()

    # # Demonstrate attribute h3.find('<subtag>'), h3.find('<subtag>').text, h3.find('<subtag>').get('<attribute>')
    # for h3 in movie_items_h3:
    #     # print(h3.find('a'))
    #     print(h3.find('a').text)
    #     print(h3.find('a').get('href'))
    #     print()

    # # Demonstrate attribute h3.find('<subtag>'), filtered with <{'class': "<class name>"}
    # for h3 in movie_items_h3:
    #     print(h3.find('a').text)
    #     print(h3.find('span', {'class': "lister-item-year text-muted unbold"}).text)
    #     print()

    # # Demonstrate shorthand notation (e.g., h3.find('<tag>').text is equivalent to h3.<tag>.text),
    # # h3.<tag>.find_next_siblings() and h3.<tag>.string
    # for h3 in movie_items_h3:
    #     print(h3.a.text)
    #     print(h3.a.string)
    #     # print(h3.span)
    #     # print(h3.span.find_next_siblings()[1])
    #     print(h3.span.string)
    #     # print(h3.span.find_next_siblings()[1].string)
    #     print(h3.a.find_next_siblings()[0].string)
    #     print(h3.a.find_next_siblings()[0].text)
    #     print()

    # # Test get_specific_page()
    # # specific_page = get_specific_page(start_url)
    # specific_page = get_specific_page(start_url, 2)
    # print(specific_page)
    # print()

    # # Test get_next_soup()
    # # next_soup = get_next_soup(start_url)
    # next_soup = get_next_soup(start_url, 3)
    # # print(next_soup.text)
    # print(next_soup.find_all('h3'))
    # print()

    # # Test crawl()
    # # next_soup = crawl(start_url, 2)
    # # next_soup = crawl(start_url)
    # # print(next(next_soup).find_all('h3'))
    # # print(next(next_soup).find_all('h3'))
    # next_soup = crawl(start_url, 2)
    # while True:
    #     try:
    #         print(next(next_soup).find_all('h3'))
    #     except StopIteration:
    #         break
    # print()

    # Test get_m_info()
    # print(get_m_info(start_url))
    # print(get_m_info(start_url, 2))
    for m in get_m_info(start_url, 2):
        print(m)

