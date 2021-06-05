from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://newsAppAdmin:newsapppass@newsappcluster.zeppd.mongodb.net'
}
db = MongoEngine()
db.init_app(app)

from newsApp import routes
from newsApp import models
from newsApp import scraper
from newsApp.scraper import yahooFinanceScraper
