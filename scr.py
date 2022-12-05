import requests
import bs4

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'модель', 'деятельность']
HEADERS = {'Accept': '*/*', 'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
           'Accept-Language': 'en-US;q=0.5,en;q=0.3', 'Cache-Control': 'max-age=0', 'Pragma': 'no-cache'}

base_url = 'https://habr.com'
url = base_url + '/ru/all/'


def get_bsoup(url):
    response = requests.get(url, headers=HEADERS)
    text = response.text
    soup = bs4.BeautifulSoup(text, features="html.parser")
    return soup


def get_info():
    soup = get_bsoup(url)
    articles = soup.find_all("article")
    for article in articles:
        hubs = article.find_all(class_="tm-article-body tm-article-snippet__lead")
        hubs = [hub.text.strip() for hub in hubs]
        for hub in hubs:
            hub = hub.split()
            for el in hub:
                el = el.lower()
                if el in KEYWORDS:
                    date = article.find(class_="tm-article-snippet__datetime-published").find("time").text
                    title = article.find("h2").find('span').text
                    href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
                    link = base_url + href
                    return f"{date} - {title} - {link}"


print(get_info())

