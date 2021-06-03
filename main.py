import argparse, sys
import csv
import matplotlib.pyplot as plt
from get_data import SeaTemps
from avg_per_decade import *
from plot_sst import *


def main():
    nh_sea_data = SeaTemps()
    data_parser = argparse.ArgumentParser(description='Compiling Hurricane Initiation with Sea Temperatures')
    data_parser.add_argument('command', metavar='<command>', choices=['print', 'by_decade'], type=str,
                             help='command to execute')
    data_parser.add_argument('-o', '--ofile', metavar='<outfile>', dest='ofile', action='store')
    data_parser.add_argument('-p', '--plot', action='store_true', dest='plot')
    data_parser.add_argument('-s', '--sort', metavar='<sort>', choices=['confidence', 'anomaly', 'merge'], dest='sort')
    args = data_parser.parse_args()

    if args.command == 'print':
        head_row = [['Year', 'Annual Anomaly', 'Lower Confidence Interval', 'Upper Confidence Interval']]
        for x in nh_sea_data:
            row = [x.year, x.avg_anomaly, x.lower_confidence, x.upper_confidence]
            head_row.append(row)
        if args.ofile is None:
            to_stdout = csv.writer(sys.stdout)
            to_stdout.writerows(head_row)
        else:
            with open(args.ofile, 'w', newline='') as optimised_sst:
                to_file = csv.writer(optimised_sst, quoting=csv.QUOTE_ALL)
                to_file.writerows(head_row)

        if args.plot is not None:
            plot_standard_data(nh_sea_data.sea_values)

    if args.command == 'by_decade':
        if args.sort is None:
            if args.ofile is None:
                data = average_per_decade(nh_sea_data.sea_values)
                confidence = avg_lower_upper_decade(nh_sea_data.sea_values)
                data.to_csv(sys.stdout, header=False)
                confidence.to_csv(sys.stdout, header=False)
            else:
                with open(args.ofile, 'w', newline='') as decade_information:
                    data = average_per_decade(nh_sea_data.sea_values)
                    confidence = avg_lower_upper_decade(nh_sea_data.sea_values)
                    data.to_csv(decade_information, header=False)
                    confidence.to_csv(sys.stdout, header=False)

        # Sorts by anomaly from avg_per_decade
        elif args.sort == 'anomaly':
            if args.ofile is None:
                print('Decade', '|', 'Average Anomaly')
                data = average_per_decade(nh_sea_data.sea_values)
                data.to_csv(sys.stdout, header=False)
            else:
                with open(args.ofile, 'w', newline='') as decade_information:
                    data = average_per_decade(nh_sea_data.sea_values)
                    data.to_csv(decade_information, header=False)

            if args.plot is not None:
                plot_decade_anomalies(data)


        # Sorts by confidence intervals from avg_per_decade
        elif args.sort == 'confidence':
            if args.ofile is None:
                print('Decade', '|', 'Lower Conf.', '|', 'Upper Conf.')
                confidence = avg_lower_upper_decade(nh_sea_data.sea_values)
                confidence.to_csv(sys.stdout, header=False)
            else:
                with open(args.ofile, 'w', newline='') as confidence_information:
                    confidence = avg_lower_upper_decade(nh_sea_data.sea_values)
                    confidence.to_csv(confidence_information, header=False)

            if args.plot is not None:
                plot_decade_confidence(confidence)

        elif args.sort == 'merge':
            if args.plot is not None:
                merged = merge(nh_sea_data.sea_values)
                merge_decade(merged)


if '__main__' == __name__:
    main()

# Issue of running command then displaying the graph

