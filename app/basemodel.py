from app import db
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError

class BaseMixin:
    id = db.Colomn(db.Integer, primary_key=True)
    create_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False) 
    updated_at= db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.utcnow)


    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        db.session.add(obj)
        try:
            db.session.commit()
            return obj
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e


    @classmethod
    def get_all(cls):
        return cls.query.all()


    @classmethod
    def get_by_id(cls, obj_id):
        if not obj_id:
            return None
        return cls.query.get(obj_id)


    @classmethod
    def get_by_email(cls, email):
        if not email or not isinstance(email, str):
            raise ValueError("Email must be none empty String")
        if not hasattr(cls, "email"):
            raise AttributeError(f'{cls.__name__} has no email column')
        return cls.query.filter_by(email=email).first()


    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        try:
            db.session.commit()
            return self
        except SQLAlchemyError as e:
            raise e
        

    def delete(self):
        db.session.delete(self)
        try:
            db.session.commit()
        except SQLAlchemyError as e:
            raise e
        





    
