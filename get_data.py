import csv, os.path, logging, requests, argparse, sys
from collections import namedtuple
from refactor_sea_data import DisplaySeaTemps


class SeaTemps:
    url = 'https://www.metoffice.gov.uk/hadobs/hadsst3/data/HadSST.3.1.1.0/diagnostics/HadSST.3.1.1.0_annual_nh_ts.txt'
    annual_nh_sea_temps = requests.get(url)
    saved_nh_sst = 'nh_sst.txt'

    def __init__(self):
        self._refactor_data_to_csv()

    def __iter__(self):
        return iter(self.sea_values)

    def _refactor_data_to_csv(self):
        # B_S_C is average Bias Sampling and Coverage Error per year
        if os.path.exists('nh_sst.txt'):
            Temperatures = namedtuple('Temperatures',
                                      'Year Avg_Temp Lower_Bias Upper_Bias Lower_Sampling Upper_Sampling Lower_Coverage'
                                      ' Upper_Coverage Lower_Bias_Sampling Upper_Bias_Sampling Lower_B_S_C Upper_B_S_C')
            with open(self.saved_nh_sst, 'r') as sst_file:
                self.sea_values = []
                # We don't want to look at data beyond 2018
                reader = csv.reader(sst_file.readlines()[:-3], delimiter=' ', skipinitialspace=True)
                for line in reader:
                    data = Temperatures(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8],
                                        line[9], line[10], line[11])
                    year = data[0]
                    avg_temp = data[1]
                    lower_confidence = data[10]
                    upper_confidence = data[11]

                    self.sea_values.append(DisplaySeaTemps(year, avg_temp, lower_confidence, upper_confidence))
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
            self._refactor_data_to_csv()

        else:
            logging.debug(self.annual_nh_sea_temps.status_code)
