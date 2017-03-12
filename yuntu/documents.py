from mongoengine import *


class Publisher(Document):
    name = StringField(max_length=50, required=True)
    address = StringField(max_length=50)
    city = StringField(max_length=60)
    state_province = StringField(max_length=30)
    country = StringField(max_length=50)
    website = URLField(max_length=60)

    def __str__(self):
        return self.name


class Author(Document):
    name = StringField(max_length=30, required=True)
    introduction = MultiLineStringField()
    email = EmailField()

    def __str__(self):
        return self.name


class Book(Document):
    title = StringField(max_length=100)
    authors = ReferenceField(Author)
    publisher = ReferenceField(Publisher)
    publication_date = DateTimeField()
    isbn = StringField(max_length=50)

    def __str__(self):
        return self.title
