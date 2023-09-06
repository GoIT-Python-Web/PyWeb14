from mongoengine import *

connect(
    db="web14",
    host="mongodb+srv://web14user:password@krabaton.5mlpr.gcp.mongodb.net/?retryWrites=true&w=majority",
)


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)
    tags = ListField(StringField(max_length=30))
    meta = {"allow_inheritance": True}


class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    image_path = StringField()


class LinkPost(Post):
    link_url = StringField()
