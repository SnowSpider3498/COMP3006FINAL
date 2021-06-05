import matplotlib.pyplot as plt
import pandas as pd
from get_data import*


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

class StormPlots:

    stormDat = StormData()

    def graphStorm(self):

        plt.style.use('dark_background')
        plt.plot(stormDat.yrs, stormDat.named, color='deeppink')
        plt.title('Named Storms per Year', color='white')
        plt.xlabel('Year', color='white')
        plt.ylabel('Named Storms', color='white')
        plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110,
                   120, 130, 140, 150, 158, 166], rotation=75, fontsize=7)
        plt.yticks(fontsize=7)
        plt.tight_layout()
        plt.show()
        plt.savefig('stormsperyear')

    def graphHurricanes(self):

        # plt.style.use('dark_background')
        fig, axs = plt.subplots(2, 1)
        axs[0].plot(stormDat.yrs, stormDat.maj, color='darkmagenta')
        axs[0].set_xlabel('Year', color='white')
        axs[0].set_xticks([0, 20, 40, 60, 80, 100, 120, 140, 152, 166])
        axs[0].set_ylabel('Major Hurricanes', color='white')

        axs[1].bar(stormDat.yrs, stormDat.hurr, color='green')
        axs[1].set_xlabel('Year', color='white')
        axs[1].set_xticks([0, 20, 40, 60, 80, 100, 120, 140, 152, 166])
        axs[1].set_ylabel('Hurricanes', color='white')

        # fig.title('Hurricanes per Year', color='white')
        fig.tight_layout()
        fig.show()
        fig.savefig('hurricanes_majperyear')




