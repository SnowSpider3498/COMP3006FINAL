import argparse, sys
import pandas as pd
import matplotlib.pyplot as plt
from get_data import SeaTemps


def main():
    nh_sea_data = SeaTemps()
    data_parser = argparse.ArgumentParser(description='Compiling Hurricane Initiation with Sea Temperatures')
    data_parser.add_argument('command', metavar='<command>', choices=['print'], type=str,
                             help='command to execute')
    data_parser.add_argument('-o', '--ofile', metavar='<outfile>', dest='ofile', action='store')
    data_parser.add_argument('-p', '--plot', action='store_true', dest='plot')
    args = data_parser.parse_args()
