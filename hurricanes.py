# imports
import requests, time, urlopen
from bs4 import BeautifulSoup as BS
import matplotlib.pyplot as plt
import pandas as pd

start_time = time.monotonic()

class Storm:

    def __init__(self, year, storms, hurricanes, deaths, damage, basin):
        self.year = int(year)
        self.storms = int(storms)
        self.hurricanes = int(hurricanes)
        self.deaths = int(deaths)
        self.damage = int(damage) # millions USD
        self.basin = str(basin)

    def __repr__(self):
        return f"Storm('{self.year}','{self.storms}','{self.hurricanes}','{self.deaths}','{self.damage}','{self.basin})"

    def __str__(self):
        return str(self.__repr__())

class StormData:

    def _get_data(self):

        #getting html
        URL = 'https://www.stormfax.com/huryear.htm'
        page = requests.get(URL).text
        soup = BS(page, 'html.parser')

        #define table
        table = soup.find('table')
        #define rows
        row = table.find_all('b')

        #define attributes
        headers = []
        years = []
        namedStorms = []
        hurricanes = []
        majorHurricanes = []

        # define headers
        for header in row[:4]:
            headers.append(header.text)

        for idx, data in enumerate(row[4:]):
            if idx < 171:
                # print(data)
                # define years
                year = data.text[:4]
                if len(year) == 4:
                    years.append(year)
                
                # for i in data:

        print(table.find())

            


# pretend main

def main():

    collectData = StormData()

    collectData._get_data()


if __name__ == '__main__':
    main()




print(f'completed in: {(time.monotonic() - start_time):.2f}s')
