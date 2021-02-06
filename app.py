import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    print('Welcome to my homepage. Please choose with route to would like to see.')
    return (
        f"/api/v1.0/precipitations<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/<start><br>"
        f"/api/v1.0/<start>/<end><br>"
    )
#################################################
# /api/v1.0/precipitation

# Convert the query results to a dictionary using date as the key and prcp as the value.

@app.route("/api/v1.0/precipitations")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

# Convert the query results to a dictionary using date as the key and prcp as the value.
    most_recent = session.query(Measurement.date, Measurement.prcp).order_by(
        Measurement.date.desc()).all()

    session.close()

    # Create a dictionary for dates
    prcp_dates = []
    for date, prcp in most_recent:
        print(date,prcp)
        date_dict = {}
        date_dict[date] = prcp
        prcp_dates.append(date_dict)

    return jsonify(prcp_dates)

#################################################

# /api/v1.0/stations
# Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all stations
    results = engine.execute('SELECT station.station, station.name FROM station')

    session.close()

    stations_list = []
    for station, name in results:
        print(station, name)
        station_dict = {}
        station_dict[station] = name
        stations_list.append(station_dict)

    return jsonify(stations_list)

#################################################

# /api/v1.0/tobs

@app.route("/api/v1.0/tobs")
def temperature():
    # Create our session (link) from Python to the DB
    session = Session(engine)

# Query the dates and temperature observations of the most active station for the last year of data.
# Return a JSON list of temperature observations (TOBS) for the previous year.
    
    usc_00519281_recent_date = session.query(Measurement.date).filter(
    Measurement.station == 'USC00519281').order_by(
    Measurement.date.desc()).first()

    usc_00519281_last_12 = (dt.datetime.strptime(usc_00519281_recent_date[0], '%Y-%m-%d') - dt.timedelta(days=365)).date()
    
    usc_00519281_last_12_temp = session.query(Measurement.date, Measurement.tobs).filter(
    Measurement.date > usc_00519281_last_12).filter(
    Measurement.station == 'USC00519281').order_by(
    Measurement.station.desc())
    
    session.close()

    usc_00519281_temp = []
    for dates, tobs in usc_00519281_last_12_temp:
        print(dates, tobs)
        usc_dates_dict = {}
        usc_dates_dict[dates] = tobs
        usc_00519281_temp.append(usc_dates_dict)
    
    return jsonify(usc_00519281_temp)

#################################################

# /api/v1.0/<start>
# Return a JSON list of the minimum temperature, the average temperature,
# date and the max temperature for a given start or start-end range.

@app.route("/api/v1.0/<start>")
def start(start):
    # create session link
    session = Session(engine)

    # take any date and convert to yyyy-mm-dd format for the query
    start_dt = dt.datetime.strptime(start, '%Y-%m-%d')

    # query data for the start date value
    outcomes = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_dt)

    session.close()

    # Create a list to hold outcomes
    temp_data = []
    for outcome in outcomes:
        outcome_dict = {}
        outcome_dict["StartDate"] = start_dt
        outcome_dict["TMIN"] = outcome[0]
        outcome_dict["TAVG"] = outcome[1]
        outcome_dict["TMAX"] = outcome[2]
        temp_data.append(outcome)

    # jsonify the result
    return jsonify(temp_data)

#################################################

# /api/v1.0/<start>/<end>
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

@app.route("/api/v1.0/<start>/<end")
def start_end(start, end):
    # create session link
    session = Session(engine)

    # take start and end dates and convert to yyyy-mm-dd format for the query
    start_dt = dt.datetime.strptime(start, '%Y-%m-%d')
    end_dt = dt.datetime.strptime(end, "%Y-%m-%d")

    # query data for the start date value
    analysis = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_dt).filter(Measurement.date <= end_dt)

    session.close()

    # Create a list to hold analysis
    temp_data_se = []
    for info in analysis:
        info_dict = {}
        info_dict["StartDate"] = start_dt
        info_dict["EndDate"] = end_dt
        info_dict["TMIN"] = info[0]
        info_dict["TAVG"] = info[1]
        info_dict["TMAX"] = info[2]
        temp_data_se.append(info_dict)

    # jsonify the result
    return jsonify(temp_data_se)

if __name__ == '__main__':
    app.run(debug=True)