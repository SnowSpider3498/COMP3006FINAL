# Final Project: Hurricane Frequency and Intensity and the correlation with Ocean Tempuratures

## Group Members
Kristoffer Sorensen & Courtnay McClure

## Research Question
Our question was focused on if sea temperature played a role in hurricane frequency and intensity.

## Datasets utilized
Hurricane data scraped from [StormFax](https://www.stormfax.com/huryear.htm)

Sea Temperatures pulled from [Met Office Hadley Centre](https://www.metoffice.gov.uk/hadobs/hadsst3/data/HadSST.3.1.1.0/diagnostics/HadSST.3.1.1.0_annual_nh_ts.txt)

## Analysis Conclusion
Although this is a very new topic, a clear correlation can be made between sea temperature anomalies and the amount of tropical storms and major hurricanes occuring in the Northern hemisphere. As data became more accurate over time, the margin of error has decreased and shown a new light on what role these two variables play.

## Usage
```bash
python3 main.py [-h] [-o <outfile>] [-p] [-s <sort>] <command>
```
### Dependencies
package dependencies listed in requirements.txt

### [command]
**print**: Displays all data

**by_decade**: Displays per decade data
  
**merge_storms**: Plots the total amount of Tropical Storms along annual anomalies
  
**merge_majors**: Plots the total amount of severe hurricanes (Category 3 to Category 5) along annual anomalies
  
### [optional arguments]
-**anomaly**: simply will show anomaly sst data, can be saved in a csv by providing an outfile
  
-**confidence**: like the anomaly but shows the upper and lower confidence bounds, can be saved in a csv by providing an outfile
  
-**merge**: ONLY Plots merged data between sst Anomalies and Confidence Intervals

-**tropical**: displays tropical storm data that can be overlayed with annual ocean temperature anomalies using the 'merge_storms' command

-**o** *folder name*: saves csvs associated with command to data/folder name of user input (encorperates plot command)
  
 -**s**: Sorts by two main options ('anomaly', 'confidence') and two command specifc options ('merge', 'tropical' - both print command only)
  
 -**p**: Plots data for plotting capable sorts
 
 ### Data Set Explanation ###
 
 For sea temperatures, we used a Hadley Climate research website that focused on specifc sea anomalies and the confidence intervals around such from 1850 to 2021, and used data specifically focused in the Northern Hemisphere. For Hurricane data, we pulled from Storm Fax, which held information on hurricane occurance, intensity and frequency from 1851 to 2017, also in the Northern Hemisphere.

### Code Instructions ###

For standard sea temperature results, displayed in the order: (year, yearly anomaly, lower confidence bound, upper confidence bound), simply call print.
  
Adding the following 'sort' features including 'anomaly', 'confidence', or 'tropical', will produce a specific output focused on the sorting description. 

(sorting by tropical will show ANNUAL HURRICANE DATA ONLY)

To save a file to csv, apply the '-o' followed by a file name of user choice.
This works for all commands/sort except for the strict command(s) of 'merge_majors' and 'merge_storms' (These are plot only).

When saving a file to csv using '-o', a graph is created for all commands except for the initial call of:
        python3 main.py by_decade ---- This produces ONLY a standard out or requested csv but no plot (for data specific reasons)
    
To see hurricane data overlayed with sea temperature anomaly data, call either function of:
        python3 main.py merge_storms ---- Looks at all tropical storms (NO CSV CAN BE SAVED) (GRAPH ONLY)
        python3 main.py merge_majors ---- Looks at ONLY major storms (NO CSV CAN BE SAVED) (GRAPH ONLY)
      
CSV files are only allowed on specific files due to display orientation constraints
        
