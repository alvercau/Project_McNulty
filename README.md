# Project_McNulty
K-nearest neighbours project.

## Scenario

The city of New York wants to optimize their bike sharing system. A common problem is that some bike stations are often full, which requires the users to find another bike station in the neighbourhood to park their bike. Riders might not be too happy with that, since it causes them to loose time. Another problem is that sometimes bike stations are empty, so riders have to go to a nearby bike station to get a bike, again, causing them to waste time. If we get a better idea of the flow of bikes, we can anticipate these types of problems and move bikes from stations that are close to overflooding to stations that are close to emptying. This requires some logistics (trucks, drivers, etc.), so it is better if we know enough time beforehand when porblems will arise in which stations. 

## Question
Where do shared bikes go?

## The data

* [City bike data](https://s3.amazonaws.com/tripdata/index.html)
  * Start station: both ID and name. Name will be used to give understandable results. Analysis will be carried out based on ID only.
  * Start hour, converted to timestamp.
  * Date. Extract weekday vs. weekend from the date.
  * End station: both ID and name
  * User type (registered user vs. costumer)
  * Birth year of user (only available for registered users)
  * gender of user (only available for registered users)
  
* [NOAA on-demand hourly weather data](https://www7.ncdc.noaa.gov/CDO/cdopoemain.cmd?datasetabbv=DS3505&countryabbv=&georegionabbv=NAMER&resolution=40)
  * temperature
  * perceived temperature
  * humidity
  * windspeed
  * Timestamp (it would be good to have ate least hourly data to align with the start hour)

* Holiday data. 
