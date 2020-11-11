
"""
Get the citation from google scholar
using title and year of publication, and volume and pages of journal.
"""

from bs4 import BeautifulSoup
import requests
import re


def create_url(title: str, journal: str, volume: str, page: str, year: str) -> str:
    """
    Return the url.
    """
    url = f"http://scholar.google.com/scholar_lookup?hl=en&title={title}&journal={journal}&volume={volume}&pages={page}&publication_year={year}"
    url = remove_tag(url)
    return url.replace(" ", "%")


def remove_tag(url: str) -> str:
    """
    Return the url removed the html tags.
    """
    tag = re.compile('<.*?>')
    clean_url = re.sub(tag, '', url)
    return clean_url


def get_citation(url: str) -> str:
    """
    Return the citation number.
    """
    url = requests.get(url).text
    soup = BeautifulSoup(url, "html.parser")
    get_div = soup.find(u"div", attrs={u"class": u"gs_ri"})
    get_a_tag = get_div.find(u"div", attrs={u"class": u"gs_fl"}).findAll('a')
    citation = get_a_tag[2].get_text()
    if 'Cited' not in citation:
        citation = 'Cited by 0'

    return citation.replace("Cited by ", "")


if __name__ == '__main__':
    """
    You have to fill following values: title, journal_name, volume, page, year. 
    
    For example,
    title = "Precisely geometry controlled microsupercapacitors for ultrahigh areal capacitance, volumetric capacitance, and energy density"
    journal_name = "Chem. Mater"
    volume = "30"
    page = "3979-3990"
    year = "2018"
    """
    title = ""
    journal_name = ""
    volume = ""
    page = ""
    year = ""

    citation = get_citation(create_url(title, journal_name, volume, page, year))
    print(citation)

