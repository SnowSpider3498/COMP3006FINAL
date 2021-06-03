import matplotlib.pyplot as plt
import pandas as pd
from get_data import SeaTemps


def plot_standard_data(args):
    years = []
    anomalies = []
    for x in args:
        years.append(x.year)
        anomalies.append(x.avg_anomaly)
    plt.plot(years, anomalies)
    plt.title('Sea Temperature Anomaly per Year')
    plt.xlabel('Year')
    plt.ylabel('Anomaly (F)')
    plt.xticks(rotation=75)
    plt.tight_layout()
    plt.show()
    plt.savefig('sst_standard')


def plot_decade_anomalies():
    pass


