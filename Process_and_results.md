# Process and results


## 1. Objective

Predict the end station of city bike trips base on start station, start time and weather conditions.  
__Assumption:__ commuters follow more predictable patterns than occasional users. I will focus on this type of user.

## 2. [Getting the data](https://github.com/alvercau/Project_McNulty/blob/master/notebooks/Getting_the_data.ipynb)

Data to be used is the following:
* Trip data from Bike Share NYC, available [here](https://s3.amazonaws.com/tripdata/index.html). Description of the fields available [here](https://www.citibikenyc.com/system-data).
* Hourly weather data, requested from NOOA. Description available [here](https://www.ncdc.noaa.gov/cdo-web/datasets#LCD)

The urls to the files with the __trip data__ were obtained using Selenium and saved in a txt file. From the remote server, all files were downloaded based on the txt file.


## 3. [Data cleaning and storing in the PSQL database](https://github.com/alvercau/Project_McNulty/blob/master/notebooks/Cleaning_data_databases.ipynb)

The __trip data__ was inserted into the databse before cleaning. The following operations were made:
* convert user type to dummy variable
* transform variables to correct datatype
* truncate the data column to hour, necessary for matching with the weather data.

_At an earlier stage of the project, I classified the data according to the [bearing](https://github.com/alvercau/Project_McNulty/blob/master/notebooks/Classification-bearing.ipynb) of the bike trips instead of the end stations. This problem is less complex (9 target variables, including return to start station) and allowed for preliminary exploration of the data and the Classification Models. An additional table containing geodata was made._

The __weather data__ was cleaned before insertion in the database. The data was pretty dirty (strings inside of integers etc.) and SQL is not the best tool to clean data.  
The data contained several columns with a lot of NaNs and empty columns corresponding to the daily weather data. These were dropped. Additonally, I converted the data to the correct data types.

## 4. Modelling

Due to technical limitations, the initial project was downsized:

* Use all data: over 37 million rows. Machine not powerfull enough.
* Use all data from 2016: over 10 million rows. Machine not powerfull enough.
* Making predictions for only one startstation (the one near Grand Central Station, which is the busiest one).
* Focus on [commuters](https://github.com/alvercau/Project_McNulty/blob/master/notebooks/End_station_dow.ipynb): select only registered users and exclude weekends. Only data from June 2016 (random choice of month, necessary because of aforementioned techincal limitations), and using data from frequently visited stations only (at least 100 visits in the month of June). Total of about 900 000 datapoints, 350 target variables. Technical problems remained: python kernel died (causing all veriables to be lost) when trying to do Grid Searches or making predictions for more complex models (Voting Classifiers). 
* Select only the [female](https://github.com/alvercau/Project_McNulty/blob/master/notebooks/End_station_dow_fem.ipynb) users from the subset above. Total of 58 000 datapoints, 92 target variables. 

The target variable was unbalanced, so I always did stratified resampling for training.

## 5. Results

For all comuters, the best model is Decision Tree, with about 8% accuracy. When trying to do predictions on a voting Classifier, the kernel consistently dies.

For females comuters, the best model is a combination of Decision Tree and Random forests (soft vote, weights 1 and 5 respectively, parameters of each model tuned with GridSearch), which has an accuracy of about 13%. 
The subset of the data for which relatively good predictions were made was selected for visualisation purposes, with the probabilities of a bike ending up in a given  end station from a given start station.


## 6. Visualisation

Interactive map with 3 radiobuttons:
* visualisation of the start stations that give the best predictions
* visualisations of the best predicted end stations
* visualisation of startstation and the 10 end stations where bikes are most likely to go, color of dot corresponding to likelihood.

## 7. Future considerations

Startstation was not one of the most predictive features, due to the reason that startstation was included as a combination of latitude and longitude, rather than as a categorical variable.  
More data (more powerfull machine is needed).  
Multi-output classification: not only predict the end station, but also the end time. I suspect that predicting the end time will be easier (using linear regression) than predicting the end station. The predicted end time can be used to restrict the ouptu of the end station calssifier, giving rise to more accurate results. 




