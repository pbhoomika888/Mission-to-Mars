# import necessary libraries
from flask import Flask, render_template
import pymongo
import scrape_mars
from flask_pymongo import pymongo
import os

# create instance of Flask app
app = Flask(__name__)
mongo = pymongo

# create route that renders index.html template
@app.route("/")
def index():
        mars_data = mongo.db.mars_data.find_one()
        return render_template("index.html", mars_data=mars_data)
    
@app.route("/scrape")
def scraped():
    mars_data = mongo.db.mars_data
    mars_data_scrape = scrape_mars.scrape()
    mars_data.update(
        {},
        mars_data_scrape,
        upsert=True
    )

if __name__ == "__main__":
    app.run(debug=True)