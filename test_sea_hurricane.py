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


# Tests if the values are refactored properly
class TestRefactor_Data(unittest.TestCase):
    def test_type_conversion(self):
        test1 = DisplaySeaTemps(1945, 0.47, 0.23, 0.65)
        self.assertEqual(1945, test1.year)
        self.assertEqual(0.47, test1.avg_anomaly)
        self.assertEqual(0.23, test1.lower_confidence)
        self.assertEqual(0.65, test1.upper_confidence)

class TestStormData(unittest.TestCase):
    def test_iterable(self):
        iter(get_data.StormData())

    def test_get_data(self):
        self.assertTrue(StormData().response == 200)
    
    def test_stormCSV(self):
        get_data.StormData().stormCSV()
        self.assertTrue(os.path.exists('storm-data.csv'))

class TestPlot(unittest.TestCase):
    def test_plot_standard_anomalies(self):
        plot_standard_anomalies(SeaTemps().sea_values)
        self.assertTrue(os.path.exists('sst_standard_anomalies.png'))

    def test_plot_standard_confidence(self):
        plot_standard_confidence(SeaTemps().sea_values)
        self.assertTrue(os.path.exists('sst_standard_confidence.png'))

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
