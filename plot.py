import matplotlib.pyplot as plt
import pandas as pd


# Standard years/anomaly plot
def plot_standard_data(args):
    years = []
    anomalies = []
    for x in args:
        years.append(x.year)
        anomalies.append(x.avg_anomaly)
    plt.plot(years, anomalies)
    plt.title('Sea Temperature Anomaly per Year')
    plt.xlabel('Year')
    plt.ylabel('Anomalies (F)')
    plt.xticks(rotation=75)
    plt.tight_layout()
    plt.show()
    plt.savefig('sst_standard')


# Plotting pandas anomaly data by decade
def plot_decade_anomalies(args):
    args.plot()
    plt.title('Sea Temperature Anomaly per Decade')
    plt.xlabel('Decade')
    plt.ylabel('Anomalies (F)')
    plt.tight_layout()
    plt.show()
    plt.savefig('sst_decade')


# Plotting pandas confidence intervals
def plot_decade_confidence(args):
    args.plot()
    plt.title('Sea Temperature Confidence per Decade')
    plt.xlabel('Decade')
    plt.ylabel('Confidence Intervals (F)')
    plt.tight_layout()
    plt.show()
    plt.savefig('sst_up_low_confidence')


# Merging the two sets of data
def merge_decade(args):
    args.plot()
    plt.title('Sea Temperature Confidence and Anomalies per Decade')
    plt.xlabel('Decade')
    plt.ylabel('Anomalies (F)')
    plt.tight_layout()
    plt.show()
    plt.savefig('sst_merge')




