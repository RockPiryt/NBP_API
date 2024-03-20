from NBP_API_project import db

class AverageRate(db.Model):
    __tablename__ = "averageRates"
    id = db.Column(db.Integer, primary_key = True )
    rate_date = db.Column(db.Date, nullable=False)
    currency = db.Column(db.String, nullable=False)
    average = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<{self.__class__.__name__}>: {self.rate_date} {self.currency}"