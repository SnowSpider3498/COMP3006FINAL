# imports
import requests, time, logging, csv
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
        self.headers = []
        self.dictData = {}
        self.csvStormDat = []

        # define algorithm for correct data pull
        singles = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21, 22, 23, 24, 25, 26, 28, 30, 31, 32, 33, 34, 37, 38, 39, 41, 43, 44, 45, 46, 49, 51, 53, 54, 56, 59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 70, 71, 72, 74, 76, 77, 78, 79, 84, 87, 88, 89, 90, 95, 96, 97, 101, 105, 106, 109, 111, 112, 114, 116, 117, 121, 122, 124, 126, 128, 131, 132, 135, 136, 140, 141, 142, 143, 146, 158, 163]
        doubSing = [18, 29, 40, 47, 48, 50, 52, 55, 57, 58, 73, 75, 80, 81, 83, 85, 86, 91, 92, 93, 94, 98, 100, 102, 103, 104, 107, 108, 110, 113, 115, 119, 120, 123, 125, 127, 129, 130, 133, 134, 137, 138, 139, 145, 148, 149, 150, 151, 152, 153, 155, 156, 157, 160, 162, 164, 165]
        doubDoub = [19, 27, 35, 36, 42, 65, 82, 99, 118, 144, 147, 154, 159, 161, 166]

        # define headers
        for header in head[:4]:
            self.headers.append(header.text)

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

                        self.dictData[year]=(nameStorm, hurricane, majhurricane)
                        self.csvStormDat.append((year, nameStorm, hurricane, majhurricane))
                    # double - single algorithm
                    elif idx in doubSing:
                        year = dat[:4]
                        nameStorm = dat[4:6]
                        hurricane = dat[6]
                        majhurricane = dat[7:]

                        self.dictData[year] = (nameStorm, hurricane, majhurricane)
                        self.csvStormDat.append((year, nameStorm, hurricane, majhurricane))
                    # double - double algorithm
                    elif idx in doubDoub:
                        year = dat[:4]
                        nameStorm = dat[4:6]
                        hurricane = dat[6:8]
                        majhurricane = dat[8:]

                        self.dictData[year] = (nameStorm, hurricane, majhurricane)
                        self.csvStormDat.append((year, nameStorm, hurricane, majhurricane))

        
    def stormDataSet(self):

        self.yrs = self.dictData.keys()
        self.named = []
        self.hurr = []
        self.maj = []

        for i in self.dictData.values():
            self.named.append(int(i[0]))
            self.hurr.append(int(i[1]))
            self.maj.append(int(i[2]))
            

    def graphStorm(self):            

        plt.style.use('dark_background')
        plt.plot(self.yrs, self.named, color='deeppink')
        plt.title('Named Storms per Year', color='white')
        plt.xlabel('Year', color='white')
        plt.ylabel('Named Storms', color='white')
        plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 158, 166], rotation = 75, fontsize = 7)
        plt.yticks(fontsize=7)
        plt.tight_layout()
        plt.show()
        plt.savefig('stormsperyear')

    def graphHurricanes(self):


        # plt.style.use('dark_background')
        fig, axs = plt.subplots(2, 1)
        axs[0].plot(self.yrs, self.maj, color='darkmagenta')
        axs[0].set_xlabel('Year', color='white')
        axs[0].set_xticks([0, 20, 40, 60, 80, 100, 120, 140, 152, 166])
        axs[0].set_ylabel('Major Hurricanes', color='white')

        axs[1].bar(self.yrs, self.hurr, color='green')
        axs[1].set_xlabel('Year', color='white')
        axs[1].set_xticks([0, 20, 40, 60, 80, 100, 120, 140, 152, 166])
        axs[1].set_ylabel('Hurricanes', color='white')

        # fig.title('Hurricanes per Year', color='white')
        fig.tight_layout()
        fig.show()
        fig.savefig('hurricanes_majperyear')

    def stormCSV(self):

        stormcsv = "storm-data.csv"

        with open(stormcsv, 'w') as output:
            writer = csv.writer(output)

            writer.writerow(self.headers)

            for row in self.csvStormDat:
                writer.writerow(row)


# pretend main

def main():

    collectData = StormData()

    collectData._get_data()

    collectData.stormDataSet()

    collectData.stormCSV()


if __name__ == '__main__':
    main()




print(f'completed in: {(time.monotonic() - start_time):.2f}s')
