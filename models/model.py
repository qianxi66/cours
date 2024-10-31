# model/models.py  
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean  
from models.database import Base  

class Flight(Base):  
    __tablename__ = 'flights'  

    id = Column(Integer, primary_key=True, index=True)  
    from_city = Column(String, nullable=False)  
    to_city = Column(String, nullable=False)  
    from_x = Column(Float)  
    from_y = Column(Float)  
    to_x = Column(Float)  
    to_y = Column(Float)  
    kilometer = Column(Float)  
    name = Column(String)  
    model = Column(String)  
    departure_time = Column(String)  
    arrival_time = Column(String)  
    departure_airport = Column(String)  
    arrival_airport = Column(String)  
    price = Column(Float)  
    schedule = Column(String)  # 周几有航班的信息  

class User(Base):  
    __tablename__ = 'users'  

    id = Column(Integer, primary_key=True, index=True)  
    name = Column(String, nullable=False)  
    email = Column(String, unique=True, nullable=False)  
    phone = Column(String, nullable=False)  
    passport_number = Column(String, unique=True, nullable=False)  

class Order(Base):  
    __tablename__ = 'orders'  

    id = Column(Integer, primary_key=True, index=True)  
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  
    flight_id = Column(Integer, ForeignKey('flights.id'), nullable=False)  
    number_of_tickets = Column(Integer, nullable=False)  
    total_price = Column(Float, nullable=False)  
    booking_date = Column(Date)  
    order_number = Column(String, unique=True, nullable=False)  
    order_food = Column(Boolean, default=False)


    # model/models.py (继续添加)  
class CityNode(Base):  
    __tablename__ = 'city_node'  

    id = Column(Integer, primary_key=True, index=True)  
    name = Column(String, nullable=False)  
    x = Column(Float)  
    y = Column(Float)  

class CityEdge(Base):  
    __tablename__ = 'city_edge'  

    id = Column(Integer, primary_key=True, index=True)  
    from_node = Column(Integer, ForeignKey('city_node.id'), nullable=False)  
    to_node = Column(Integer, ForeignKey('city_node.id'), nullable=False)  
    distance = Column(Float)