from NBP_API_project import db
from marshmallow import Schema, fields, validate, validates, ValidationError
from datetime import datetime


# Class to generate table in DB
class AverageRate(db.Model):
    __tablename__ = "averageRates"
    id = db.Column(db.Integer, primary_key=True)
    rate_date = db.Column(db.Date, nullable=False)
    currency = db.Column(db.String, nullable=False)
    average = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<{self.__class__.__name__}>: {self.rate_date} {self.currency}"

# Class to serialize python object to json format - create schema
class AverageRateSchema(Schema):
    id = fields.Integer(dump_only=True)
    rate_date = fields.Date("%Y-%m-%d", required=True)
    currency = fields.String(required=True)

    # Check if date is lower or equal current date
    @validates('rate_date')
    def validate_rate_date(self, value):
        now_date = datetime.now().date()
        if value > now_date:
            raise ValidationError(
                f'Rate_date must be lower or equal {now_date}')


rates_schema = AverageRateSchema()
