from mongoengine import Document, DateTimeField
from datetime import datetime

class BaseDocument(Document):
    inserted_at = DateTimeField()
    updated_at = DateTimeField()

    meta = {'allow_inheritance': True, 'abstract': True}

    def clean(self):
        if not self.inserted_at:
            self.inserted_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
