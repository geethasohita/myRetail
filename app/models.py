from app import db


class CurrentPrice(db.EmbeddedDocument):
    value = db.FloatField()
    currency_code = db.StringField()


class Product(db.Document):
    product_id = db.StringField()
    product_name = db.StringField()
    product_description = db.StringField()
    current_price = db.EmbeddedDocumentField(CurrentPrice)
