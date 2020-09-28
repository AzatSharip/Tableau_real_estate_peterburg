# -*- coding: utf-8 -*-
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import random



def main():
    time.sleep(random.uniform(1,3))
    url = 'https://maps.vlasenko.net/list/russia/leningradskaya/'
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.content, features="html.parser")
    status = r.status_code
    print(status)


    names_lst = []
    lon_lst = []
    lat_lst = []
    count = 0
    blockquote = soup.find_all("blockquote")

    for b in blockquote:
        # print(b.find_all('b'))
        # print(b)
        for loc in b:
            try:
                count += 1
                # print(loc)

                name = loc.get_text()
                names_lst.append(name)

                link = 'https://maps.vlasenko.net' + loc.find('a')['href']
                lon, lat = get_coord(link)
                lon_lst.append(lon)
                lat_lst.append(lat)

                # print(count)
                print(f'{7311 - count} осталось')
                print(name, lon, lat)
            except:
                pass
    print(len(names_lst))
    print(len(lon_lst))
    print(len(lat_lst))

    df_main = pd.DataFrame({'name': names_lst, 'longitude': lon_lst, 'latitude': lat_lst})
    print(df_main)
    df_main.to_csv(r'D:\\Personal\\GitHub\\Data_science\\lenobl_coord.csv', index=False)


def get_coord(url):
    time.sleep(random.uniform(1,2))
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.content, features="html.parser")
    lon_lat = soup.find_all('div', itemprop='geo')

    for l_l in lon_lat:
        lon = float(l_l.find('input', id="lon")['value'])
        lat = float(l_l.find('input', id="lat")['value'])
        # print(lon, lat)
        return lon, lat




if __name__ == '__main__':
    df = pd.read_csv('D:\\Personal\\GitHub\\Data_science\\df_clean.csv')
    main()
    #get_coord('https://maps.vlasenko.net/ru/leningradskaya/boksitogorskij/abramova_gora/')