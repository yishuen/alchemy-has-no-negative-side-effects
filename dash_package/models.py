from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
Base = declarative_base()
from console import db

#change to sqlalchemy code

class Strain(Base):
    __tablename__ = 'strains'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    race = Column(Text)
    flavors = relationship('Flavor', secondary='strainflavors', back_populates='strains')
    effects = relationship('Effect', secondary='straineffects', back_populates='strains')
    countries = relationship('Country', secondary='straincountries', back_populates='strains')

class Flavor(Base):
    __tablename__ = 'flavors'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    strains = relationship('Strain', secondary='strainflavors', back_populates='flavors')

class StrainFlavor(Base):
    __tablename__ = 'strainflavors'
    strain_id = Column(Integer, ForeignKey('strains.id'), primary_key=True)
    flavor_id = Column(Integer, ForeignKey('flavors.id'), primary_key=True)

class Effect(Base):
    __tablename__ = 'effects'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    type = Column(Text)
    strains = relationship('Strain', secondary='straineffects', back_populates='effects')

class StrainEffects(Base):
    __tablename__ = 'straineffects'
    strain_id = Column(Integer, ForeignKey('strains.id'), primary_key=True)
    effect_id = Column(Integer, ForeignKey('effects.id'), primary_key=True)

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    strains = relationship('Strain', secondary='straincountries', back_populates='countries')

class StrainCountry(Base):
    __tablename__ = 'straincountries'
    strain_id = Column(Integer, ForeignKey('strains.id'), primary_key=True)
    country_id = Column(Integer, ForeignKey('countries.id'), primary_key=True)


engine = create_engine('sqlite:///weed.db')
Base.metadata.create_all(engine)
