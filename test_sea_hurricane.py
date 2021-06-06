import unittest
import os
from refactor_data import *
import get_data
from data_manipulation import *
from main import *
from plot import *


class TestSeaTemps(unittest.TestCase):
    def test_iterable(self):
        iter(get_data.SeaTemps())

    def test_get_data(self):
        # make sure the website returns a status code
        self.assertTrue(get_data.SeaTemps().response == 200)

class TestStormData(unittest.TestCase):
    def test_iterable(self):
        iter(get_data.StormData())

    def test_get_data(self):
        self.assertTrue(get_data.StormData()._get_data().response == 200)
    
    def test_stormCSV(self):
        get_data.StormData().stormCSV()
        self.assertTrue(os.path.exists('storm-data.csv'))

class TestDataManipulation(unittest.TestCase):
    def test_average_per_decade(self):
        pass

    def test_avg_lower_upper_decade(self):
        pass

    def test_merge(self):
        pass
# to get an update
class TestRefactorData(unittest.TestCase):
    def test_display_sea_temps(self):
        pass

    def test_storm(self):
        pass

class TestPlot(unittest.TestCase):
    def test_plot_standard_anomalies(self):
        plot_standard_anomalies(SeaTemps().sea_values)
        self.assertTrue(os.path.exists('sst_standard_anomalies.png'))

    def test_plot_standard_confidence(self):
        plot_standard_confidence(SeaTemps().sea_values)
        self.assertTrue(os.path.exists('sst_standard_confidence.png'))

    def test_plot_decade_anomalies(self):
        pass
        # plot_decade_anomalies(data)
        # self.assertTrue(os.path.exists('sst_decade.png'))

    def test_plot_decade_confidence(self):
        pass
        # plot_decade_confidence(confidence)
        # self.assertTrue(os.path.exists('sst_up_low_confidence.png'))

    def test_merge_decade(self):
        pass
        # merge_decade(merged)
        # self.assertTrue(os.path.exists('sst_merge.png'))

    def test_graphStorm(self):
        graphStorm(StormData().hurricane_values)
        self.assertTrue(os.path.exists('stormsperyear.png'))

    def test_graph_severe_hurricanes(self):
        graph_severe_hurricanes(StormData().hurricane_values)
        self.assertTrue(os.path.exists('hurricanes_majperyear.png'))

    def test_combine_anomaly_storms(self):
        combine_anomaly_storms(StormData().hurricane_values, SeaTemps().sea_values)
        self.assertTrue(os.path.exists('Anomalies_TropicalStorms.png'))

    def test_combine_anomaly_majors(self):
        combine_anomaly_majors(StormData().hurricane_values, SeaTemps().sea_values)
        self.assertTrue(os.path.exists('Anomalies_MajorHurricanes.png'))


if __name__ == '__main__':
    unittest.main()
