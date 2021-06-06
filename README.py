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

**Storm**: explores salary per points
  
**Storm**: explores salary per points

### [optional arguments]
-**anomaly**: simply will show anomaly sst data, can be saved in a csv by providing an outfile
  
-**confidence**: like the anomaly but shows the upper and lower confidence bounds, can be saved in a csv by providing an outfile

-**p**: plots figures associated with command

-**csv** *folder name*: saves csvs associated with command to data/folder name of user input

# -**start_year** *year*: utilizes this year as beginning year to scrape webdata

# -**end_year** *year*: utilized this year as end year to scrape webdata

# -**flask_app**: runs local flask application to display plots 

