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
    return (
        f"/api/v1.0/precipitations<br>"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )
# /api/v1.0/2020-08-23


# /api/v1.0/precipitation

# Convert the query results to a dictionary using date as the key and prcp as the value.

# Return the JSON representation of your dictionary.
# -----------------------------
# Measurement
# -----------------------------
# id INTEGER
# station TEXT
# date TEXT
# prcp FLOAT
# tobs FLOAT
# -----------------------------
# Station
# -----------------------------
# id INTEGER
# station TEXT
# name TEXT
# latitude FLOAT
# longitude FLOAT
# elevation FLOAT

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


# # /api/v1.0/stations

# # Return a JSON list of stations from the dataset.

# @app.route("/api/v1.0/stations")
# def names():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all passenger names"""
#     # Query all passengers
#     results = session.query(Passenger.name).all()

#     session.close()

#     # Convert list of tuples into normal list
#     all_names = list(np.ravel(results))

#     return jsonify(all_names)

# # /api/v1.0/tobs

# # Query the dates and temperature observations of the most active station for the last year of data.

# # Return a JSON list of temperature observations (TOBS) for the previous year.

# @app.route("/api/v1.0/tobs")
# def names():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all passenger names"""
#     # Query all passengers
#     results = session.query(Passenger.name).all()

#     session.close()

#     # Convert list of tuples into normal list
#     all_names = list(np.ravel(results))

#     return jsonify(all_names)

# # /api/v1.0/<start>

# # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
Date
Min_Temp
Ave_Temp
Max_Temp
# # When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.

# @app.route("/api/v1.0/<start>")
# def names():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all passenger names"""
#     # Query all passengers
#     results = session.query(Passenger.name).all()

#     session.close()

#     # Convert list of tuples into normal list
#     all_names = list(np.ravel(results))

#     return jsonify(all_names)

# # /api/v1.0/<start>/<end>
# # When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

# @app.route("/api/v1.0/<start>/<end")
# def names():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all passenger names"""
#     # Query all passengers
#     results = session.query(Passenger.name).all()

#     session.close()

#     # Convert list of tuples into normal list
#     all_names = list(np.ravel(results))

#     return jsonify(all_names)


# /api/v1.0/<start> and /api/v1.0/<start>/<end>

# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.




#  session.close()

if __name__ == '__main__':
    app.run(debug=True)