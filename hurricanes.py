# imports
import requests, time
from bs4 import BeautifulSoup as BS
import matplotlib.pyplot as plt

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
        return f"Storm('{self.year}','{self.storms}','{self.hurricanes}','{self.basin})"

    def __str__(self):
        return str(self.__repr__())

class StormData:

    def _get_data(self):
        URL = 'https://www.wunderground.com/hurricane/archive/EP'

        page = requests.get(URL)
        
        soup = BS(page.content, 'html.parser')

        table = soup.find('table', class_='mat-table cdk-table mat-sort')

        print(table)

        # years = table.find_all('td', class_='mat-cell cdk-cell cdk-column-year mat-column-year ng-star-inserted')

        # print(years)


# pretend main

def main():

    collectData = StormData()

    collectData._get_data()


if __name__ == '__main__':
    main()




print(f'completed in: {(time.monotonic() - start_time):.2f}s')
