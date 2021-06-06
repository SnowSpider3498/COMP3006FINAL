# Final Project: Hurricane Frequency and Intensity and the correlation with Ocean Tempuratures

## Group Members
Kristoffer Sorensen & Courtnay McClure

## Research Question
<br /> <br />

## Datasets utilized
Hurricane data scraped from [StormFax](https://www.stormfax.com/huryear.htm)

Sea Temperatures pulled from [Met Office Hadley Centre](https://www.metoffice.gov.uk/hadobs/hadsst3/data/HadSST.3.1.1.0/diagnostics/HadSST.3.1.1.0_annual_nh_ts.txt)
<br /> <br />

## Analysis Conclusion

<br /> <br />

## Usage
```bash
python3 ----.py [-h] [-o <outfile>] [-p] [-s <sort>] <command>
```
### Dependencies
package dependencies listed in requirements.txt

### [command]
**print**: Displays all data

**by_decade**: Displays per decade data
  
**Storm**: Plots the total amount of Tropical Storms
  
**Severe**: Plots the total amount of severe hurricanes (Category 3 to Category 5)
  
**merge_data**: Merges SST Anomaly Data with Tropical Storm data and plots both on the same graph
  
### [optional arguments]
-**anomaly**: simply will show anomaly sst data, can be saved in a csv by providing an outfile
  
-**confidence**: like the anomaly but shows the upper and lower confidence bounds, can be saved in a csv by providing an outfile
  
-**merge**: ONLY Plots merged data between sst Anomalies and Confidence Intervals

-**p**: plots figures associated with command

-**csv** *folder name*: saves csvs associated with command to data/folder name of user input
  
-**tropical**: Displays the total tropical storms for a specific year
  
