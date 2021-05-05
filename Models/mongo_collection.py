from mongoengine import Document, StringField

class Mongo_Colecction(Document):
    File_Id = StringField(required = True)
    Path = StringField(required = True)
    Region = StringField(required = True)
    Update_Date = StringField(required = True)
    Init_Date = StringField(required = True)
    Final_Date = StringField(required = True)
