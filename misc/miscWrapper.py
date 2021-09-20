import requests
from bs4 import BeautifulSoup


class BaseApi:
    def __init__(self, url, decode=True):
        self.url = url
        self.decode = decode

    def func(self):
        def inner():
            return requests.get (url=self.url).content.decode ('ascii') if self.decode else requests.get (url=self.url)

        return inner


def bb():
    url = "https://www.billboard.com/charts/hot-100"
    page = requests.get (url)
    soup = BeautifulSoup (page.content, 'html.parser')
    query = []
    td = soup.find_all (
        "span",
        class_="chart-element__information__song text--truncate color--primary"
    )[:10]
    ts = soup.find_all (
        "span",
        class_=
        "chart-element__information__artist text--truncate color--secondary"
    )[:10]
    for i in range (10):
        query.append (f"{i + 1}. {td[i].text} - {ts[i].text}")
    return "\n".join (query)


class MiscWrapper:
    def __init__(self):
        self.wrappers = {
            'joke': BaseApi ('https://v2.jokeapi.dev/joke/Any?format=txt').func (),
            'insult': BaseApi ("https://evilinsult.com/generate_insult.php?lang=en&type=text").func (),
            'bb': bb
        }

    def get(self, wrap):
        return self.wrappers[wrap] ()
