import pandas as pd


# Averaging temp anomalies and intervals per decade
def _average_per_decade(self):
    years = []
    temp_flux = []
    for x in self.sea_values:
        years.append(x.year)
        temp_flux.append(x.avg_anomaly)
    df = pd.DataFrame({'Anomaly Avg': temp_flux}, index=years)
    decade_anomaly = (df.groupby((df.index // 10) * 10).sum()) / 10

    return decade_anomaly
