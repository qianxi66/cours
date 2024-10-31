# model/crud.py  
from sqlalchemy.orm import Session  
from models import model  

def get_flight_by_id(db: Session, flight_id: int):  
    return db.query(model.Flight).filter(model.Flight.id == flight_id).first()  

def get_all_flights(db: Session):  
    return db.query(model.Flight).all()  

def search_flights(db: Session, from_city: str, to_city: str, date: str):  
    return db.query(model.Flight).filter(  
        model.Flight.from_city == from_city,  
        model.Flight.to_city == to_city,  
        model.Flight.departure_time.like(f'{date}%')  
    ).all()  

def create_user(db: Session, user: model.User):  
    db.add(user)  
    db.commit()  
    db.refresh(user)  
    return user  

def get_user_by_email(db: Session, email: str):  
    return db.query(model.User).filter(model.User.email == email).first()  

def create_order(db: Session, order: model.Order):  
    db.add(order)  
    db.commit()  
    db.refresh(order)  
    return order  

def get_orders_by_user(db: Session, user_id: int):  
    return db.query(model.Order).filter(model.Order.user_id == user_id).all()  

def cancel_order(db: Session, order_id: int):  
    db.query(model.Order).filter(model.Order.id == order_id).delete()  
    db.commit()