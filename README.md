# sqlalchemy-challenge

![Surf_UP](https://github.com/llhabers/sqlalchemy-challenge/blob/main/surfs_up.png)

## Situation

I decided that I wanted to take a long holiday vacation in Honolulu, Hawaii. To maximize my time with this amazing opportunity, I decided to some climate analysis on the area. 

## Task

I decied to use SQLAlchemy and Flask app to conduct an analysis and well as creating a web page to review my results.

### Task 1: Climate Analysis and Exploration
<br>
#### Precipitation Analysis
Start by finding the most recent date in the data set.
<br>
Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. Note you do not pass in the date as a variable to your query.
<br>
Select only the date and prcp values.
<br>
Load the query results into a Pandas DataFrame and set the index to the date column.
<br>
Sort the DataFrame values by date.
<br>
Plot the results using the DataFrame plot method.
<br>

#### Station Analysis
<br>
Design a query to calculate the total number of stations in the dataset.
<br>
Design a query to find the most active stations (i.e. which stations have the most rows?).
List the stations and observation counts in descending order.
Which station id has the highest number of observations?
Using the most active station id, calculate the lowest, highest, and average temperature.
Hint: You will need to use a function such as func.min, func.max, func.avg, and func.count in your queries.
<br>
Design a query to retrieve the last 12 months of temperature observation data (TOBS).
Filter by the station with the highest number of observations.
Query the last 12 months of temperature observation data for this station.
Plot the results as a histogram with bins=12.

### Task 2: Climate App
<br>
#### Flask to create app
Use Flask to create your routes.
<br>
Routes
Home page - '/'
<br>
Precipitation - '/api/v1.0/precipitation'
<br>
Stations - '/api/v1.0/stations'
<br>
Temperatures - '/api/v1.0/tobs'
<br>
Start - '/api/v1.0/start'
<br>
Start & End - '/api/v1.0/start/end'

Convert the query results to a dictionary using date as the key and prcp as the value.
Return the JSON representation of your dictionary.
/api/v1.0/stations
Return a JSON list of stations from the dataset.
/api/v1.0/tobs
Query the dates and temperature observations of the most active station for the last year of data.
Return a JSON list of temperature observations (TOBS) for the previous year.
<!-- /api/v1.0/<start> and /api/v1.0/<start>/<end> -->
Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

## Action

## Results
![Precipitation](https://github.com/llhabers/sqlalchemy-challenge/blob/main/12_Months_Precipitation_Data.png)
![Histogram_Temperature](https://github.com/llhabers/sqlalchemy-challenge/blob/main/12_Months_of_Temperature_for_USC00519281.png)

I was able to use python, SQLAlchemy to do some basic climate analysis and data exploration of my climate database. With the help of ORM queries, Pandas and Matplotlib, I was able to use the database to find out which dates shows the most precipitation. Being able to view this data would let me know the best time period I should travel to Honolulu. I was also able to see the avaerage temperature in Honolulu as well as seeing the frequency of days with the average temperature.  
<br>