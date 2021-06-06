import matplotlib.pyplot as plt
from get_data import StormData
import mpl_toolkits.axisartist as AA
from mpl_toolkits.axes_grid1 import host_subplot

stormDat = StormData()

# Standard years/anomaly plot
def plot_standard_anomalies(args):
    years, anomalies = [], []
    for x in args:
        years.append(x.year)
        anomalies.append(x.avg_anomaly)
    plt.plot(years, anomalies, color='green')
    plt.title('Sea Temperature Anomaly per Year')
    plt.xlabel('Year')
    plt.ylabel('Anomalies (F)')
    plt.tight_layout()
    plt.show()
    plt.savefig('sst_standard_anomalies')


# Standard confidence
def plot_standard_confidence(args):
    years, lower, upper = [], [], []
    for x in args:
        years.append(x.year)
        lower.append(x.lower_confidence)
        upper.append(x.upper_confidence)
    plt.plot(years, upper, color='red')
    plt.plot(years, lower, color='blue')
    plt.title('Sea Temperature Confidence per Year')
    plt.xlabel('Year')
    plt.ylabel('Confidence (F)')
    plt.tight_layout()
    plt.show()
    plt.savefig('sst_standard_confidence')


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


def graphStorm(args):
    year, nameStorm, hurricane, majhurricane = [], [], [], []
    for x in args:
        year.append(x.year)
        nameStorm.append(x.storms)
        hurricane.append(x.hurricanes)

    plt.style.use('dark_background')
    plt.plot(year, nameStorm, color='deeppink')
    plt.title('Tropical Storms per Year', color='white')
    plt.xlabel('Year', color='white')
    plt.ylabel('Tropical Storms', color='white')
    plt.yticks(fontsize=7)
    plt.tight_layout()
    plt.show()
    plt.savefig('stormsperyear')


def graph_severe_hurricanes(args):
    year, hurricane, majhurricane = [], [], []
    for x in args:
        year.append(x.year)
        majhurricane.append(x.majors)
        hurricane.append(x.hurricanes)
    plt.style.use('dark_background')
    fig, axs = plt.subplots(2, 1)
    axs[0].plot(year, majhurricane, color='darkmagenta')
    axs[0].set_xlabel('Year', color='white')
    axs[0].set_ylabel('Major Hurricanes', color='white')
    axs[1].bar(year, hurricane, color='green')
    axs[1].set_xlabel('Year', color='white')
    axs[1].set_ylabel('Hurricanes', color='white')
    # fig.title('Hurricanes per Year', color='white')
    fig.tight_layout()
    fig.show()
    fig.savefig('hurricanes_majperyear')


def combine_anomaly_storms(args, args2):
    year, nameStorm = [], []
    for x in args:
        year.append(x.year)
        nameStorm.append(x.storms)
    years, anomalies = [], []
    for x in args2:
        years.append(x.year)
        anomalies.append(x.avg_anomaly)

    host = host_subplot(111, axes_class=AA.Axes)
    plt.subplots_adjust(right=0.75)

    par1 = host.twinx()

    offset = 0
    new_fixed_axis = par1.get_grid_helper().new_fixed_axis
    par1.axis["right"] = new_fixed_axis(loc="right", axes=par1, offset=(offset, 0))

    par1.axis["right"].toggle(all=True)

    host.set_xlim(1850, 2020)
    host.set_ylim(0, 30)

    host.set_xlabel("Years")
    host.set_ylabel("Tropical Storms")
    par1.set_ylabel("Anomalies (F)")

    p1, = host.plot(year, nameStorm, label="Tropical Storms")
    p2, = par1.plot(years, anomalies, label="Anomalies (F)")

    par1.set_ylim(-0.6, 0.8)

    host.legend()

    host.axis["left"].label.set_color(p1.get_color())
    par1.axis["right"].label.set_color(p2.get_color())

    plt.draw()
    plt.show()
    plt.savefig('Anomalies_TropicalStorms')


def combine_anomaly_majors(args, args2):
    year, majhurricane = [], []
    for x in args:
        year.append(x.year)
        majhurricane.append(x.majors)
    years, anomalies = [], []
    for x in args2:
        years.append(x.year)
        anomalies.append(x.avg_anomaly)

    host = host_subplot(111, axes_class=AA.Axes)
    plt.subplots_adjust(right=0.75)

    par1 = host.twinx()

    offset = 0
    new_fixed_axis = par1.get_grid_helper().new_fixed_axis
    par1.axis["right"] = new_fixed_axis(
        loc="right", axes=par1, offset=(offset, 0))

    par1.axis["right"].toggle(all=True)

    host.set_xlim(1850, 2020)
    host.set_ylim(-1, 9)

    host.set_xlabel("Years")
    host.set_ylabel("Major Hurricanes")
    par1.set_ylabel("Anomalies (F)")

    p1, = host.plot(year, majhurricane, label="Major Hurricanes")
    p2, = par1.plot(years, anomalies, label="Anomalies (F)")

    par1.set_ylim(-0.6, 0.8)

    host.legend()

    host.axis["left"].label.set_color(p1.get_color())
    par1.axis["right"].label.set_color(p2.get_color())

    plt.draw()
    plt.show()
    plt.savefig('Anomalies_MajorHurricanes')
