import requests
from time import sleep
from bs4 import BeautifulSoup as bs


def check(URL):
    page = requests.get(URL)

    soup = bs(page.content, "html.parser")

    results = soup.find(id="pnlInventory")

    stock = results.find_all("span", class_="inventoryCnt")
    check = ""
    for job_elem in stock:
        check = job_elem.text.strip()
    return check


def tof():
    if (
        check(
            "https://www.microcenter.com/product/626147/gigabyte-b460m-aorus-pro-intel-lga-1200-microatx-motherboard?storeid=085" #just a random link for an example
        )
        != "Sold Out"
    ):
        return "In stock."
    else:
        return "not in stock"
