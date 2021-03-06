from email.mime import image
from urllib import request

from bs4 import BeautifulSoup
from django.conf import settings
from newspaper import Article
from os.path import join

# Importing required libraries
import urllib.request


def bbc_beatify_article_text(article: Article) -> Article:
    """
    Beatify the article text section of any bbc article
    """
    soup = BeautifulSoup(article.html, "html.parser")
    all_p = soup.find_all("p")
    p_texts = [p.text for p in all_p]

    article_fulltext = "\n".join(p_texts)
    article.text = article_fulltext

    return article


def download_image(url: str) -> str:
    image_extension = ["jpg", "png", "jpeg"]

    for ex in image_extension:
        image_name = url.split("/")[-1]
        if ex in image_name:
            e = image_name.split(ex)
            image_name = "".join([e[0], ex])

    static_img_url = join("article-img", image_name)
    image_url = join(settings.PROJECT_ROOT, "static", static_img_url)

    # Adding information about user agent
    opener = urllib.request.build_opener()
    opener.addheaders = [
        (
            "User-Agent",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36",
        )
    ]
    urllib.request.install_opener(opener)

    # create a new image file
    with open(image_url, "wb") as fp:
        pass

    # downlaod the url image
    request.urlretrieve(url, image_url)

    return static_img_url
