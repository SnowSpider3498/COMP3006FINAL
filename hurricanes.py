# imports
import requests, time
from bs4 import BeautifulSoup as BS
import matplotlib.pyplot as plt
import pandas as pd

start_time = time.monotonic()

class Storm:

    def __init__(self, year, storms, hurricanes, majors):
        self.year = int(year)
        self.storms = int(storms)
        self.hurricanes = int(hurricanes)
        self.majors = int(majors)
        # self.basin = str(basin)

    def __repr__(self):
        return f"Storm('{self.year}','{self.storms}','{self.hurricanes}','{self.majors})"

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
        #define headers
        head = table.find_all('b')
        # define rows
        fullRow = table.find_all('tr')

        #define attributes
        headers = []
        self.data = []
        dictData = {} #should i have it as a dictionary? or a list? then i can utilize the class data similar to autompg.
        # define algorithm for correct data pull
        singles = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21, 22, 23, 24, 25, 26, 28, 30, 31, 32, 33, 34, 37, 38, 39, 41, 43, 44, 45, 46, 49, 51, 53, 54, 56, 59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 70, 71, 72, 74, 76, 77, 78, 79, 84, 87, 88, 89, 90, 95, 96, 97, 101, 105, 106, 109, 111, 112, 114, 116, 117, 121, 122, 124, 126, 128, 131, 132, 135, 136, 140, 141, 142, 143, 146, 158, 163]
        doubSing = [18, 29, 40, 47, 48, 50, 52, 55, 57, 58, 73, 75, 80, 81, 83, 85, 86, 91, 92, 93, 94, 98, 100, 102, 103, 104, 107, 108, 110, 113, 115, 119, 120, 123, 125, 127, 129, 130, 133, 134, 137, 138, 139, 145, 148, 149, 150, 151, 152, 153, 155, 156, 157, 160, 162, 164, 165]
        doubDoub = [19, 27, 35, 36, 42, 65, 82, 99, 118, 144, 147, 154, 159, 161, 166]

        # define headers
        for header in head[:4]:
            headers.append(header.text)

        # define years, named storms, hurricanes, and major hurricanes        
        for idx, data in enumerate(fullRow):
            if idx == 1:
                # turn rows into list
                text = data.text
                text = text.split()
                text.pop()
                text.pop()
                # iterate
                for idx, dat in enumerate(text):
                    # single algorithm
                    if idx in singles:
                        year = dat[:4]
                        nameStorm = dat[4]
                        hurricane = dat[5]
                        majhurricane = dat[6:]

                        # dictData[year]=(nameStorm, hurricane, majhurricane)
                        self.data.append(Storm(year, nameStorm, hurricane, majhurricane))
                    # double - single algorithm
                    elif idx in doubSing:
                        year = dat[:4]
                        nameStorm = dat[4:6]
                        hurricane = dat[6]
                        majhurricane = dat[7:]

                        # dictData[year] = (nameStorm, hurricane, majhurricane)
                        self.data.append(Storm(year, nameStorm, hurricane, majhurricane))
                    # double - double algorithm
                    elif idx in doubDoub:
                        year = dat[:4]
                        nameStorm = dat[4:6]
                        hurricane = dat[6:8]
                        majhurricane = dat[8:]

                        # dictData[year] = (nameStorm, hurricane, majhurricane)
                        self.data.append(Storm(year, nameStorm, hurricane, majhurricane))

        print(self.data)


    def graphStorm(self):

        pass
                
        # print(headers)
            


# pretend main

def main():

    collectData = StormData()

    collectData._get_data()


if __name__ == '__main__':
    main()




print(f'completed in: {(time.monotonic() - start_time):.2f}s')
