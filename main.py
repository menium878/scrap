from asyncore import read
from importlib.resources import contents
from bs4 import BeautifulSoup
import requests
import time
def fine_curr():
    html_text=requests.get('https://coinranking.com').text

    soup = BeautifulSoup(html_text, 'lxml')

    currs = soup.find_all('tr',class_='table__row table__row--click table__row--full-width')
    for curr in currs:
        name_curr=curr.find('a',class_='profile__link').text.replace(' ','')
        price_curr=curr.find('div',class_='valuta valuta--light undefined').text.replace(' ','').replace('$','')
        ##print(f'''
        ##Name of the currency: {name_curr}
        ##Price: {price_curr}
        ##''')
        print(name_curr.strip(),price_curr.strip())
        print('')

if __name__ == '__main__':
    while True:
        fine_curr()
        time.sleep(10)



