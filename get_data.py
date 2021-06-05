import csv, os.path, logging, requests
from collections import namedtuple
from refactor_sea_data import DisplaySeaTemps


class SeaTemps:
    annual_nh_sea_temps = requests.get('https://www.metoffice.gov.uk/hadobs/hadsst3/data/HadSST.3.1.1.0/diagnostics/HadSST.3.1.1.0_annual_nh_ts.txt')
    saved_nh_sst = 'nh_sst.txt'
    sea_values = []

    def __init__(self):
        self._refactor_data_to_csv()
        self.response = SeaTemps.annual_nh_sea_temps.status_code

    def __iter__(self):
        return iter(self.sea_values)

    # Acts similar to AutoMPG data collection but is much more simplified
    def _refactor_data_to_csv(self):
        # B_S_C is average Bias Sampling and Coverage Error per year
        if os.path.exists('nh_sst.txt'):
            Temperatures = namedtuple('Temperatures',
                                      'Year Avg_Temp Lower_Bias Upper_Bias Lower_Sampling Upper_Sampling Lower_Coverage'
                                      ' Upper_Coverage Lower_Bias_Sampling Upper_Bias_Sampling Lower_B_S_C Upper_B_S_C')
            with open(self.saved_nh_sst, 'r') as sst_file:
                # We don't want to look at data beyond 2018
                reader = csv.reader(sst_file.readlines()[:-3], delimiter=' ', skipinitialspace=True)
                for x in reader:
                    data = Temperatures(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11])
                    year = data.Year
                    avg_temp = data.Avg_Temp
                    lower_confidence = data.Lower_B_S_C
                    upper_confidence = data.Upper_B_S_C

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

# You could add the option to look at only the 1800's, 1900's or early 2000's
