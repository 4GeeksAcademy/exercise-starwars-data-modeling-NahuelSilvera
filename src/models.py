import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(60), nullable=False)  
    username = Column(String(30), nullable=False)
    user_creation_date = Column(TIMESTAMP, nullable=False)  

    # Relación con Favoritos
    favorites = relationship("Favorites", back_populates="user")


class Planets(Base):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    climate = Column(String(100), nullable=True)
    terrain = Column(String(100), nullable=True)
    population = Column(Integer, nullable=True)

    # Relación con Favoritos
    favorites = relationship("Favorites", back_populates="planet")


class Characters(Base):
    __tablename__ = 'characters'
    character_id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    species = Column(String(100), nullable=True)
    homeworld = Column(String(100), nullable=True)
    gender = Column(String(20), nullable=True)

    # Relación con Favoritos
    favorites = relationship("Favorites", back_populates="character")


class Favorites(Base):
    __tablename__ = 'favorites'
    favorite_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    favorite_type = Column(String(50), nullable=False)
    favorite_id_ref = Column(Integer, nullable=False)

    # Relaciones
    user = relationship("Users", back_populates="favorites")
    planet = relationship("Planets", back_populates="favorites")
    character = relationship("Characters", back_populates="favorites")

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e

