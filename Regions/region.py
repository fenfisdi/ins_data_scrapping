from .base import BaseDocument
from mongoengine import (
        StringField,
        BooleanField)

class Region(BaseDocument):
    hash = StringField(required=True)
    name = StringField(required=True)
    active = BooleanField(default=True)