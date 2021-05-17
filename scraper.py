import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51"}


def finder(search):

    url = "https://www.amazon.in/s?k="
    # search = '+'.join(input("!!!Enter Product").split())
    url += '+'.join(search.split())
    print("... SEARCHING ...", url)

    req = requests.get(url, headers=header)
    if req.status_code > 500:
        print(
            f"{Fore.LIGHTRED_EX}MFs blocked me :(... try another proxy{Style.RESET_ALL}")
        if "To discuss automated access to Amazon data please contact" in req.text:
            print(f"{Fore.RED}Data access prevented{Style.RESET_ALL}")
    else:
        print("... OG STATUS ...", req.status_code)

    src = req.content

    soup = BeautifulSoup(src, 'lxml')
    print(f"{Fore.GREEN}... returned embeds{Style.RESET_ALL}")
    return soup.findAll("a", {"class": "a-link-normal a-text-normal"})
    # css classes in <i> as a-star-xx-yy

# <span class="a-size-medium a-color-base a-text-normal">Dell Vostro 3405 14" (35.56cms) FHD AG Display Laptop
# (Ryzen-5 3500U / 8GB / 512 SSD / Vega 8 Graphics / Win 10 + Office H&amp;S/ Dune Color) D552122WIN9DE</span>
