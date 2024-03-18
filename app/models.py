from . import db 
class property(db.model):
    _tablename_ =  'properties'
    id= db.Column(db.Integer, primary_key= True, autoincremenet= True)
    name= db.Column(db.String(100), nullable=False)
    no_of_beds= db.Column(db.Integer, nullable=False)
    no_of_baths= db.Column(db.Integer, nullable=False)
    location= db.Column(db.String(255), nullable=False)
    amount= db.Column(db.Float, nullable=False)
    type= db.Column(db.String(50), nullable=False)
    description= db.Column(db.Text, nullable=False)
    photo= db.Column(db.String(255), nullable=True)

