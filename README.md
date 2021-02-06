# sqlalchemy-challenge

![Surf_UP](https://github.com/llhabers/sqlalchemy-challenge/blob/main/surfs_up.png)

## Situation

I decided that I wanted to take a long holiday vacation in Honolulu, Hawaii. To maximize my time with this amazing opportunity, I decided to some climate analysis on the area. 

## Task

I decied to use SQLAlchemy and Flask app to conduct an analysis and well as creating a web page to review my results.

### Task 1: Climate Analysis and Exploration<br>
#### Precipitation Analysis<br>
Start by finding the most recent date in the data set.<br>
Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. Note you do not pass in the date as a variable to your query.<br>
Select only the date and prcp values.<br>
Load the query results into a Pandas DataFrame and set the index to the date column.<br>
Sort the DataFrame values by date.<br>
Plot the results using the DataFrame plot method.<br>

#### Station Analysis<br>
Design a query to calculate the total number of stations in the dataset.<br>
Design a query to find the most active stations (i.e. which stations have the most rows?).<br>
List the stations and observation counts in descending order.<br>
Which station id has the highest number of observations?<br>
Using the most active station id, calculate the lowest, highest, and average temperature.<br>
Hint: You will need to use a function such as func.min, func.max, func.avg, and func.count in your queries.<br>
Design a query to retrieve the last 12 months of temperature observation data (TOBS).<br>
Filter by the station with the highest number of observations.<br>
Query the last 12 months of temperature observation data for this station.<br>
Plot the results as a histogram with bins=12.<br>

### Task 2: Climate App<br>
#### Flask to create app<br>
Use Flask to create your routes.<br>
Routes
Home page - '/'<br>
Precipitation - '/api/v1.0/precipitation'<br>
Stations - '/api/v1.0/stations'<br>
Temperatures - '/api/v1.0/tobs'<br>
Start - '/api/v1.0/start'<br>
Start & End - '/api/v1.0/start/end'<br>

Convert the query results to a dictionary using date as the key and prcp as the value.<br>
Return the JSON representation of your dictionary.<br>
Return a JSON list of stations from the dataset.<br>
Query the dates and temperature observations of the most active station for the last year of data.<br>
Return a JSON list of temperature observations (TOBS) for the previous year.<br>
Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.<br>
When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.<br>
When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.<br>

## Action<br>
#### Climate Analysis and Exploration<br>
I was able to use SQL and python syntax to conduct my analysis. Some of the syntax are;<br>
SELECT<br>
FROM<br>
WHERE<br>
GROUP_BY<br>
ORDER_BY<br>
FILTER<br>
Statiscal function<br>
Min<br>
Max<br>
Ave<br>
Count<br>
#### Climate App<br>
In order for me to create an app for my data anaylsis, I had to create dictionaries for the data I retreived from Pandas. Once I was able to create dictionaries, I used for loops to pull all the information needed to create each app.


## Results<br>
![Precipitation](https://github.com/llhabers/sqlalchemy-challenge/blob/main/12_Months_Precipitation_Data.png)
![Histogram_Temperature](https://github.com/llhabers/sqlalchemy-challenge/blob/main/12_Months_of_Temperature_for_USC00519281.png)

I was able to use python, SQLAlchemy to do some basic climate analysis and data exploration of my climate database. With the help of ORM queries, Pandas and Matplotlib, I was able to use the database to find out which dates shows the most precipitation. Being able to view this data would let me know the best time period I should travel to Honolulu. I was also able to see the avaerage temperature in Honolulu as well as seeing the frequency of days with the average temperature.  
<br>