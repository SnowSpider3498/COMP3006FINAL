import requests
import logging
import csv
import os
from collections import namedtuple, defaultdict


class SortSeaTemps:
    def __init__(self, year, avg_anomaly, lower_confidence, upper_confidence):
        self.year = int(year)
        self.avg_anomaly = float(avg_anomaly)
        self.lower_confidence = float(lower_confidence)
        self.upper_confidence = float(upper_confidence)

    def __str__(self):
        return f'{self.year} {self.avg_anomaly} {self.lower_confidence} {self.upper_confidence}'

    # Sorts by year/avg anomaly
    def __gt__(self, other):
        if type(self) == type(other):
            if self.avg_anomaly > other.avg_anomaly:
                return (self.year, self.avg_anomaly, self.lower_confidence, self.lower_confidence) \
                       > (other.year, other.avg_anomaly, other.lower_confidence, other.upper_confidence)
            else:
                return (self.year, self.avg_anomaly, self.lower_confidence, self.lower_confidence) \
                       < (other.year, other.avg_anomaly, other.lower_confidence, other.upper_confidence)
        else:
            return NotImplemented

    def __lt__(self, other):
        pass

    def __hash__(self):
        return hash((self.year, self.avg_anomaly, self.lower_confidence, self.upper_confidence))


class SeaTemps:
    url = 'https://www.metoffice.gov.uk/hadobs/hadsst3/data/HadSST.3.1.1.0/diagnostics/HadSST.3.1.1.0_annual_nh_ts.txt'
    annual_nh_sea_temps = requests.get(url)
    saved_nh_sst = 'nh_sst.txt'

    def __init__(self):
        self._get_data()
        self._refactor_data_to_csv()

    def _refactor_data_to_csv(self):
        # B_S_C is average Bias Sampling and Coverage Error per year
        if os.path.exists('nh_sst.txt'):
            Temperatures = namedtuple('Temperatures',
                                      'Year Avg_Temp Lower_Bias Upper_Bias Lower_Sampling Upper_Sampling Lower_Coverage'
                                      ' Upper_Coverage Lower_Bias_Sampling Upper_Bias_Sampling Lower_B_S_C Upper_B_S_C')
            with open(self.saved_nh_sst, 'r') as sst_file:
                sea_values = []
                reader = csv.reader(sst_file, delimiter=' ', skipinitialspace=True)
                for line in reader:
                    data = Temperatures(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8],
                                        line[9], line[10], line[11])
                    year = data[0]
                    avg_temp = data[1]
                    lower_conf = data[10]
                    upper_conf = data[11]
                    print(year, avg_temp, lower_conf, upper_conf)
        else:
            self._get_data()

    def _get_data(self):
        if self.annual_nh_sea_temps.status_code:
            logging.debug(self.annual_nh_sea_temps.status_code)
            with open(self.saved_nh_sst, 'w') as nh_sst:
                for line in self.annual_nh_sea_temps:
                    # Data is read in bytes, so here I decode that and convert it into strings
                    line = line.decode()
                    nh_sst.write(line)
        else:
            logging.debug(self.annual_nh_sea_temps.status_code)


def _create_commandline():
    pass


def main():
    pass


if '__main__' == __name__:
    SeaTemps()
