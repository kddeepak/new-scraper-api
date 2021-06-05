from newsApp import db


class Articles(db.Document):
    site_url = db.StringField()
    story_date = db.DateTimeField
    category = db.StringField()
    source = db.StringField()
    author = db.StringField()
    description = db.StringField()
    title = db.StringField()
    image_url = db.StringField()
    created_at = db.DateTimeField
